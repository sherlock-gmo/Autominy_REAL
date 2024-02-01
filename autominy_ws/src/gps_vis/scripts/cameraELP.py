#!/usr/bin/env python
import rospy
import roslib
import numpy as np
import cv2 as cv
from cv_bridge import CvBridge
from sensor_msgs.msg import Image, CompressedImage

bridge = CvBridge()
cap = cv.VideoCapture(0)
cap.set(3,640)	# Resolution y
cap.set(4,480)	# Resolution x
cap.set(cv.CAP_PROP_FPS,30)	# FPS
#cap.set(cv.CAP_PROP_EXPOSURE,-3)	# Exposure, min -7, max -1, increment 1

# Resolucion y frecuencia del topico en ROS
#(320,240)		# max 90.0 Hz
#(640,480)		# max 51.5 Hz
#(1024,768)		# max 5.5 Hz
#(1280,720)		# 1Mpx max 18.0 Hz +++MAX+++
#(1920,1082)	# 2Mpx max 5.7 Hz
#(2560,1920)	# 5Mpx max 3.4 Hz
#(2592,1944)	# MAX max 2.9 Hz

imagenC_msg = CompressedImage()
imagenC_msg.format = "jpeg" 
#======================================================
#					VIDEO CAPTURE
#======================================================
def video_cap():
	_,imagen0 = cap.read()	    							  # Original
	imagen0_msg = bridge.cv2_to_imgmsg(imagen0,"bgr8") #,"bgr8"
	imagenC_msg.data = np.array(cv.imencode('.jpg', imagen0)[1]).tostring()
	Im_pub.publish(imagen0_msg)			#Publica el mensaje de imagen en Image_topic
	ImC_pub.publish(imagenC_msg)		#Publica el mensaje de imagen en Image_topic
	#rate.sleep()
#====================================================================
#						PRINCIPAL
#====================================================================
if __name__ == '__main__':
    try:
			print("*** Nodo inicializado ***")
			rospy.init_node('ELP_camera', anonymous=True)				# Nombre del nodo
			Im_pub = rospy.Publisher('/sensors/camera/gps_vis/image_raw', Image, queue_size=5)	
			ImC_pub = rospy.Publisher('/sensors/camera/gps_vis/image_raw/compressed', CompressedImage, queue_size=5)
			while not rospy.is_shutdown():			# Ejecuta el bucle mientras no se presiona ctrl+C
				video_cap()
    except rospy.ROSInterruptException:
        pass
