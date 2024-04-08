#! /usr/bin/env python
import cv2
import rospy
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from autominy_msgs.msg import SpeedPWMCommand, NormalizedSteeringCommand

import time



path_libs ='/home/ros/Autominy_REAL/autominy_ws/src/dotmex_final/control/libs'
import sys
sys.path.insert(1, path_libs)
from lib_lanekeep_functions import lane_keep_f

LKF = lane_keep_f()

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
		"""
		#V. Camera
		self.l = 30 #30 # Tamano de la recta con que se modela el camino
		self.FT = 0
		self.side = -1 #-1 # 1=Derecha -1=Izquierda
		self.x_ref = 85 #88 #120
		self.x1_h = 85 #88 #120
		self.x_search = 20 #160
		self.imagenF = np.zeros((640,480))
		self.v = 185 #145-275
		"""
		self.k = 0
		self.W = np.zeros((3,2))

		self.x0 = 0
		self.y0 = 0
		self.x1 = 0
		self.y1 = 0
		self.imagenT = np.zeros((960,540,3))

		rospy.Subscriber("/sensors/camera/color/image_raw",Image,self.callback_Cam)
		self.Vpub = rospy.Publisher('/actuators/speed_pwm',SpeedPWMCommand,queue_size=15)
		self.Spub = rospy.Publisher('/actuators/steering_normalized',NormalizedSteeringCommand,queue_size=15)
#******************************************************************************************************************
#******************************************************************************************************************
#******************************************************************************************************************
#																	CAMERA RGB
#----------------------------------------------------------------------------------------------------------------
	def callback_Cam(self,data_camera):
		#start_time = time.time()

		#____________________________Procesamiento de la imagen
		imagen0 = bridge.imgmsg_to_cv2(data_camera, "bgr8") 	# Imagen cv2
		# Segmenta la imagen
		imagenSeg = LKF.seg_img(imagen0, True)	
		# Obtiene los pixeles blancos y les aplica quita la distorcion radial y tangencial, y aplica la homografia
		list_px = LKF.get_list(imagenSeg) 

		if (self.k==0):
			# Se entrena el clasificador de datos durante K iteraciones
			K = 150 #150	 
			for k in range (0,K): 
				#	Se busca un punto de forma aleatoria y se hace una regresion lineal con sus vecinos
				p, m, b = LKF.min_line(list_px,LKF.eps,LKF.n0)
				# Se actualizan el clasificador de lineas
				LKF.L = LKF.act_line(LKF.L,p,m,b,LKF.alpha)
				# Se obtienen las lineas segmentadas
				self.k=self.k+1

		LKF.L, R = LKF.get_lines(list_px,LKF.L,10.0)

		#print('t = ', (time.time()-start_time))
		#print(R)


		# VISUALIZACION
		x1r = 200
		x2r = 299
		y1r = int(round(x1r*LKF.L[0,0]+LKF.L[1,0]))
		y2r = int(round(x2r*LKF.L[0,0]+LKF.L[1,0]))
		x1c = 200
		x2c = 299
		y1c = int(round(x1c*LKF.L[0,1]+LKF.L[1,1]))
		y2c = int(round(x2c*LKF.L[0,1]+LKF.L[1,1]))
		x1l = 200
		x2l = 299
		y1l = int(round(x1l*LKF.L[0,2]+LKF.L[1,2]))
		y2l = int(round(x2l*LKF.L[0,2]+LKF.L[1,2]))
		imagenH = np.zeros((300,300,3))
		for x,y in list_px:	imagenH = cv2.circle(imagenH, (int(x), int(y)), 2, (0, 255, 0), -1)
		imagenH =cv2.line(imagenH, (y1r,x1r),(y2r,x2r), (0,0,255), 3)
		imagenH =cv2.line(imagenH, (y1c,x1c),(y2c,x2c), (0,0,255), 3)
		imagenH =cv2.line(imagenH, (y1l,x1l),(y2l,x2l), (0,0,255), 3)

		cv2.imshow('test',imagenH)
		cv2.waitKey(1)


		"""
#******************************************************************************************************************
#******************************************************************************************************************
#******************************************************************************************************************
#																	LANE KEEPING AND PASSING
#----------------------------------------------------------------------------------------------------------------
	def lane_keeping(self,maneuver):
		if (maneuver==2):
			self.v = 175
			self.side = 1
			self.x_ref = 118 #115
			self.x_search = 180
			self.l = 30
		if (maneuver==1):
			self.v = self.v_max
			self.side = -1
			self.x_ref = 82 #85
			self.x_search = 20
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
		print('speed ',speed_msg.value)
		print('*********************')
		"""
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
		#self.Vpub.publish(speed_msg)
		#self.Spub.publish(steering_msg)
#################################################################################################################
#################################################################################################################
#################################################################################################################
#								MAIN
if __name__ == '__main__':
	print("Nodo inicializado: optimal_control.py")
	rospy.init_node('optimal_control',anonymous=True)
	autominy()
	rospy.spin()

