#! /usr/bin/env python
import time
import rospy
import random
import numpy as np
from autominy_msgs.msg import SteeringAngle, NormalizedSteeringCommand

path_data = '/home/ros/dotMEX_Autominy_REAL/autominy_ws/src/dotmex_final/calibration/servo_motor/'
steering_msg = NormalizedSteeringCommand() # -1.0 to 1.0

#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
class autominy(object):
#----------------------------------------------------------------------------------------------------------------
#																	INIT
#----------------------------------------------------------------------------------------------------------------
	def __init__(self):
		rospy.Subscriber("/sensors/steering",SteeringAngle, self.callback_st)
		self.t0 = time.time()
		self.Spub = rospy.Publisher('/actuators/steering_normalized',NormalizedSteeringCommand,queue_size=15)
#----------------------------------------------------------------------------------------------------------------
#																	S. Steering
	def callback_st(self,data2):
		self.st_sensor = data2.value

		t = time.time()
		Dt = t-self.t0
		if (Dt<=5.0): 
			steering_msg.value = -1.0
		if (5.0<Dt<=10.0):
			steering_msg.value = 1.0
		if (Dt>10.0):
			steering_msg.value = -1.0



		self.Spub.publish(steering_msg)

		# Guardado de datos
		N = 3
		f = open(path_data+'sensors_servo_'+str(N)+'.csv','a+')
		f.write("%5.6f	%5.6f	%5.6f\n" %(Dt, steering_msg.value, self.st_sensor))
		f.close()

		#T = 0.1
		#time.sleep(T)
#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************
#																PRINCIPAL
if __name__ == '__main__':
	print("Nodo inicializado: sensors_servo.py")
	rospy.init_node('sensors_servo',anonymous=True)
	autominy()
	rospy.spin()


