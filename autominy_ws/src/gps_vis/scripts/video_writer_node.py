#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

br  = CvBridge()
i = 582
path='/home/dotmex/Autominy_REAL/autominy_ws/src/gps_vis/scripts/caps/'
#**********************************************************
#							SEGMENTACAO
#**********************************************************
def img_callback(data):
	global i
	# Adquiere la imagen original
	imagen0 = br.imgmsg_to_cv2(data,'rgb8')
	name = 'imagen_fish_eye_'+str(i)+'.jpg'
	#cv2.imshow('original',imagen0)
	cv2.imwrite(path+name, imagen0) 
	i = i+1

#***********************************************************
#						PRINCIPAL
#***********************************************************
def main():
	print('*****Capturando datos*****')
	rospy.init_node('video_writer_node',anonymous=True)
	rospy.Subscriber('/sensors/camera/color/image_raw',Image,img_callback)
	rospy.spin()
if __name__ == '__main__':
	main()





