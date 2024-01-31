#! /usr/bin/env python
import cv2
import time
import rospy
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from autominy_msgs.msg import Speed, SteeringAngle
from autominy_msgs.msg import SpeedPWMCommand, NormalizedSteeringCommand

path_data = '/home/ros/dotMEX_Autominy_REAL/autominy_ws/src/tmr2023/calibracion/sensors_bag/'
path_libs = '/home/ros/dotMEX_Autominy_REAL/autominy_ws/src/tmr2023/scripts/libs'
import sys
sys.path.insert(1, path_libs)
from lib_lanekeep_functions import tip, roi_zone, vec_create, line_detector

bridge = CvBridge()
speed_msg = SpeedPWMCommand() #-1000 to 1000 pwm
steering_msg = NormalizedSteeringCommand() # -1.0 to 1.0

#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
class autominy(object):
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#																	INIT
#----------------------------------------------------------------------------------------------------------------
	def __init__(self):
		#V. Camera
		self.l = 60 # Tamano de la recta con que se modela el camino
		self.FT = 0
		self.side = 1 #-1 # 1=Derecha -1=Izquierda
		self.x_ref = 118 #88 #120
		self.x1_h = 118 #88 #120
		self.x_search = 180 #160
		self.v = 275
		# Sensors
		self.sp_sensor = 0.0
		self.st_sensor = 0.0
		#+++++++++++++++++++++++++++++++++++++++
		rospy.Subscriber("/sensors/camera/color/image_raw",Image,self.callback_V)
		rospy.Subscriber("/sensors/speed",SteeringAngle,self.callback_sp)
		rospy.Subscriber("/sensors/steering",Speed,self.callback_st)
		self.Vpub = rospy.Publisher('/actuators/speed_pwm',SpeedPWMCommand,queue_size=15)
		self.Spub = rospy.Publisher('/actuators/steering_normalized',NormalizedSteeringCommand,queue_size=15)
#----------------------------------------------------------------------------------------------------------------
#
#----------------------------------------------------------------------------------------------------------------
#																	CAMERA RGB
	def callback_V(self,data0):
		#____________________________Procesamiento de la imagen
		imagen0 = bridge.imgmsg_to_cv2(data0, "bgr8") 	# Imagen cv2
		# Crea la mascara del color segmentado (anaranjado)
		lower = np.array([100,95,125])
		upper = np.array([140,255,255])
		imagenS = cv2.inRange(cv2.cvtColor(imagen0,cv2.COLOR_BGR2HSV),lower,upper)
		imagenS = cv2.medianBlur(imagenS,1)
		imagenF = tip(imagenS) 	# TIP
		self.lane_keeping(imagenF)
#----------------------------------------------------------------------------------------------------------------
#
#----------------------------------------------------------------------------------------------------------------
#																	S. Speed
	def callback_sp(self,data1):
		self.sp_sensor = data1.value
#----------------------------------------------------------------------------------------------------------------
#
#----------------------------------------------------------------------------------------------------------------
#																	S. Steering
	def callback_st(self,data2):
		self.st_sensor = data2.value
#----------------------------------------------------------------------------------------------------------------
#																	CONTROLLERS
#----------------------------------------------------------------------------------------------------------------
	def lane_keeping(self,imagenF):
		self.side = 1
		self.x_ref = 118
		self.x_search = 180
		self.l = 90

		speed_msg.value = self.v
		y1 = 0
		y2 = 0
		#print('--------SEGUIMIENTO DEL CARRIL-----------')
		#________________________________________Busca la linea
		if (self.FT<=10):
			x1 = self.x_search
			self.FT = self.FT+1
		else: x1 = self.x1_h
		# self.side = 1, DERECHA // self.side = -1, IZQUIERDA
		x1,y1,x2,y2 = line_detector(imagenF,x1,self.l,self.side)
		self.x1_h = x1
		#________________________________________Ley de Control
		Ky = 0.45631688
		Kth = 0.5265962
		e_y = x1-self.x_ref
		e_th = np.arctan2(x2-x1,self.l) #En radianes
		steering_msg.value = np.arctan(-Ky*e_y-Kth*e_th)*(2.0/np.pi) #Normalizado
		self.Vpub.publish(speed_msg)
		self.Spub.publish(steering_msg)

		# Guardado de datos
		char = str(self.v)
		t = time.time()
		f = open(path_data+'sensors_bag_l90_01_'+char+'.csv','a+')
		f.write("%5.6f  %5.6f   %5.6f   %5.6f   %5.6f\n" %(t, speed_msg.value, self.sp_sensor, steering_msg.value, self.st_sensor))
		f.close()

#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************
#																PRINCIPAL
if __name__ == '__main__':
	print("Nodo inicializado: sensors_bag.py")
	rospy.init_node('sensors_bag',anonymous=True)
	autominy()
	rospy.spin()

