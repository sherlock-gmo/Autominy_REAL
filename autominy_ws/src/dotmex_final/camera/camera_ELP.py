#!/usr/bin/env python
import rospy
import numpy as np
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image, CompressedImage

#***************************IMPORTANTE**********************
# Algunas veces hay que verificar si la camara tiene permisos
# v4l2-ctl --list-devices	# Verifica si la camara tiene permisos
# sudo chmod 777 /dev/video0	# Le da permisos a la camara
#***********************************************************

bridge = CvBridge()
#***************************** RGB *************************
cap_rgb = cv2.VideoCapture(0)
cap_rgb.set(3,1920)	# Resolution y
cap_rgb.set(4,1080)	# Resolution x
cap_rgb.set(cv2.CAP_PROP_FPS,30)	# FPS

RGBc_msg = CompressedImage()
RGBc_msg.format = "jpeg"
#======================================================
#					VIDEO CAPTURE
#======================================================
def video_cap():
	#***************************** RGB *************************
	_,imagen0 = cap_rgb.read()
	if imagen0 is not None:
		imagen0 = cv2.resize(imagen0,(960,540),cv2.INTER_LINEAR)
		#imagen0 = cv2.cvtColor(imagen0,cv2.COLOR_BGR2RGB)
		RGB_msg = bridge.cv2_to_imgmsg(imagen0,'bgr8')
		RGBc_msg.data = np.array(cv2.imencode('.jpg', imagen0)[1]).tostring()
		RGB_pub.publish(RGB_msg)			#Publica el mensaje de imagen en Image_topic
		RGBc_pub.publish(RGBc_msg)			#Publica el mensaje de imagen en Image_topic
	else: print('La camara no tiene permisos !!!')
#====================================================================
#						PRINCIPAL
#====================================================================
if __name__ == '__main__':
    try:
			print('*** Nodo inicializado ***')
			rospy.init_node('cameraELP_pub', anonymous=False)				# Nombre del nodo
			RGB_pub = rospy.Publisher('/sensors/camera/color/image_raw', Image, queue_size=15)
			RGBc_pub = rospy.Publisher('/sensors/camera/color/image_raw/compressed', CompressedImage, queue_size=10)
			while not rospy.is_shutdown():			# Ejecuta el bucle mientras no se presiona ctrl+C
				video_cap()
    except rospy.ROSInterruptException:
        pass
