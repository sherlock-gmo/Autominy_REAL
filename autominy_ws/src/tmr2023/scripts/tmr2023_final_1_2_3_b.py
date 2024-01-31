#! /usr/bin/env python
import cv2
import time
import rospy
import numpy as np
from bno055_usb_stick_msgs.msg import Output
from sensor_msgs.msg import Image, LaserScan
from cv_bridge import CvBridge
from std_msgs.msg import Int16
from autominy_msgs.msg import SpeedPWMCommand, NormalizedSteeringCommand
from darknet_ros_msgs.msg import BoundingBoxes

#path_libs = '/home/dotmex/dotMEX_Autominy_REAL/autominy_ws/src/tmr2023/scripts/libs'
path_libs ='/home/ros/dotMEX_Autominy_REAL/autominy_ws/src/tmr2023/scripts/libs'
import sys
sys.path.insert(1, path_libs)
from lib_lanekeep_functions import tip, roi_zone, vec_create, line_detector #,vis_cam
from lib_lidar_functions import lidar_roi_f, lidar4ransac, lidar_ev, lidar_roi_f2     #,vis_lidar
from lib_parking_functions import steer_control, fit_ransac
from lib_model_builder import get_KBW
from lib_nn_maneuver import get_NNmaneuver
_,_,B_d,W_d = get_KBW(path_libs+'/behavior_selector_weights.h5')


bridge = CvBridge()
speed_msg = SpeedPWMCommand() #-1000 to 1000 pwm
steering_msg = NormalizedSteeringCommand() # -1.0 to 1.0
#################################################################################################################
#################################################################################################################
#################################################################################################################
class autominy(object):
#----------------------------------------------------------------------------------------------------------------
#									INIT
#----------------------------------------------------------------------------------------------------------------
	def __init__(self):
		# V. Imu
		self.FTY = True
		self.yaw0 = 0.0
		self.Dyaw = 0.0
		self.D = 38.0 #38.0 #34.0
		self.Pflag = False
		#V. Lidar
		self.step = 0
		self.R = np.zeros(360)
		self.s_obj = 0
		#V. Camera
		self.l = 30 #30 # Tamano de la recta con que se modela el camino
		self.FT = 0
		self.side = 1 #-1 # 1=Derecha -1=Izquierda
		self.x_ref = 118 #I 85 #D 120
		self.x1_h = 118 #I 85 #D 120
		self.x_search = 180 #I 20 #D 160
		self.imagenF = np.zeros((640,480))
		self.v = 185 #145-275
		#self.e_y_h = 0.0
		#self.Ie_y = 0.0
		# V. YOLO
		self.v_max = 185 #235 #185-275
		self.s_carro = 0
		self.s_alto = 0
		#V. Behavior Control
		self.s_rojo = 0
		self.s_peat = 0
		self.s_est = 0
		self.s_ev = 0
		#V. Parallel Parking
		self.space_count = 0
		self.stop_rs = False
		self.car1 = False
		self.space_free = False



		rospy.Subscriber('/parking',Int16,self.callback_Park)
		rospy.Subscriber('/sensors/bno055/output', Output, self.callback_Imu)
		rospy.Subscriber('/sensors/rplidar/scan', LaserScan, self.callback_Lidar)
		rospy.Subscriber("/sensors/camera/color/image_raw",Image,self.callback_Cam)
		rospy.Subscriber("/darknet_ros/bounding_boxes",BoundingBoxes,self.callback_Yolo)
		self.Vpub = rospy.Publisher('/actuators/speed_pwm',SpeedPWMCommand,queue_size=15)
		self.Spub = rospy.Publisher('/actuators/steering_normalized',NormalizedSteeringCommand,queue_size=15)
#******************************************************************************************************************
#******************************************************************************************************************
#******************************************************************************************************************
#																	PERCEPTION
#******************************************************************************************************************
#******************************************************************************************************************
#******************************************************************************************************************
	def delay_time(self,delay):
		speed_msg.value = 0
		self.Vpub.publish(speed_msg)
		time.sleep(delay)
#---------------------------------------------------------------------------------------------------------------
#																	Park Signal
	def callback_Park(self, data_park):
		self.s_est = data_park.data
		print(self.s_est)
#----------------------------------------------------------------------------------------------------------------
#																	IMU
	def callback_Imu(self, data_imu):
		c = 1.3
		yaw = data_imu.euler_angles.heading*(180.0/np.pi)
		if (self.FTY==True): self.yaw0 = yaw
		if (self.yaw0>=360.0-self.D*c) and (yaw<=self.D*c): yaw = yaw+360.0
		if (self.yaw0<=self.D*c) and (yaw>=360-self.D*c): yaw = yaw-360.0
		self.Dyaw = self.yaw0-yaw
		self.behavior_control()
#----------------------------------------------------------------------------------------------------------------
#																	LIDAR
	def callback_Lidar(self, data_lidar):
		rmax = 2.5 # Distancia maxima de deteccion
		i = 0
		self.R = np.clip(data_lidar.ranges,0.08,rmax)
		cam_post = [157,158,159,160,161,162,200,201,202,203,204]
		self.R.put(cam_post,rmax)	#Quita los postes
		R0_i = self.R[0:12]
		R0_d = self.R[359:347]
		R0 = np.concatenate((R0_i,R0_d),axis=None)
		r0 = np.min(R0)
		if (r0<=0.9): #0.9
			self.s_obj = 1
		else: self.s_obj = 0
#----------------------------------------------------------------------------------------------------------------
#																	CAMERA RGB
	def callback_Cam(self,data_camera):
		#____________________________Procesamiento de la imagen
		imagen0 = bridge.imgmsg_to_cv2(data_camera, "bgr8") 	# Imagen cv2
		# Crea la mascara del color segmentado (anaranjado)
		lower = np.array([100,95,125])	#RGB: 100,46,170 # BGR: 0,45,146
		upper = np.array([140,255,255])	#RGB:140,255,255 # BGR: 11,255,255
		imagenS = cv2.inRange(cv2.cvtColor(imagen0,cv2.COLOR_BGR2HSV),lower,upper)
		imagenS = cv2.medianBlur(imagenS,1)
		#imagenS = cv2.Sobel(imagenS,cv2.CV_8U,1,0, ksize=3)
		self.imagenF = tip(imagenS) 	# TIP
#----------------------------------------------------------------------------------------------------------------
#																	YOLO
	def callback_Yolo(self,data_yolo):
		self.s_peat = 0
		self.s_carro = 0
		self.s_rojo = 0
		self.s_alto = 0
		id_class = data_yolo.bounding_boxes
		for i in range(len(id_class)):
			id_number = id_class[i].id
			area = (id_class[i].xmax-id_class[i].xmin)*(id_class[i].ymax-id_class[i].ymin)
			cx = int(id_class[i].xmin+(id_class[i].xmax-id_class[i].xmin)/2.0)
			cy = int(id_class[i].ymin+(id_class[i].ymax-id_class[i].ymin)/2.0)
			p = id_class[i].probability
			# Senales de transito
			#if (id_number == 15) and (area>=2167): self.stop = False 	# Sem Verde
			#if (id_number == 17) and (area>=2167): self.stop = True	# Sem Rojo
			if (id_number == 13) and (area>=2000): self.v_max = 185		# lim 50km_h
			if (id_number == 14) and (area>=2000): self.v_max = 235		# lim 100km_h
			if (id_number == 8) and (area>=1700): self.s_alto = 1		# Alto
			# v=225 => area = 2000
			# v=235 => area = xxx
			#if (id_number == 9) and (area>=2450): self.NoEst = True	# No estacionarse

			# Objetos del camino
			if (id_number == 4) and (area>=1500) and (220<=cx<=450) and (150<=cy<=360): self.s_peat = 1	# Peaton
			#if (id_number == 0) and (area>=8500) and (215<=cx<=430) and (p>=0.8): self.s_carro = 1		# Carro
			if (id_number == 0) and (area>=6000) and (215<=cx<=430) and (p>=0.8): self.s_carro = 1          # Carro

			"""
			id		class			area_min
			----------------------------------------------
			0		carro
			1		camion
			2		bicicleta
			3		moto
			4		peaton
			5		perro
			6		gato
			7		caballo
			8		alto
			9		noest
			10		20km
			11		30km
			12		40km
			13		50km			2450
			14		100km			1500
			15		sem_verde
			16		sem_amarillo
			17		sem_rojo
			18		sem_NA
			19		tren
			"""

#******************************************************************************************************************
#******************************************************************************************************************
#******************************************************************************************************************
#																	BEHAVIOR CONTROL
#******************************************************************************************************************
#******************************************************************************************************************
#******************************************************************************************************************
	def behavior_control(self):
		#Entradas:
		#[s_rojo s_peat s_ev s_est]
		#Salidas
		#[Alto S.Carril Evasion Estacionamiento]
		"""
		# Inicia la evasion
		if (self.s_obj==1) and (self.s_carro==1):
			self.s_ev=1
			self.FT = 0
		# Termina la evasion
		ev_f = lidar_ev(self.R)
		if (self.s_ev==1) and (ev_f==True):
			self.s_ev = 0
			self.FT = 0

		x = np.reshape(np.array([int(self.s_rojo),int(self.s_peat),int(self.s_ev),int(self.s_est)]),(1,4))
		y = get_NNmaneuver(B_d,W_d,x)
		maneuver = np.argmax(y)
		"""

		"""
		# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		#if (self.s_est==1): maneuver = 3
		#else: maneuver = 1
		#if (self.s_peat==0): maneuver = 1
		#else: maneuver = 0
		if (self.s_peat==0):
			if (self.s_obj==1) and (self.s_carro==1):
				self.s_ev=1
				self.FT = 0
			if (self.s_ev==1): maneuver = 2
			else: maneuver = 1
		else: maneuver = 0
		"""


		# Maneuver selector
		"""
		# Prueba 1
		if (self.s_alto==0):
			maneuver = 2
			self.side = 1 #1 #self.side = 1, DERECHA // self.side = -1, IZQUIERDA
		if (self.s_alto==1):
			maneuver = 5
		"""
		"""
		# Pruebas 2 y 3
		if (self.s_obj==1) and (self.s_carro==1):
			self.s_ev=1
		if (self.s_ev==0):
			maneuver = 2
		else:
			maneuver = 1
			self.FT = 0
			self.space_count = self.space_count+1
			x_alin = (0.065)*(1.0/30.0)*self.space_count # v=185 => 0.065[m/s]
			if (x_alin>=0.8):
				maneuver = 2
				self.s_ev = 0
				self.FT = 0
				self.space_count = 0
		"""
		
		# Prueba 4
		maneuver = 4
		self.side = 1
		

		if (maneuver==0):
			print('---------ALTO TOTAL------------')
			self.stop_car()
		if (maneuver==1):
			print('--------SEGUIMIENTO DEL CARRIL IZQUIERDO-----------')
			self.lane_keeping(maneuver)
		if (maneuver==2):
			print('--------SEGUIMIENTO DEL CARRIL DERECHO-----------')
			self.lane_keeping(maneuver)
		if (maneuver==3):
			print('-----------ESTACIONAMIENTO PARALELO-----------')
			self.parallel_parking()
		if (maneuver==4):
			print('-----------ESTACIONAMIENTO PPERPENDICULAR-----------')
			self.perpendicular_parking()
		if (maneuver==5):
			print('------------ALTO PARCIAL---------')
			self.stop_car_p()
#******************************************************************************************************************
#******************************************************************************************************************
#******************************************************************************************************************
#																	UNDERLEVEL CONTROL
#******************************************************************************************************************
#******************************************************************************************************************
#******************************************************************************************************************
#----------------------------------------------------------------------------------------------------------------
#																	STOP CAR
	def stop_car(self):
			#self.v_max = 0
			speed_msg.value = 0
			steering_msg.value = 0.0
			self.Vpub.publish(speed_msg)
			self.Spub.publish(steering_msg)
#----------------------------------------------------------------------------------------------------------------
#																	LANE KEEPING AND PASSING
	def lane_keeping(self,maneuver):
		if (maneuver==2):
			# Derecha
			self.v = self.v_max #175
			self.side = 1
			self.x_ref = 118 #118
			self.x_search = 150 #180
			self.l = 30
		if (maneuver==1):
			# Izquierda
			self.v = 185  #175
			self.side = -1
			self.x_ref = 75 #82
			self.x_search = 30
			self.l = 50

		speed_msg.value = self.v
		y1 = 0
		y2 = 0
		#________________________________________Busca la linea
		if (self.FT<=10): #10
			#print('-----------INCORPORAMIENTO AL CARRIL-----------')
			x1 = self.x_search
			self.FT = self.FT+1
		else: x1 = self.x1_h
		#print('x1 ',x1)
		# self.side = 1, DERECHA // self.side = -1, IZQUIERDA
		x1,y1,x2,y2 = line_detector(self.imagenF,x1,self.l,self.side)
		self.x1_h = x1
		#________________________________________Ley de Control
		Ky =  0.45631688 #0.48340796
		Kth = 0.5265962 #0.53838659
		#KDy = 0.0
		#KIy = 0.0
		e_y = x1-self.x_ref
		e_th = np.arctan2(x2-x1,self.l) #En radianes

		#h = 1.0/30.0
		#De_y = (e_y-self.e_y_h)/h
		#self.Ie_y = self.Ie_y+h*e_y

		steering_msg.value = np.arctan(-Ky*e_y-Kth*e_th)*(2.0/np.pi) #Normalizado
		#self.e_y_h = e_y
		#print(x1,y1)
		#print(x2,y2)
		print('steering ',steering_msg.value)
		#print('speed ',speed_msg.value)
		print('*********************')

	 	#Visualizacion
		#vis_cam(imagenF,x1,x2,y1,y2)
		self.Vpub.publish(speed_msg)
		self.Spub.publish(steering_msg)
#----------------------------------------------------------------------------------------------------------------
#																PARALLEL PARKING
	def parallel_parking(self):
			Nv = 185 #185 #215
			R0_i = self.R[0:29]
			R0_d = self.R[329:359]
			R0 = np.concatenate((R0_i,R0_d))
			r0 = np.amin(R0)
			r180 = np.amin(self.R[159:199]) #162,199 #np.amin(self.R[165:205])
			k = (-1)*self.side
			
			
			# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			if (self.side==-1):
				r_alin1 = self.R[130] #135
				r_alin2 = self.R[89]
			else:
				r_alin1 = self.R[230] #135
				r_alin2 = self.R[269]
			# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			
			
			if (self.step == 0):
				ymax = 0.3
				ymin = 0.1
				R_side = lidar4ransac(self.R,ymax,ymin,self.side) # Puntos del lidar usados para el RANSAC
				m,b = fit_ransac(R_side,rmax)
				v = Nv
				d_ref = 15.0*k #15.0 # Separacion en [cm]
				u,d = steer_control(m,b,d_ref)
				depth = 0.35 # Profundidad del espacio para estacionarse [m]
				"""
				flag_space, count_side = lidar_roi_f(self.R,self.side,depth)
				if (flag_space==True): self.Pflag =True
				if (self.Pflag==True) and (r_alin2<0.3) and (r_alin1<0.3): #90 #!!!!!!!!!!!!!!!!!!!!!!!!!!!
					self.FTY = False
					self.step = self.step+1
					self.delay_time(0.1)
				"""
				flag_space = lidar_roi_f(self.R,self.side, depth)
				if (flag_space==True) and (abs(abs(d_ref)-abs(d))<=5.0): self.Pflag =True
				if (self.Pflag== True): self.space_count = self.space_count+1
				x_alin = (0.065)*(1.0/30.0)*self.space_count #0.065
				print('Pflag ', self.Pflag)
				if (self.Pflag==True) and (x_alin>=0.65):
					self.FTY = False
					self.step = self.step+1
					self.delay_time(0.1)


			if (self.step == 1):
				print('Inicio de la maniobra')
				u = 1.0*k
				v = -Nv #*0.85
				if (abs(self.Dyaw)>=self.D): self.step = self.step + 1

			if (self.step == 2):
				u = -1.0*k
				v = -Nv #*0.85
				if (abs(self.Dyaw)<=5.0) or (r180<=0.34): #0.37
					self.step = self.step + 1
					self.delay_time(0.1)

			if (self.step == 3):
				u = 1.0*k
				v = Nv
				if (r0<=0.22) or (abs(self.Dyaw)<=5.0): #0.28
					self.step = self.step + 1

			if (self.step == 4):
				if (abs(self.Dyaw)>=5.0): self.step = 2
				else:
					print('Fin de la maniobra')
					u = 0
					v = 0

			#print('r0 ',r0)
			print('Dyaw ',self.Dyaw)
			print('step ',self.step)
			#print('u ',u)
			#print('v ',v)
			print('****************************')

			# Visualizacion
			#vis_lidar(m,b,R)
			speed_msg.value = v
			steering_msg.value = u
			self.Vpub.publish(speed_msg)
			self.Spub.publish(steering_msg)
#----------------------------------------------------------------------------------------------------------------
#																PERPENDICULAR PARKING
	def perpendicular_parking(self):
			Nv = 250 #250 Bateria FULL
			r180 = np.amin(self.R[159:199]) #162,199 #np.amin(self.R[165:205])
			k = (-1)*self.side
			#self.d = 2.0
			#m = 5.0
			if (self.step == 0):
				ymax = 1.75 #[m]
				ymin = 0.35 #0.35
				R_side = lidar4ransac(self.R,ymax,ymin,self.side) # Puntos del lidar usados para el RANSAC
				m,b = fit_ransac(R_side,3.0)
				v = Nv
				d_ref = 80.0*k # Separacion en [cm]
				u,d = steer_control(m,b,d_ref)
				if (abs(m)<=0.2) and (abs(d_ref-d)<=0.05):
					self.stop_rs = True
				if (self.stop_rs == True):
					print('STOP RANSAC')
					u = 0.0
				else: u,self.d = steer_control(m,b,d_ref)

				depth = 0.6 # Profundidad del espacio para estacionarse [m]
				flag_space = lidar_roi_f(self.R,self.side, depth)
				flag_space2 = lidar_roi_f2(self.R,self.side)
				print(flag_space)
				if (flag_space == False) and (self.car1==False):
					self.car1 = True
					self.stop_car_p()
				if (self.car1== True) and (flag_space==True):
					self.space_free = True
					self.stop_car_p()
				if (flag_space2 == True) and (self.space_free == True) and (self.car1==True):
					#self.step = self.step+1
					self.stop_car_p()
					#self.step = self.step+1

				#if (self.car1==True) and (self.space_free==True):
				#flag_space2 = lidar_roi_f2(self.R,self.side)

				#if (self.car1==True) and (flag_space==False) and (flag_space2==True):
				#	self.stop_car_p()
					#self.step = self.step+1


				#if (self.car_roi==True) and (flag_space2 == True): self.step = self.step+1







				"""
				if (flag_space==True) and (abs(abs(d_ref)-abs(d))<=5.0): self.Pflag =True
				if (self.Pflag== True): self.space_count = self.space_count+1
				x_alin = (0.05)*(1.0/30.0)*self.space_count #0.065
				#print('Pflag ', self.Pflag)
				if (self.Pflag==True) and (x_alin>=0.65):
					v = 0
					#self.FTY = False
					#self.step = self.step+1
					#self.delay_time(1.0)
				"""


			if (self.step == 1):
				print('Inicio de la maniobra')
				u = 0.0 #1.0*k
				v = 0.0 #-Nv*1.0
				if (abs(self.Dyaw)>=90.0) or (r180<=0.3):
					v = 0.0
					self.step = self.step + 1

			if (self.step == 2):
				print('Fin de la maniobra')
				u = 0
				v = 0

			#print('r0 ',r0)
			#print('Dyaw ',self.Dyaw)
			#print('step ',self.step)
			#print('u ',u)
			#print('v ',v)
			print('****************************')

			# Visualizacion
			#vis_lidar(m,b,R)
			speed_msg.value = v
			steering_msg.value = u
			self.Vpub.publish(speed_msg)
			self.Spub.publish(steering_msg)
#----------------------------------------------------------------------------------------------------------------
#
	def stop_car_p(self):
		self.stop_car()
		self.delay_time(1.0) #5.0
		self.s_alto = 0
#################################################################################################################
#################################################################################################################
#################################################################################################################
#								MAIN
if __name__ == '__main__':
	print("Nodo inicializado: TMR_2023.py")
	rospy.init_node('tmr_2023',anonymous=True)
	autominy()
	rospy.spin()

