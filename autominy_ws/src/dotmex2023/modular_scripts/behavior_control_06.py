#! /usr/bin/env python
import cv2
import rospy
import numpy as np
from bno055_usb_stick_msgs.msg import Output
from sensor_msgs.msg import Image, LaserScan
from cv_bridge import CvBridge
from std_msgs.msg import Int16
from autominy_msgs.msg import SpeedPWMCommand, NormalizedSteeringCommand
from darknet_ros_msgs.msg import BoundingBoxes

#path_libs = '/home/dotmex/dotMEX_Autominy_REAL/autominy_ws/src/dotmex2023/modular_scripts/libs'
path_libs ='/home/ros/dotMEX_Autominy_REAL/autominy_ws/src/dotmex2023/modular_scripts/libs'
import sys
sys.path.insert(1, path_libs)
from lib_lanekeep_functions import tip, roi_zone, vec_create, line_detector
from lib_lidar_functions import lidar_roi, lidar_left, lidar_ev
from lib_parking_functions import steer_control, fit_ransac
from lib_model_builder import get_KBW
from lib_nn_maneuver import get_NNmaneuver
_,_,B_d,W_d = get_KBW(path_libs+'/NN_maneuver.hdf5')


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
		self.D = 38.0 #34.0
		self.Pflag = False
		#V. Lidar
		self.step = 0
		self.R = np.zeros(360)
		self.s_obj = False
		self.Ev = False
		#V. Camera
		self.l = 30 #30 # Tamano de la recta con que se modela el camino
		self.FT = 0
		self.side = -1 #-1 # 1=Derecha -1=Izquierda
		self.x_ref = 85 #88 #120
		self.x1_h = 85 #88 #120
		self.x_search = 20 #160
		self.imagenF = np.zeros((640,480))
		self.v = 155 #145-275
		#self.e_y_h = 0.0
		#self.Ie_y = 0.0
		#V. Yolo
		self.v_max = 165 #145-275
		self.s_peat = 0
		self.s_carro = 0
		#V. Behavior Control
		self.s_park = 0

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
	def delay_time(self):
		speed_msg.value = 0
		self.Vpub.publish(speed_msg)
		time.sleep(0.1)
#---------------------------------------------------------------------------------------------------------------
#																	Park Signal
	def callback_Park(self, data_park):
		self.s_park = data_park.data
		print(self.s_park)
#----------------------------------------------------------------------------------------------------------------
#																	IMU
	def callback_Imu(self, data_imu):
		c = 1.3
		yaw = data_imu.euler_angles.heading*(180.0/np.pi)
		if (self.FTY==True): self.yaw0 = yaw
		if (self.yaw0>=360.0-self.D*c) and (yaw<=self.D*c): yaw = yaw+360.0
		if (self.yaw0<=self.D*c) and (yaw>=360-self.D*c): yaw = yaw-360.0
		self.Dyaw = self.yaw0-yaw
		#print('yaw0 ',self.yaw0)
		#print('yaw ',yaw)
		#print('Dyaw',self.Dyaw)
		#print('******************************************')
		self.behavior_control()
#----------------------------------------------------------------------------------------------------------------
#																	LIDAR
	def callback_Lidar(self, data_lidar):
		rmax = 1.5 # Distancia maxima de deteccion
		i = 0
		self.R = np.clip(data_lidar.ranges,0.08,rmax)
		cam_post = [157,158,159,160,161,162,200,201,202,203,204]
		self.R.put(cam_post,rmax)	#Quita los postes
		R0_i = self.R[0:12]
		R0_d = self.R[359:347]
		R0 = np.concatenate((R0_i,R0_d),axis=None)
		r0 = np.min(R0)
		if (r0<=0.9): #0.9
			self.s_obj = True
			#self.v_max = 145
		else: self.s_obj = False

		#print('gamma ',np.argmin(self.R))
		#print('rho ',np.min(self.R))
		#ev_f = lidar_ev(self.R)
		#print('ev_f ',ev_f)
		#if (self.Ev==True) and (ev_f==True):
		#	self.Ev = False
		#	self.FT = 0

		"""
		if (self.Obj==True):
			self.Ev = True
			self.FT = 0
		_,Rl,_ = lidar_roi(self.R)
		rmin = np.min(self.R)
		if (Rl==False) and (rmin>=0.55) and (self.Obj==False):
			self.Ev = False
			self.FT = 0
		#print(self.Obj)
		#print(np.min(self.R))
		#print(np.argmin(self.R))
		"""
#----------------------------------------------------------------------------------------------------------------
#																	CAMERA RGB
	def callback_Cam(self,data_camera):
		#____________________________Procesamiento de la imagen
		imagen0 = bridge.imgmsg_to_cv2(data_camera, "bgr8") 	# Imagen cv2
		# Crea la mascara del color segmentado (anaranjado)
		lower = np.array([100,46,136])	#RGB: 100,46,170 # BGR: 0,45,146
		upper = np.array([140,255,255])	#RGB:140,255,255 # BGR: 11,255,255
		imagenS = cv2.inRange(cv2.cvtColor(imagen0,cv2.COLOR_BGR2HSV),lower,upper)
		imagenS = cv2.medianBlur(imagenS,1)
		self.imagenF = tip(imagenS) 	# TIP
#----------------------------------------------------------------------------------------------------------------
#																	YOLO
	def callback_Yolo(self,data_yolo):
		self.s_peat = 0
		self.s_carro = 0
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
			if (id_number == 13) and (area>=2000): self.v_max = 175		# lim 50km_h
			if (id_number == 14) and (area>=2000): self.v_max = 200		# lim 100km_h
			if (id_number == 8) and (area>=2450): self.s_peat = 1		# Alto
			#if (id_number == 9) and (area>=2450): self.NoEst = True	# No estacionarse

			# Objetos del camino
			if (id_number == 4) and (area>=1500) and (220<=cx<=450) and (150<=cy<=360): self.s_peat = 1	# Peaton
			if (id_number == 0) and (area>=8500) and (220<=cx<=425) and (p>=0.85): self.s_carro = 1		# Carro
			#print('p ',p)
			#print('car ',self.s_carro)

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
		"""
		if (abs(self.th)<=0.2618): self.Curve = False
		else: self.Curve = True
		if (self.Obj==True) and (self.Car==True) and (self.Curve==False):
			self.Ev = True
			self.FTY = False
		"""
		#Entradas:
		#[Est Curve Ev Obj Ped tfRed] -- Renglones de In_bin
		#Salidas
		#[Alto SeguirCarril Evasion Estacionamiento] -- Renglones de Out_bin
		"""
		x = np.array([int(self.Park),int(self.Curve),int(self.Ev),int(self.Obj),int(self.Ped),int(self.tfRed)])
		y = get_NNmaneuver(B_d,W_d,x)
		maneuver = np.argmax(y)
		"""

		# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		#if (self.s_park==1): maneuver = 3
		#else: maneuver = 1
		#if (self.s_peat==0): maneuver = 1
		#else: maneuver = 0

		if (self.s_peat==0):
			if (self.s_obj==1) and (self.s_carro==1):
				self.Ev=True
				self.FT = 0
			if (self.Ev==True): maneuver = 2
			else: maneuver = 1
		else: maneuver = 0

                ev_f = lidar_ev(self.R)
                if (self.Ev==True) and (ev_f==True):
                        self.Ev = False
                        self.FT = 0

		# Maneuver selector
		if (maneuver==0):
			print('---------ALTO------------')
			self.stop_car()
		if (maneuver==1):
			print('--------SEGUIMIENTO DEL CARRIL-----------')
			self.lane_keeping(maneuver)
		if (maneuver==2):
			print('--------EVASION-----------')
			self.lane_keeping(maneuver)
		if (maneuver==3): self.parking()

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
			self.v = 145
			self.side = 1
			self.x_ref = 115 #115
			self.x_search = 180
			self.l = 30
		if (maneuver==1):
			self.v = self.v_max
			self.side = -1
			self.x_ref = 84 #85
			self.x_search = 10
			self.l = 50

		speed_msg.value = self.v
		y1 = 0
		y2 = 0
		#________________________________________Busca la linea
		if (self.FT<=5):
			#print('-----------INCORPORAMIENTO AL CARRIL-----------')
			x1 = self.x_search
			self.FT = self.FT+1
		else: x1 = self.x1_h
		# self.side = 1, DERECHA // self.side = -1, IZQUIERDA
		x1,y1,x2,y2 = line_detector(self.imagenF,x1,self.l,self.side)
		self.x1_h = x1
		#x2_h = x2
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
		#print('steering ',steering_msg.value)
		#print('speed ',speed_msg.value)
		#print('*********************')
		"""
	 	#Visualizacion
		#namedWindow("homografia");
		imagenS = cv2.cvtColor(self.imagenF,cv2.COLOR_GRAY2BGR)
		imagenS = cv2.circle(imagenS,(x1,y1),3,(0, 0, 255),-1)
		imagenS = cv2.circle(imagenS,(x2,y2),3,(0, 0, 255),-1)
		imagenS = cv2.line(imagenS, (x1,y1), (x2,y2), (0, 0, 255), 2)
		cv2.imshow('homografia',imagenS)
		cv2.moveWindow("homografia", 400,20)
		cv2.waitKey(1)
		"""
		self.Vpub.publish(speed_msg)
		self.Spub.publish(steering_msg)
#----------------------------------------------------------------------------------------------------------------
#																	PARKING
	def parking(self):
			print('-----------ESTACIONAMIENTO-----------')
			Nv = 185 #215
			R0_i = self.R[0:14]
			R0_d = self.R[344:359]
			R0 = np.concatenate((R0_i,R0_d))
			r0 = np.amin(R0)
			r180 = np.amin(self.R[169:199]) #162,199 #np.amin(self.R[165:205])
			r90 = self.R[89]
			r_alin = self.R[130] #135
			if (self.step == 0):
				rmax = 3.0
				rmin = 0.10
				R_left = lidar_left(self.R,rmax,rmin)
				m,b = fit_ransac(R_left,rmax)
				v = Nv
				d_ref = 15.0
				u,d = steer_control(m,b,d_ref)
				_,flag_l,_ = lidar_roi(self.R)
				if (flag_l==False):
					self.Pflag =True
				if (self.Pflag==True) and (r90<0.3) and (r_alin<0.3): #90
					#self.D = np.arccos(1-(d*0.01+0.1)/(2.0*0.63))*(180/np.pi)-5.8 # Calculo de D de cambio
					self.FTY = False
					self.step = self.step+1
					self.delay_time()

			if (self.step == 1):
				print('Inicio de la maniobra')
				u = 1.0
				v = -Nv #*0.85
				if (self.Dyaw<=-self.D): self.step = self.step + 1

			if (self.step == 2):
				u = -1.0
				v = -Nv #*0.85
				if (self.Dyaw>=0.0) or (r180<=0.32): #0.32 #0.35
					self.step = self.step + 1
					self.delay_time()

			if (self.step == 3):
				#if (self.Dyaw<0.0): u = 1
				#if (self.Dyaw>=0.0): u = 0
				u = 1.0
				v = Nv
				if (r0<=0.28) or (self.Dyaw>=0.0) : #0.25
					self.step = self.step + 1

			if (self.step == 4):
				#v = 0
				#u = 0
				if (self.Dyaw<0.0):
					self.step = 2
				#	#u = 1
				#	#v = -Nv
				if (self.Dyaw>=0.0):
					print('Fin de la maniobra')
					u = 0
					v = 0
			"""
			# Visualizacion
			x1 = -200
			x2 = 200
			y1_r = int(299.0-(m*x1+b))
			y2_r = int(299.0-(m*x2+b))
			x1_r = x1+299
			x2_r = x2+299
			x1_min = int(100.0*r_min*np.cos(th_min)+299.0)
			y1_min = int(299.0-100.0*r_min*np.sin(th_min))
			imagenR = np.zeros((600,600,3))
			font = cv2.FONT_HERSHEY_SIMPLEX
			imagenR =cv2.line(imagenR, (299,299),(329,299), (255,0,0), 2) #ejeX
			imagenR = cv2.putText(imagenR, 'X', (331, 299), font, 0.4, (255,255,255), 1, cv2.LINE_AA)
			imagenR =cv2.line(imagenR, (299,299),(299,269), (0,0,255), 2) #ejeY
			imagenR = cv2.putText(imagenR, 'Y', (299,267), font, 0.4, (255,255,255), 1, cv2.LINE_AA)
			imagenR =cv2.line(imagenR, (x1_r,y1_r),(x2_r,y2_r), (0,125,255), 2)
			imagenR =cv2.line(imagenR, (299,299),(x1_min,y1_min), (255,255,0), 2)
			imagenR = cv2.circle(imagenR,(299,299),2,(255, 255, 255),-1)
			i = 0
			for j in self.R:
				r_l = j*100.0
				th_l = (i)*(np.pi/180.0)
				x = int(r_l*np.cos(th_l)+299.0)
				y = int(299.0-r_l*np.sin(th_l))
				imagenR = cv2.circle(imagenR,(x,y),2,(0, 0, 255),-1)
				i = i+1
			cv2.imshow('lidar',imagenR)
			#cv2.moveWindow("lidar", 400,400)
			cv2.waitKey(1)
			"""
			#print('r0 ',r0)
			#print('Dyaw ',self.Dyaw)
			print('step ',self.step)
			print('u ',u)
			print('v ',v)
			#print('****************************')
			speed_msg.value = v
			steering_msg.value = u
			self.Vpub.publish(speed_msg)
			self.Spub.publish(steering_msg)
#################################################################################################################
#################################################################################################################
#################################################################################################################
#								MAIN
if __name__ == '__main__':
	print("Nodo inicializado: behavior_control_01.py")
	rospy.init_node('behavior_control_01',anonymous=True)
	autominy()
	rospy.spin()

