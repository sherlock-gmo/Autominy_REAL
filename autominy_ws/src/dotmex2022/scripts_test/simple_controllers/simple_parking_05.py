#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import LaserScan
from bno055_usb_stick_msgs.msg import Output
from std_msgs.msg import Bool
from autominy_msgs.msg import SpeedPWMCommand, NormalizedSteeringCommand

import time

path_libs = '/home/ros/dotMEX_Autominy_REAL/autominy_ws/src/dotmex2022/scripts_test/simple_controllers/libs'
import sys
sys.path.insert(1, path_libs)
from lib_parking_functions import steer_control, fit_ransac
from lib_lidar_functions import lidar_roi, lidar_left

speed_msg = SpeedPWMCommand() #-1000 to 1000 pwm
steering_msg = NormalizedSteeringCommand() # -1.0 to 1.0

#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
class sensors_processing(object):
#----------------------------------------------------------------------------------------------------------------
#																	INIT
#----------------------------------------------------------------------------------------------------------------
	def __init__(self):
		# V. IMU
		self.FTY = True
		self.yaw0 = 0.0
		self.Dyaw = 0.0
		self.D = 32.0 #34.0
		#V. Lidar
		self.step = 0
		self.R = np.zeros(360)
		#V. Parking
		self.Pflag = False
		rospy.Subscriber('/sensors/rplidar/scan', LaserScan, self.callback_Lidar)
		rospy.Subscriber('/sensors/bno055/output', Output, self.callback_Imu)
		self.Vpub = rospy.Publisher('/actuators/speed_pwm',SpeedPWMCommand,queue_size=15)
		self.Spub = rospy.Publisher('/actuators/steering_normalized',NormalizedSteeringCommand,queue_size=15)
#----------------------------------------------------------------------------------------------------------------
#																	CALLBACKS
#----------------------------------------------------------------------------------------------------------------
#																	LIDAR
	def callback_Lidar(self, data_lidar):
		rmax = 3.0 # Distancia maxima de deteccion
		i = 0
		for r in data_lidar.ranges:
			if (r>=rmax): r = rmax
			if (i>=160) and (i<=162): r = rmax
			if (i>=199) and (i<=202): r = rmax
			self.R[i] = r
			i = i+1
		#print(np.argmin(data_lidar.ranges))
#----------------------------------------------------------------------------------------------------------------
#																	IMU
	def callback_Imu(self, data_imu):
		#D = 34.0 #34.0
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
		self.maneuver()

	def delay_time(self):
		v = 0
		speed_msg.value = v
		self.Vpub.publish(speed_msg)
		time.sleep(0.1)
#----------------------------------------------------------------------------------------------------------------
#																	CONTROLLERS
#----------------------------------------------------------------------------------------------------------------
	def maneuver(self):
		if np.all((self.R == 0)): pass
		#_______________________________________________________________________________________
		else:
			#print('-----------ESTACIONAMIENTO-----------')
			Nv = 180 #215
			R0_i = self.R[0:14]
			R0_d = self.R[344:359]
			R0 = np.concatenate((R0_i,R0_d))
			r0 = np.amin(R0)
			r180 = np.amin(self.R[165:205])
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
				v = -Nv*0.85
				if (self.Dyaw<=-self.D): self.step = self.step + 1
			
			if (self.step == 2):
				u = -1.0
				v = -Nv*0.85
				if (self.Dyaw>=0.0) or (r180<=0.38): #0.35
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
			print('Dyaw ',self.Dyaw)
			print('step ',self.step)
			#print('u ',u)
			#print('v ',v)
			print('****************************')
			speed_msg.value = v
			steering_msg.value = u
			self.Vpub.publish(speed_msg)
			self.Spub.publish(steering_msg)
#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
if __name__ == '__main__':
	print("Nodo inicializado: simple_parking_01.py")
	rospy.init_node('simple_parking_01',anonymous=True)
	sensors_processing()
	rospy.spin()








