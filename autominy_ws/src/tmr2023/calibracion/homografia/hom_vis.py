#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

br  = CvBridge()
#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************
#  		               TIP
def tip(imagenN):
	H=np.array([[-4.51935893e-01,-1.59213448,2.29943094e+02],[-1.49372457e-01,-5.42175253,6.00556357e+02],[-4.31688088e-04,-1.60028341e-02,1.0]])
	imagenH = cv2.warpPerspective(imagenN, H, (200,300),borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0))
	return imagenH
#**********************************************************
#**********************************************************
#**********************************************************
def img_callback(data):
	imagen0 = br.imgmsg_to_cv2(data,'bgr8')
	# Color anaranjado en RGB
	lower = np.array([100,95,125])	#RGB: 100,95,125 # BGR: 0,45,146
	upper = np.array([140,255,255])	#RGB:140,255,255 # BGR: 11,255,255
	imagenS = cv2.inRange(cv2.cvtColor(imagen0,cv2.COLOR_BGR2HSV),lower,upper)
	imagenS = cv2.medianBlur(imagenS,1)
	imagenF = tip(imagenS) 	# TIP
	#imagenC = tip(imagen0) 	# TIP
	
	#cv2.imshow('homografia_color',imagenC)	
	cv2.imshow('homografia_seg',imagenF)	
	cv2.waitKey(1)
#***********************************************************
#						PRINCIPAL
#***********************************************************
def main():
	rospy.init_node('hom_vis',anonymous=True)
	rospy.Subscriber('/sensors/camera/color/image_raw',Image,img_callback)
	rospy.spin()
if __name__ == '__main__':
	main()
