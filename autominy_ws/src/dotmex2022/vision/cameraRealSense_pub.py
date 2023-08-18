#!/usr/bin/env python
import rospy
import numpy as np
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image, CompressedImage

bridge = CvBridge()
#***************************** RGB *************************
cap_rgb = cv2.VideoCapture(4)
# 2 IR-der
# 4 RGB
cap_rgb.set(3,640)	# Resolution y
cap_rgb.set(4,480)	# Resolution x
cap_rgb.set(cv2.CAP_PROP_FPS,30)	# FPS

RGBc_msg = CompressedImage()
RGBc_msg.format = "jpeg"
"""
#***************************** IR *************************
cap_ir = cv2.VideoCapture(2)
cap_ir.set(3,640)	# Resolution y
cap_ir.set(4,480)	# Resolution x
cap_ir.set(cv2.CAP_PROP_FPS,30)	# FPS
IRc_msg = CompressedImage()
IRc_msg.format = "jpeg" 
"""
#======================================================
#					VIDEO CAPTURE
#======================================================
def video_cap():
	#***************************** RGB *************************
	_,imagen0 = cap_rgb.read()
	imagen0 = cv2.cvtColor(imagen0,cv2.COLOR_BGR2RGB)
	RGB_msg = bridge.cv2_to_imgmsg(imagen0,'bgr8')
	RGBc_msg.data = np.array(cv2.imencode('.jpg', imagen0)[1]).tostring()
	"""
	#***************************** IR *************************
	_,imagen1 = cap_ir.read()
	IR_msg = bridge.cv2_to_imgmsg(imagen1)
	IRc_msg.data = np.array(cv2.imencode('.jpg', imagen1)[1]).tostring()
	#**********************************************************
	"""
	RGB_pub.publish(RGB_msg)			#Publica el mensaje de imagen en Image_topic
	RGBc_pub.publish(RGBc_msg)			#Publica el mensaje de imagen en Image_topic
	#IR_pub.publish(IR_msg)			#Publica el mensaje de imagen en Image_topic
	#IRc_pub.publish(IRc_msg)			#Publica el mensaje de imagen en Image_topic

#====================================================================
#						PRINCIPAL
#====================================================================
if __name__ == '__main__':
    try:
			print('*** Nodo inicializado ***')
			rospy.init_node('cameraRealSense_pub', anonymous=False)				# Nombre del nodo
			RGB_pub = rospy.Publisher('/sensors/camera/color/image_raw', Image, queue_size=10)
			RGBc_pub = rospy.Publisher('/sensors/camera/color/image_raw/compressed', CompressedImage, queue_size=10)
			#IR_pub = rospy.Publisher('/sensors/camera/ir/image_raw', Image, queue_size=10)
			#IRc_pub = rospy.Publisher('/sensors/camera/ir/image_raw/compressed', CompressedImage, queue_size=10)
			while not rospy.is_shutdown():			# Ejecuta el bucle mientras no se presiona ctrl+C
				video_cap()
    except rospy.ROSInterruptException:
        pass
