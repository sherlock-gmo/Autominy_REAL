#! /usr/bin/env python
import cv2
import rospy
import numpy as np
from sensor_msgs.msg import Image, LaserScan
from cv_bridge import CvBridge
from autominy_msgs.msg import SpeedPWMCommand
from autominy_msgs.msg import NormalizedSteeringCommand

path_libs = '/home/ros/dotMEX_Autominy_REAL/autominy_ws/src/dotmex2022/scripts_test/simple_controllers/libs'
import sys
sys.path.insert(1, path_libs)
from lib_lanekeep_functions import tip, roi_zone, vec_create, line_detector

bridge = CvBridge()
speed_msg = SpeedPWMCommand() #-1000 to 1000 pwm
steering_msg = NormalizedSteeringCommand() # -1.0 to 1.0
#speed_msg = SpeedPWMCommand() #-1000 to 1000 pwm
#steering_msg = SteeringCommand() # -0.498 to 0.512 rad



#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
class autominy(object):
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#																	INIT
#----------------------------------------------------------------------------------------------------------------
	def __init__(self):
		#V. Lidar
		self.step = 0
		self.R = np.zeros(360)
		self.Obj = False
		#V. Camera
		self.l = 60 # Tamano de la recta con que se modela el camino
		self.FT = 0
		self.side = -1 # 1=Derecha -1=Izquierda
		self.x_ref = 88 #120# 88
		self.x1_h = 88
		self.v = 250
		rospy.Subscriber("/sensors/camera/color/image_raw",Image,self.callback_V)
		rospy.Subscriber('/sensors/rplidar/scan', LaserScan, self.callback_Lidar)
		self.Vpub = rospy.Publisher('/actuators/speed_pwm',SpeedPWMCommand,queue_size=15)
		self.Spub = rospy.Publisher('/actuators/steering_normalized',NormalizedSteeringCommand,queue_size=15)
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#																	CALLBACKS
#----------------------------------------------------------------------------------------------------------------
#																	LIDAR
	def callback_Lidar(self, data_lidar):
		rmax = 3.0 # Distancia maxima de deteccion
		i = 0
		for r in data_lidar.ranges:
			if (r>=rmax): r = rmax
			if (i>=162) and (i<=164): r = rmax
			if (i>=206) and (i<=208): r = rmax
			self.R[i] = r
			i = i+1
		#print(np.argmin(data_lidar.ranges))
		R0_i = R[0:10]
		R0_d = R[359:349]
		R0 = np.concatenate((R0_i,R0_d),axis=None)
		r0 = np.min(R0)
		if (r0<=0.6): self.Obj = True
		else: self.Obj = False

#----------------------------------------------------------------------------------------------------------------
#																	CAMERA RGB
	def callback_V(self,data0):
		#____________________________Procesamiento de la imagen	
		imagen0 = bridge.imgmsg_to_cv2(data0, "bgr8") 	# Imagen cv2
		# Crea la mascara del color segmentado (anaranjado)
		lower = np.array([0,145,141])
		upper = np.array([10,255,255])
		imagenS = cv2.inRange(cv2.cvtColor(imagen0,cv2.COLOR_BGR2HSV),lower,upper)
		imagenS = cv2.medianBlur(imagenS,1)	
		imagenF = tip(imagenS) 	# TIP
		self.lane_keeping(imagenF)
#----------------------------------------------------------------------------------------------------------------
#																	CONTROLLERS
#----------------------------------------------------------------------------------------------------------------
	def lane_keeping(self,imagenF):
		if (self.Obj==True): speed_msg.value = 0
		else: speed_msg.value = self.v
		y1 = 0
		y2 = 0
		#print('--------SEGUIMIENTO DEL CARRIL-----------')
		#________________________________________Busca la linea
		if (self.FT<=10):
			x1 = 150 
			self.FT = self.FT+1
		else: x1 = self.x1_h
		# self.side = 1, DERECHA // self.side = -1, IZQUIERDA
		x1,y1,x2,y2 = line_detector(imagenF,x1,self.l,self.side)
		x1_h = x1
		x2_h = x2
		#________________________________________Ley de Control	
		Ky = 0.1656
		Kth = 0.6048
		e_y = x1-self.x_ref
		e_th = np.arctan2(x2-x1,self.l) #En radianes
		steering_msg.value = np.arctan(-Ky*e_y-Kth*e_th)*(2.0/np.pi) #Normalizado
		print('steering ',steering_msg.value)
		"""
	 	#Visualizacion
		#namedWindow("homografia");
		imagenS = cv2.cvtColor(imagenF,cv2.COLOR_GRAY2BGR)
		imagenS = cv2.circle(imagenS,(x1,y1),3,(0, 0, 255),-1)
		imagenS = cv2.circle(imagenS,(x2,y2),3,(0, 0, 255),-1)
		imagenS = cv2.line(imagenS, (x1,y1), (x2,y2), (0, 0, 255), 2) 
		cv2.imshow('homografia',imagenS)	
		cv2.moveWindow("homografia", 400,20)
		cv2.waitKey(1)	
		"""
		self.Vpub.publish(speed_msg) 
		self.Spub.publish(steering_msg)

#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************
#																PRINCIPAL
if __name__ == '__main__':
	print("Nodo inicializado: simple_passing_01.py")
	rospy.init_node('simple_passing_01',anonymous=True)
	autominy()
	rospy.spin()

