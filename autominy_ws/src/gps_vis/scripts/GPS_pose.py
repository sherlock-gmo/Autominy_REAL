#!/usr/bin/env python
import rospy
import time
import cv2
import numpy as np
from geometry_msgs.msg import Pose2D

pose_msg = Pose2D()

cap = cv2.VideoCapture(0) #1
cap.set(3,640)	# Resolution y
cap.set(4,480)	# Resolution x
cap.set(cv2.CAP_PROP_SATURATION,-0.75)	# Saturacion
cap.set(cv2.CAP_PROP_FPS,30)	# FPS

H = np.array([[6.30238413e-01,-1.52026387e-01,2.11429691e+01],[9.07304807e-02,6.53824267e-01,-2.65866923e+01],[-1.94007022e-04,-2.92863954e-05,1.0]])
K = np.array([[319.71415651,0.0,344.96615854], [0.0,317.26216773,261.53024149], [0.0,0.0,1.0]])
dist_coef = np.array([[-0.3466721 ,  0.14940472, -0.00101803,  0.00506543, -0.03453036]])
# Cian
lower_1 = np.array([70,190,90])
upper_1 = np.array([90,255,255])
# Magenta
lower_2 = np.array([115,165,100])
upper_2 = np.array([179,255,255])

Ker = 1
#path = '/home/sherlock1804/Autominy_REAL/autominy_ws/src/gps_vis/scripts/'
path = '/home/dotmex/Autominy_REAL/autominy_ws/src/gps_vis/scripts/'
#**********************************************************************************
#**********************************************************************************
#**********************************************************************************
def video_cap():
	# Procesamiento de la imagen
	_,imagen0 = cap.read()	
	h,w = imagen0.shape[:2]
	w = int(w*1.0)
	h = int(h*1.5)
	mapx,mapy = cv2.initUndistortRectifyMap(K,dist_coef,None,None,(w,h),5)
	imagenF = cv2.remap(imagen0,mapx,mapy,cv2.INTER_LINEAR)
	imagenF = cv2.warpPerspective(imagenF, H, (375,430),borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0)) 
	imagenF_1 = cv2.inRange(cv2.cvtColor(imagenF,cv2.COLOR_BGR2HSV),lower_1,upper_1) 
	imagenF_2 = cv2.inRange(cv2.cvtColor(imagenF,cv2.COLOR_BGR2HSV),lower_2,upper_2) 
	imagenF_1 = cv2.medianBlur(imagenF_1,2*Ker+1)
	imagenF_2 = cv2.medianBlur(imagenF_2,2*Ker+1)
	
	# Calculo de la posicion
	M_1 = cv2.moments(imagenF_1)
	M_2 = cv2.moments(imagenF_2)
	#print(M_1["m00"])
	#print(M_2["m00"])
	if (M_1["m00"]>=17000) and (M_2["m00"]>=17000):
		cX_1 = int(M_1["m10"]/M_1["m00"])
		cY_1 = int(M_1["m01"]/M_1["m00"])
		cX_2 = int(M_2["m10"]/M_2["m00"])
		cY_2 = int(M_2["m01"]/M_2["m00"])
		t = time.time()
		pose_msg.x = cX_2
		pose_msg.y = cY_2
		pose_msg.theta = np.arctan2(cY_1-cY_2,cX_1-cX_2) # En radianes
		GPS_pub.publish(pose_msg)
	else:
		cX_1 = 0
		cY_1 = 0
		cX_2 = 0
		cY_2 = 0

	# Guarda los datos
	t = time.time()
	f = open(path+'pose_ev_275_11.csv','a+')
	f.write("%5.6f	%5.6f	%5.6f	%5.6f\n" %(t, pose_msg.x, pose_msg.y, pose_msg.theta))
	f.close()
	"""
 	#Visualizacion
	imagenF = cv2.circle(imagenF, (cX_1,cY_1), 3, (255,0,255),-1)
	imagenF = cv2.circle(imagenF, (cX_2,cY_2), 3, (255,0,0),-1)
	cv2.imshow('homografia',imagenF)	
	#cv2.moveWindow("homografia", 400,20)
	cv2.waitKey(1)
	"""
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
