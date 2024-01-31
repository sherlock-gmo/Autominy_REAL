#! /usr/bin/env python
import cv2
import rospy
import numpy as np
from darknet_ros_msgs.msg import BoundingBoxes

path_libs = '/home/dotmex/dotMEX_Autominy_REAL/autominy_ws/src/tmr2023/scripts/libs'
#path_libs ='/home/ros/dotMEX_Autominy_REAL/autominy_ws/src/tmr2023/scripts/libs'
import sys
sys.path.insert(1, path_libs)
from lib_yolo_functions import yolo_roi

#################################################################################################################
#################################################################################################################
#################################################################################################################
class autominy(object):
#----------------------------------------------------------------------------------------------------------------
#									INIT
#----------------------------------------------------------------------------------------------------------------
	def __init__(self):
		rospy.Subscriber("/darknet_ros/bounding_boxes",BoundingBoxes,self.callback_Yolo)
#----------------------------------------------------------------------------------------------------------------
#																	YOLO
	def callback_Yolo(self,data_yolo):
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
			#if (id_number == 13) and (area>=2000): self.v_max = 185		# lim 50km_h
			#if (id_number == 14) and (area>=2000): self.v_max = 235		# lim 100km_h
			if (id_number == 8) and (area>=1700): print('¡¡¡Alto!!!')			# Alto*** 
			# v=225 => area = 2000
			# v=235 => area = xxx
			#if (id_number == 9) and (area>=2450): self.NoEst = True	# No estacionarse
			#if (id_number == 0) and (area>=6000) and (175<=cx<=475) and (p>=0.65): print('¡¡¡carro!!!')		# Carro***
			
			if (id_number == 4): # Peaton***
				C = [60,350,251,125,420,120,585,350]
				p = yolo_roi(C, cx, cy)
				if (area>=1500) and (p==True): 
					print('*************************************')
					print('¡¡¡Peaton!!! ')	# Peaton***
					print('*************************************')

			if (id_number == 0): # Carro***
				C = [150,340,270,140,385,140,510,340]
				k = yolo_roi(C, cx, cy)
				if (area>=6500) and (k==True): 
					print('*************************************')
					print('¡¡¡Carro!!! ')	# Carro***
					print('*************************************')
					
			if (id_number == 0):
				print('cx ',cx)
				print('cy ',cy)
				print('area ',area)
				print('p ',p)

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
#################################################################################################################
#################################################################################################################
#################################################################################################################
#								MAIN
if __name__ == '__main__':
	print("Nodo inicializado: YOLO_cal.py")
	rospy.init_node('YOLO_cal',anonymous=True)
	autominy()
	rospy.spin()

