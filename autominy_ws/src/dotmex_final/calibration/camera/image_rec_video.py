#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 12:03:27 2022

@author: barov
"""

import rospy
import cv2 as cv
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import time

bridge = CvBridge()
path = '/home/ros/dotMEX_Autominy_REAL/autominy_ws/src/dotmex_final/calibration/camera_calibration/caps_1920_1080/'
x = 1
#======================================================
#					VIDEO CAPTURE
#======================================================
def captura(dato):
	global x
	nombre = 'imagen'+ str(x) +'.png'
	imag0 = bridge.imgmsg_to_cv2(dato, "bgr8")
	time.sleep(0.5)
	cv.imwrite(path+nombre,imag0)
	x = x+1

#====================================================================
#						PRINCIPAL
#====================================================================
if __name__ == '__main__':
    try:
        print ('*** Nodo Image_rec inicializado ***')
        rospy.init_node('Image_rec', anonymous=True)
        rospy.Subscriber('/sensors/camera/color/image_raw',Image, captura)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
