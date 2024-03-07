#! /usr/bin/env python
import cv2
import time
import rospy
import numpy as np
from bno055_usb_stick_msgs.msg import Output
from sensor_msgs.msg import Image, LaserScan
from cv_bridge import CvBridge
from std_msgs.msg import Int16
from autominy_msgs.msg import Speed, SteeringAngle
from autominy_msgs.msg import SpeedPWMCommand, NormalizedSteeringCommand
from darknet_ros_msgs.msg import BoundingBoxes

path_data = '/home/ros/Autominy_REAL/autominy_ws/src/dotmex_final/ads/lk_275/'
#path_libs = '/home/dotmex/dotMEX_Autominy_REAL/autominy_ws/src/tmr2023/scripts/libs'
path_libs ='/home/ros/Autominy_REAL/autominy_ws/src/dotmex_final/ads/libs'
import sys
sys.path.insert(1, path_libs)
from lib_lanekeep_functions import lane_keep_f
from lib_lidar_functions import lidar_f
from lib_parking_functions import parking_f
LKF = lane_keep_f()
LF = lidar_f()
PF = parking_f()


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
		self.D = 40.0 #38.0 #34.0
		#V. Lidar
		self.R = np.zeros(360)
		self.s_obj = False
		# V. Parking
		self.step = 0
		self.Parflag = False
		self.Perflag = False
		self.FTP = 0
		self.line_parking = [0.0, 0.0]
		self.c = 0



		#V. Camera
		self.FTC = 0
		self.l = 30 #30 # Tamano de la recta con que se modela el camino
		self.imagenF = np.zeros((640,480))

		#V. Lane-Keeping
		self.y_ref = -15.0
		self.side = 1 #-1 # 1=Derecha -1=Izquierda
		self.v = 185 #145-275
		self.M = 0.0
		self.B = 0.0



		# V. YOLO
		self.v_max = 185 #145-275
		self.s_carro = 0

		#V. Behavior Control
		self.s_rojo = 0
		self.s_peat = 0
		self.s_est = 0
		self.s_ev = 0



		# BAG
		rospy.Subscriber("/sensors/speed",SteeringAngle,self.callback_sp)
		rospy.Subscriber("/sensors/steering",Speed,self.callback_st)
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
#																	DATA BAG
#******************************************************************************************************************
#******************************************************************************************************************
#******************************************************************************************************************
#----------------------------------------------------------------------------------------------------------------
#																	S. Speed
	def callback_sp(self,data1):
		self.sp_sensor = data1.value
#----------------------------------------------------------------------------------------------------------------
#																	S. Steering
	def callback_st(self,data2):
		self.st_sensor = data2.value
#----------------------------------------------------------------------------------------------------------------
#																	Save BAG
	def save_data(self,N,sp_ref,sp_sensor,st_ref,st_sensor):
		t = time.time()
		f = open(path_data+'sensors_bag_'+str(N)+'.csv','a+')
		f.write("%5.6f	%5.6f	%5.6f	%5.6f	%5.6f\n" %(t,sp_ref,sp_sensor,st_ref,st_sensor))
		f.close()
#******************************************************************************************************************
#******************************************************************************************************************
#******************************************************************************************************************
#																	PERCEPTION
#******************************************************************************************************************
#******************************************************************************************************************
#******************************************************************************************************************
	def stop_time(self,delay):
		speed_msg.value = 0
		self.Vpub.publish(speed_msg)
		time.sleep(delay)
#---------------------------------------------------------------------------------------------------------------
#																	Park Signal
	def callback_Park(self, data_park):
		self.s_est = data_park.data
		#print(self.s_est)
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
		self.R = np.clip(data_lidar.ranges,0.08,rmax)				# Satura los datos obtenidos entre 0.08 y rmax [m]
		self.s_obj = LF.lidar_obj(self.R)
		"""
		ev_f = lidar_ev(self.R)
		#print('ev_f ',ev_f)
		if (self.s_ev==1) and (ev_f==True):
			self.s_ev = 0
			self.FT = 0
		"""
#----------------------------------------------------------------------------------------------------------------
#																	CAMERA RGB
	def callback_Cam(self,data_camera):
		#start_time = time.time()
		#_Procesamiento de la imagen
		imagen0 = bridge.imgmsg_to_cv2(data_camera, "bgr8") 	# Imagen cv2
		# Recorta la imagen y la segmenta
		imagenSeg = LKF.seg_img(imagen0, True)
		# Obtiene los pixeles blancos, les quita la distorcion radial y tangencial; y aplica la homografia
		list_px,N = LKF.get_list(imagenSeg,self.l)
		if (N<1000):
			print('No hay camino!')
			LKF.L = LKF.init_L()
			self.FTC = 0
		else:
			# Detecta las lineas de la derecha e izquierda
			if (self.FTC<=5):
				LKF.L = LKF.line_class_FT(500,list_px,LKF.L)
				self.FTC = self.FTC+1
			else:
				LKF.L = LKF.get_lines(list_px,LKF.L,15.0)
			# VISUALIZACION
			#LKF.vis_lines(list_px,LKF.L,self.l)
		#print('t = ', (time.time()-start_time))
		"""
		xh = 299.0
		yh = 149.0
		gamma = 0.5
		mr = LKF.L[0,0]
		br = LKF.L[1,0]
		#self.M = self.M+gamma*(LKF.L[0,0]-self.M)
		#self.B = self.B+gamma*(LKF.L[1,0]-self.B)
		#mr = self.M
		#br = self.B
		d = yh-mr*xh-br/np.sqrt(mr**2+1)
		e_y = self.y_ref-d
		e_psi = -np.arctan(mr)
		#print('mr ',mr)
		#print('br ',br)
		#print('e_y ',e_y)
		#print('e_psi ',e_psi*(180.0/np.pi))
		#print(LKF.L[1,0],LKF.L[1,1])
		print('right ',mr*299.0+br)
		print('left ',LKF.L[0,1]*299.0+LKF.L[1,1])
		print('********************')
		"""
#----------------------------------------------------------------------------------------------------------------
#																	YOLO
	def callback_Yolo(self,data_yolo):
		self.s_peat = 0
		self.s_carro = 0
		self.s_rojo = 0
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
			if (id_number == 8) and (area>=2450): self.s_rojo = 1		# Alto
			#if (id_number == 9) and (area>=2450): self.NoEst = True	# No estacionarse

			# Objetos del camino
			if (id_number == 4) and (area>=1750) and (220<=cx<=450) and (150<=cy<=360): self.s_peat = 1	# Peaton
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
#																	BEHAVIOR SELECTOR
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
		maneuver = 2  #2
		self.side = 1 #self.side = 1, DERECHA // self.side = -1, IZQUIERDA


		if (maneuver==0):
			print('---------ALTO PARCIAL------------')
			self.partial_stop(5.0)
		if (maneuver==1):
			print('---------ALTO TOTAL------------')
			self.total_stop()


		if (maneuver==2):
			print('--------SEGUIMIENTO DEL CARRIL-----------')
			self.lane_keeping()
		"""
		if (maneuver==3):
			print('--------SEGUIMIENTO DEL CARRIL DERECHO-----------')
			#self.lane_keeping(maneuver)
		if (maneuver==4):
			print('--------REBASE-----------')
			#self.lane_keeping(maneuver)
		"""


		if (maneuver==5):
			print('-----------ESTACIONAMIENTO-----------')
			self.parking()

#******************************************************************************************************************
#******************************************************************************************************************
#******************************************************************************************************************
#																	MOVEMENT CONTROL
#******************************************************************************************************************
#******************************************************************************************************************
#******************************************************************************************************************
#----------------------------------------------------------------------------------------------------------------
#																	ALTO PARCIAL
	def partial_stop(self,delay):
			speed_msg.value = 0
			self.Vpub.publish(speed_msg)
			time.sleep(delay)
#----------------------------------------------------------------------------------------------------------------
#																	ALTO TOTAL
	def total_stop(self):
			speed_msg.value = 0
			steering_msg.value = 0.0
			self.Vpub.publish(speed_msg)
			self.Spub.publish(steering_msg)
#----------------------------------------------------------------------------------------------------------------
#																	LANE KEEPING AND PASSING
	def lane_keeping(self):
		"""
		#self.side = 1, DERECHA // self.side = -1, IZQUIERDA
		if (self.side==1):
			self.v = 175
			self.side = 1
			self.x_ref = 118 #115
			self.x_search = 180
			self.l = 30
		if (self.side==-1):
			self.v = self.v_max
			self.side = -1
			self.x_ref = 82 #85
			self.x_search = 20
			self.l = 50
		"""
		#self.side = 1, DERECHA // self.side = -1, IZQUIERDA
		if (self.side==1):
			i = 0
			self.y_ref = 164.0 #-15.0
		if (self.side==-1):
			i = 1
			self.y_ref = 15.0

		# Ley de Control
		Ky = 0.24948692316565374
		Kpsi = 2.853095113181638
		# V = 165-225
		# R	Q11	Q22	Ky			kth
		#			0.35			2.5
		# 1.0	0.1	10.0	0.25809045983258455	2.509303215016082	++
		# 1.0	0.075	11.25	0.22091511879474462	2.6430666678457455	++
		# 1.0	0.0875	12.5	0.23591059897497782	2.7519665652471006	+++
		# 1.0	0.09	13.75	0.23670416124963695	2.856979438018758	++++
		# 1.0	0.1	13.75	0.24948692316565374	2.853095113181638	++++

		# V = 235
		# 1.0   0.1     13.75   0.24948692316565374     2.853095113181638	++++

                # V = 250
		#			0.2			2.65			+
                # 1.0   0.1     13.75   0.24948692316565374     2.853095113181638       +
		# 1.0	0.075	12.5	0.21843677580754153	2.7572214516214926	+
		# 1.0	0.06	10.0	0.2000022159633122	2.526217286397629	++
		# 1.0	0.06375	11.475	0.20327546928919757	2.669391213357197	+++



                # V = 275
		#			0.15			2.85			+
                # 1.0   0.1     13.75   0.24948692316565374     2.853095113181638       +
		# 1.0	0.06	12.0	0.19627613258117674	2.7195433291121223	+

		m = LKF.L[0,i]
		b = LKF.L[1,i]
		#xh = 299.0-(self.l/2.0)
		#yh = 149.0
		#d = yh-m*xh-b/np.sqrt(m**2+1)

		e_y = (m*299+b)-self.y_ref
		e_psi = -np.arctan(m)

		steering_msg.value = np.arctan(-Ky*e_y-Kpsi*e_psi)*(2.0/np.pi) #Normalizado
		if (self.FTC>5): speed_msg.value = 175 #self.v
		else: speed_msg.value = 0

		#print('steering ',steering_msg.value)
		#print('speed ',speed_msg.value)
		#print('e_y ',e_y)
		print('y1 ',m*299.0+b)
		#print(LKF.L)
		#print('e_psi ',e_psi*(180.0/np.pi))
		print('*********************')

		self.Vpub.publish(speed_msg)
		self.Spub.publish(steering_msg)

		# Guardado de datos
                #c = 6
                #self.save_data(c,speed_msg.value,self.sp_sensor,steering_msg.value,self.st_sensor)

#----------------------------------------------------------------------------------------------------------------
#																PERPENDICULAR PARKING
	def perpendicular_parking(self,Nv,r180,k,u):
		print('Maniobra perpendicular')


		if (self.step == 0):
			# "Medicion" de la distancia para acomodarse
			x_alin = 0.12*self.c*(1.0/30.0)
			self.c = self.c+1
			if (x_alin>=0.65):
				self.D = 100.0
				self.FTY = False
				self.step = self.step+1
				self.stop_time(0.1)

		if (self.step == 1):
			u = 1.0*k
			v = -Nv
			if (abs(self.Dyaw)>=90.0): # or (r180<=0.3):
				self.step = self.step + 2

		if (self.step == 2):
			u = 0.0
			v = -Nv
			if (r180<=0.39): self.step = self.step+1

		if (self.step == 3):
			print('Fin de la maniobra')
			u = 0
			v = 0

		return u,v
#----------------------------------------------------------------------------------------------------------------
#																PARALLEL PARKING
	def parallel_parking(self,Nv,r0,r180,k,u):
		print('Maniobra en paralelo')

		if (self.step == 0):
			# "Medicion" de la distancia para acomodarse
			r_alin = self.R[225]
			if (r_alin<=0.3):
				self.D = 40.0
				self.FTY = False
				self.step = self.step+1
				self.stop_time(0.1)

		if (self.step == 1):
			u = 1.0*k
			v = -Nv #*0.85
			if (abs(self.Dyaw)>=self.D): self.step = self.step + 1

		if (self.step == 2):
			u = -1.0*k
			v = -Nv #*0.85
			if (abs(self.Dyaw)<=2.5) or (r180<=0.34): #0.37
				self.step = self.step + 1
				self.delay_time(0.1)

		if (self.step == 3):
			u = 1.0*k
			v = Nv
			if (r0<=0.24) or (abs(self.Dyaw)<=2.5): #0.28
				self.step = self.step + 1

		if (self.step == 4):
			if (abs(self.Dyaw)>=5.0): self.step = 2
			else:
				print('Fin de la maniobra')
				u = 0
				v = 0
		return u,v
#----------------------------------------------------------------------------------------------------------------
#																PARKING
	def parking(self):
		u = 0.0
		Nv = 185 #185
		# Obtiene la distancia entre el lidar y un objeto enfrente/detras
		r0, r180 = LF.polar_roi(self.R)
		k = (-1)*self.side

		if (self.step == 0):
			# Puntos del lidar usados para el ajuste lineal
			if (self.FTP<=30):
				# Ancho de la caja en [m]
				ymax = 0.6
				ymin = 0.1
				Xs,Ys = LF.lidar4ransac_FT(self.R,ymax,ymin,self.side)
				self.FTP = self.FTP+1
			else: Xs,Ys = LF.lidar4ransac(self.R,self.line_parking,5.0)
			m,b = PF.fit_ransac(Xs,Ys)
			self.line_parking = [m, b]
			# Control de la velocidad y el angulo de direccion
			v = Nv
			d_ref = 17.0*k #15.0 # Separacion en [cm]
			u,d = PF.steer_control(m,b,d_ref)

			# Deteccion del espacio suficiente y el tipo de estacionamiento
			depth1 = abs(d_ref/100.0)+0.3 # Profundidad del espacio para estacionarse en paralelo [m]
			depth2 = abs(d_ref/100.0)+0.5 # Profundidad del espacio para estacionarse en perpendicular [m]
			# 0=Ninguno // 1=Paralelo // 2=Perpendicular
			parking_type = PF.parking_type(self.R,self.side,depth1,depth2)

			if (parking_type==1) and (self.Perflag==False):
				self.Parflag = True
			if (parking_type==2) and (self.Parflag==False): 
				self.Perflag = True

		if (self.Parflag==True): u,v = self.parallel_parking(Nv,r0,r180,k,u)
		if (self.Perflag==True): u,v = self.perpendicular_parking(Nv,r180,k,u)


		# Visualizacion
		#print('r0 ',r0)
		#print('Dyaw ',self.Dyaw)
		print('step ',self.step)
		#print('u ',u)
		#print('v ',v)
		print('****************************')
		#LF.vis_lidar(m,b,R)

		speed_msg.value = v
		steering_msg.value = u
		self.Vpub.publish(speed_msg)
		self.Spub.publish(steering_msg)

		# Guardado de datos
		c = 18
		#self.save_data(c,speed_msg.value,self.sp_sensor,steering_msg.value,self.st_sensor)

#################################################################################################################
#################################################################################################################
#################################################################################################################
#								MAIN
if __name__ == '__main__':
	try:
		print("Nodo inicializado: Automated_Driven_System.py")
		rospy.init_node('ads',anonymous=True)
		autominy()
		rospy.spin()
	except rospy.ROSInterruptException:
		pass

