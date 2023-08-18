#! /usr/bin/env python
import time
import rospy
import random
import numpy as np
from autominy_msgs.msg import Speed, SpeedPWMCommand

path_data = '/home/ros/dotMEX_Autominy_REAL/autominy_ws/src/dotmex2022/calibration/sensors_bag/'
speed_msg = SpeedPWMCommand() #-1000 to 1000 pwm

#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
class autominy(object):
#----------------------------------------------------------------------------------------------------------------
#																	INIT
#----------------------------------------------------------------------------------------------------------------
	def __init__(self):
		rospy.Subscriber("/sensors/speed",Speed,self.callback_sp)
		self.Vpub = rospy.Publisher('/actuators/speed_pwm',SpeedPWMCommand,queue_size=15)
#----------------------------------------------------------------------------------------------------------------
#																	S. Speed
	def callback_sp(self,data1):
		self.sp_sensor = data1.value
		speed_msg.value = random.randrange(0,1000,10)
		self.Vpub.publish(speed_msg)

		# Guardado de datos
		N = 5
		t = time.time()
		f = open(path_data+'sensors_bldc_'+str(N)+'.csv','a+')
		f.write("%5.6f	%5.6f	%5.6f\n" %(t, speed_msg.value, self.sp_sensor))
		f.close()

		#T = (1.0/1000.0)*random.randrange(10,200,10)
		T = 0.2
		time.sleep(T)
#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************
#																PRINCIPAL
if __name__ == '__main__':
	print("Nodo inicializado: sensors_bldc.py")
	rospy.init_node('sensors_bldc',anonymous=True)
	autominy()
	rospy.spin()

