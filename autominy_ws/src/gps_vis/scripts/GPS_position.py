#!/usr/bin/env python
import rospy
import time
import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(3,640)	# Resolution y
cap.set(4,480)	# Resolution x
cap.set(cv2.CAP_PROP_FPS,30)	# FPS

H = np.array([[7.65938814e-01,-3.86885980e-02,-3.96679539e+01], [2.66939449e-02,6.52405542e-01,-7.08676541], [-8.70156474e-05,9.51535501e-05,1.0]])
K = np.array([[319.71415651,0.0,344.96615854],[0.0,317.26216773,261.53024149],[0.0,0.0,1.0]])
dist_coef = np.array([[-0.3466721,0.14940472,-0.00101803,0.00506543,-0.03453036]])
lower = np.array([40,100,100])
upper = np.array([65,255,255])
path = '/home/sherlock/dotMEX_Autominy_REAL/autominy_ws/src/gps_vis/scripts/'

#**********************************************************************************
#**********************************************************************************
#**********************************************************************************
def video_cap():
	# Procesamiento de la imagen
	_,imagen0 = cap.read()	
	h,w = imagen0.shape[:2]
	w = int(w*1.0)
	h = int(h*1.45)
	mapx,mapy = cv2.initUndistortRectifyMap(K,dist_coef,None,None,(w,h),5)
	imagenF = cv2.remap(imagen0,mapx,mapy,cv2.INTER_LINEAR)
	imagenF = cv2.warpPerspective(imagenF, H, (370,395),borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0)) 
	imagenF = cv2.inRange(cv2.cvtColor(imagenF,cv2.COLOR_BGR2HSV),lower,upper)
	#imagenF = cv2.medianBlur(imagenF,1)
	
	# Calculo de la posicion
	M = cv2.moments(imagenF)
	#print(M["m00"])
	if (M["m00"]>=20000):
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])
		t = time.time()
				
		# Guarda los datos
		f = open(path+'position_v175.csv','a+')
		f.write("%5.2f	%5.2f	%5.2f\n" %(t, cX, cY))
		f.close()
		

 	#Visualizacion
	cv2.imshow('homografia',imagenF)	
	cv2.moveWindow("homografia", 400,20)
	cv2.waitKey(1)

#**********************************************************************************
#**********************************************************************************
#**********************************************************************************
if __name__ == '__main__':
    try:
			print "*** Nodo inicializado, GPS_vis ***"
			rospy.init_node('gps_vis', anonymous=True)	
			while not rospy.is_shutdown():	
				video_cap()
    except rospy.ROSInterruptException:
        pass
