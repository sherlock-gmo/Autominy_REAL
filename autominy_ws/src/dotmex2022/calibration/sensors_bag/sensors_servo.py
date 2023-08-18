#! /usr/bin/env python
import time
import rospy
import random
import numpy as np
from autominy_msgs.msg import SteeringAngle, NormalizedSteeringCommand

path_data = '/home/ros/dotMEX_Autominy_REAL/autominy_ws/src/dotmex2022/calibration/sensors_bag/'
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
		self.Spub = rospy.Publisher('/actuators/steering_normalized',NormalizedSteeringCommand,queue_size=15)
#----------------------------------------------------------------------------------------------------------------
#																	S. Steering
	def callback_st(self,data2):
		self.st_sensor = data2.value
		steering_msg.value = (1.0/100.0)*random.randrange(-100,100,2)
		self.Spub.publish(steering_msg)

		# Guardado de datos
		N = 5
		t = time.time()
		f = open(path_data+'sensors_servo_'+str(N)+'.csv','a+')
		f.write("%5.6f	%5.6f	%5.6f\n" %(t, steering_msg.value, self.st_sensor))
		f.close()

		#T = (1.0/1000.0)*random.randrange(10,200,10)
		T = 0.1
		time.sleep(T)
#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************
#																PRINCIPAL
if __name__ == '__main__':
	print("Nodo inicializado: sensors_servo.py")
	rospy.init_node('sensors_servo',anonymous=True)
	autominy()
	rospy.spin()

