#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

# V.globales
br  = CvBridge()
flag = True
H = 179
S = 255
V = 255
h = 0
s = 0
v = 0
K = 0
#**********************************************************
def nothing(x):
	pass
#**********************************************************
#								INTERFAZ GRAFICA
#**********************************************************
def interfaz():
	global flag
	if (flag==True):
		# Crea las barras de desplazamiento
		cv2.createTrackbar('H','segmentacion',0,179,nothing)
		cv2.createTrackbar('S','segmentacion',0,255,nothing)
		cv2.createTrackbar('V','segmentacion',0,255,nothing)
		cv2.createTrackbar('h','segmentacion',0,179,nothing)
		cv2.createTrackbar('s','segmentacion',0,255,nothing)
		cv2.createTrackbar('v','segmentacion',0,255,nothing)
		cv2.createTrackbar('K','segmentacion',0,10,nothing)
		# Posicion inicial de las barras
		cv2.setTrackbarPos('H','segmentacion',179)
		cv2.setTrackbarPos('S','segmentacion',255)
		cv2.setTrackbarPos('V','segmentacion',255)
		cv2.setTrackbarPos('h','segmentacion',0)
		cv2.setTrackbarPos('s','segmentacion',0)
		cv2.setTrackbarPos('v','segmentacion',0)
		cv2.setTrackbarPos('K','segmentacion',0)
		flag = False
	else: pass
#**********************************************************
#							SEGMENTACAO
#**********************************************************
def img_callback(data):
	global flag
	global H,S,V,h,s,v,K
	# Adquiere la imagen original
	imagen0 = br.imgmsg_to_cv2(data,'bgr8')
	imagen0 = cv2.resize(imagen0,(320,240),cv2.INTER_LINEAR)
	cv2.imshow('original',imagen0)
	# Crea la mascara del color segmentado
	upper = np.array([H,S,V])
	lower = np.array([h,s,v])
	imagenHSV = cv2.cvtColor(imagen0,cv2.COLOR_BGR2HSV)
	imagenSeg = cv2.inRange(imagenHSV,lower,upper)
	imagenSeg = cv2.medianBlur(imagenSeg,2*K+1)
	cv2.imshow('segmentacion',imagenSeg)
	interfaz()
	# Actualiza los valores de las variables
	H = cv2.getTrackbarPos('H','segmentacion')
	S = cv2.getTrackbarPos('S','segmentacion')
	V = cv2.getTrackbarPos('V','segmentacion')
	h = cv2.getTrackbarPos('h','segmentacion')
	s = cv2.getTrackbarPos('s','segmentacion')
	v = cv2.getTrackbarPos('v','segmentacion')
	K = cv2.getTrackbarPos('K','segmentacion')
	cv2.waitKey(1)
#***********************************************************
#						PRINCIPAL
#***********************************************************
def main():
	rospy.init_node('segmentacao',anonymous=True)
	rospy.Subscriber('/sensors/camera/color/image_raw',Image,img_callback)
	rospy.spin()
if __name__ == '__main__':
	main()





