#! /usr/bin/env python
import time
import rospy
import random
import numpy as np
from autominy_msgs.msg import SteeringAngle, NormalizedSteeringCommand

path_data = '/home/ros/Autominy_REAL/autominy_ws/src/dotmex_final/calibration/servomotor/'
steering_msg = NormalizedSteeringCommand() # -1.0 to 1.0

#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
class autominy(object):
#----------------------------------------------------------------------------------------------------------------
#																	INIT
#----------------------------------------------------------------------------------------------------------------
	def __init__(self):
		self.z10 = 0.0
		self.z20 = 0.0
		self.w = 2.5							# Escala de tiempo del oscilador en [rad/s]
		#self.h = 1.0/30.0					
		self.t0 = time.time()
		self.tk = self.t0
		rospy.Subscriber("/sensors/steering",SteeringAngle, self.callback_st)
		self.Spub = rospy.Publisher('/actuators/steering_normalized',NormalizedSteeringCommand,queue_size=15)
#----------------------------------------------------------------------------------------------------------------
#																	Duffin Oscilator
	def f_duffin(self,T,z10,z20,w,h):
		z1 = z10+h*w*z20
		z2 = z20+h*(w*z1-0.025*z20-0.75*w*(z1**3)+0.3*np.sin(w*T))
		s = (3.33/5.89)*z1
		return s, z1, z2
#----------------------------------------------------------------------------------------------------------------
#																	S. Steering
	def callback_st(self,data0):
		self.st_sensor = data0.value
		tk1 = time.time()
		h = tk1-self.tk			# Periodo de muestreo en [s]
		T = tk1-self.t0			# Tiempo transcurrido en [s]
		s,z1,z2 = self.f_duffin(T,self.z10,self.z20,self.w,h)	# Oscilador de duffin como excitacion persistente
		# Publicacion del mensaje
		steering_msg.value = s
		self.Spub.publish(steering_msg)
		# Guardado de datos
		N = 1
		f = open(path_data+'servo_bag'+str(N)+'.csv','a+')
		f.write("%5.6f	%5.6f	%5.6f	%5.6f\n" %(T, h, steering_msg.value, self.st_sensor))
		f.close()
		# Actualizacion
		self.tk = tk1
		self.z10 = z1
		self.z20 = z2
#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************
#																PRINCIPAL
if __name__ == '__main__':
	print("Nodo inicializado: servo_bag.py")
	rospy.init_node('servo_bag',anonymous=True)
	autominy()
	rospy.spin()


