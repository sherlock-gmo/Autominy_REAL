#! /usr/bin/env python
import cv2
import rospy
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from autominy_msgs.msg import SpeedPWMCommand, NormalizedSteeringCommand

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
		rospy.Subscriber("/sensors/camera/color/image_raw",Image,self.callback_Cam)
		self.Vpub = rospy.Publisher('/actuators/speed_pwm',SpeedPWMCommand,queue_size=15)
		self.Spub = rospy.Publisher('/actuators/steering_normalized',NormalizedSteeringCommand,queue_size=15)
#******************************************************************************************************************
#******************************************************************************************************************
#******************************************************************************************************************
#																	CAMERA RGB
#----------------------------------------------------------------------------------------------------------------
	def callback_Cam(self,data_camera):
		#____________________________Procesamiento de la imagen
		imagen0 = bridge.imgmsg_to_cv2(data_camera, "bgr8") 	# Imagen cv2
		# Segmenta la imagen
		imagenSeg = LKF.seg_img(imagen0)	
		# Obtiene los pixeles blancos y les aplica quita la distorcion radial y tangencial, y aplica la homografia
		list_px = LKF.get_list(imagenSeg) 

		# Le aplica RANSAC a los puntos y los separa en grupos
		# El eje vertical de la imagen es el eje x
		# El eje horizontal de la imagen es el eje y
		M, B, R, Y0 = LKF.get_lines(list_px) 														
		#print('M ',M)
		#print('B ',B)
		print('R ',R)
		#print('Y0 ',Y0)
		"""
		l = 200 #[cm]
		Pd, _, Pi = LKF.seg_lines(Y0,M,B,R,l)
		x1_d,y1_d,x2_d,y2_d = Pd
		#x1_c,y1_c,x2_c,y2_c = Pc
		x1_i,y1_i,x2_i,y2_i = Pi
		print(Pd)
		#print(Pc)
		print(Pi)
		"""
		#imagenH = np.zeros((300,300,3))
		#for x,y in list_px:	imagenR = cv2.circle(imagenH, (int(x), int(y)), 2, (0, 255, 0), -1)
		#imagenR =cv2.line(imagenR, (y2_d,x2_d),(y1_d,x1_d), (255,0,0), 2)
		#imagenR =cv2.line(imagenR, (y2_i,x2_i),(y1_i,x1_i), (0,0,255), 2)
		#imagenR =cv2.line(imagenR, (y2_c,x2_c),(y1_c,x1_c), (255,255,255), 2)


		#cv2.imshow('test',imagenR)
		#cv2.imshow('seg',imagenSeg)
		#cv2.imshow('homografia',imagenR)
		#cv2.waitKey(1)






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

