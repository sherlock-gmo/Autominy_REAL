#!/usr/bin/env python
import rospy
import time
import cv2
import numpy as np
from geometry_msgs.msg import Pose2D

pose_msg = Pose2D()

cap = cv2.VideoCapture(1) #1
cap.set(3,1280)	# Resolution y
cap.set(4,720)	# Resolution x
cap.set(cv2.CAP_PROP_FPS,30)	# FPS

H = np.array([[ 2.34695419e-01, -1.32684008e-01, -6.51538676e+01], [ 3.44425305e-03,  2.11796937e-01, -5.43928720e+00], [-4.85568704e-05, -1.12204468e-03,  1.00000000e+00]])
K = np.array([[625.70905563,0.0,714.99743504],[0.0,623.30278949,397.75606526],[0.0,0.0,1.0]])
dist_coef = np.array([[-3.34720632e-01,1.18125580e-01,4.17257777e-04,-1.61458599e-04,-1.85794482e-02]])
# Green
lower_g = np.array([60,50,50])
upper_g = np.array([80,255,255])
# Orange
lower_o = np.array([60,50,50])
upper_o = np.array([80,255,255])
path = '/home/sherlock/cinvespuma_ws/src/gps_vis/scripts/'

#**********************************************************************************
#**********************************************************************************
#**********************************************************************************
def video_cap():
	# Procesamiento de la imagen
	_,imagen0 = cap.read()	
	h,w = imagen0.shape[:2]
	f = 1.19
	w = int(w*f)
	h = int(h*f)
	mapx,mapy = cv2.initUndistortRectifyMap(K,dist_coef,None,None,(w,h),5)
	imagenF = cv2.remap(imagen0,mapx,mapy,cv2.INTER_LINEAR)
	imagenF = cv2.warpPerspective(imagenF, H, (300,300),borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0)) 
	imagenF_g = cv2.inRange(cv2.cvtColor(imagenF,cv2.COLOR_BGR2HSV),lower_g,upper_g) 
	imagenF_o = cv2.inRange(cv2.cvtColor(imagenF,cv2.COLOR_BGR2HSV),lower_o,upper_o) 
	#imagenF = cv2.medianBlur(imagenF,3)
	
	# Calculo de la posicion
	M_g = cv2.moments(imagenF_g)
	M_o = cv2.moments(imagenF_o)
	#print(M_g["m00"])
	#print(M_m["m00"])
	if (M_g["m00"]>=17000) and (M_m["m00"]>=17000):
		cX_g = int(M_g["m10"]/M_g["m00"])
		cY_g = int(M_g["m01"]/M_g["m00"])
		cX_o = int(M_o["m10"]/M_o["m00"])
		cY_o = int(M_o["m01"]/M_o["m00"])
		#t = time.time()
		pose_msg.x = cX_g
		pose_msg.y = cY_g
		pose_msg.theta = np.arctan2(cY_g-cY_o,cX_g-cX_o)*(np.pi/180.0)
		GPS_pub.publish(pose_msg)

		"""
		# Guarda los datos
		f = open(path+'prueba_pose02.csv','a+')
		f.write("%5.2f	%5.2f	%5.2f\n" %(t, cX, cY))
		f.close()
		"""

 	#Visualizacion
	imagenF = cv2.circle(imagenF, (cX,cY), 3, (0,0,255),-1)
	cv2.imshow('homografia',imagenF)	
	cv2.moveWindow("homografia", 400,20)
	cv2.waitKey(1)

#**********************************************************************************
#**********************************************************************************
#**********************************************************************************
if __name__ == '__main__':
    try:
			print("*** Nodo inicializado, GPS_pose ***")
			rospy.init_node('gps_pose', anonymous=True)	
			GPS_pub = rospy.Publisher('pose_car', Pose2D, queue_size=8) 	
			while not rospy.is_shutdown():	
				video_cap()
    except rospy.ROSInterruptException:
        pass
