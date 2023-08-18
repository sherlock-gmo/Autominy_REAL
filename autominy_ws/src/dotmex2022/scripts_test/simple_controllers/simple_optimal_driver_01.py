#! /usr/bin/env python
import cv2
import rospy
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from autominy_msgs.msg import SpeedPWMCommand
from autominy_msgs.msg import SteeringCommand

bridge = CvBridge()
speed_msg = SpeedPWMCommand() #-1000 to 1000 pwm
steering_msg = SteeringCommand() # -0.498 to 0.512 rad

# V. globales de la vision
s = 100
l = 60 # Tamano de la recta con que se modela el camino
FT = 0
side_line = False # True=Derecha False=Izquierda
x_ref = 89
x1 = 89
x2 = 89
x1_h = 89
x2_h = 89
th_line = 0.0

# V. globales del control
u = 90
v = 50 
speed_msg.value = v

#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************
#  		               TIP
def tip(imagenN):
	# Matriz H
	H=np.array([[-3.70328855e-01, -1.65601076,2.32836764e+02],[1.00431211e-03, -5.45716507, 5.72661483e+02],[-1.76527831e-05, -1.62771589e-02, 1.0]]) 
	# Obtenemos la imagen con correccion de pespectiva
	imagenH = cv2.warpPerspective(imagenN, H, (200,300),borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0)) 
	return imagenH
#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************
def roi_zone(x):
	assert (x>=0) and (x<=199), 'x out of limits'
	if (x>120) and (x<=199):
		y = int(round(-2.3418*x+580.0160))
	if (x>=81) and (x<=120):
		y = 299
	if (x>=0) and (x<81):
		y = int(round(1.7778*x+154.9982))
	return y
#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************
def vec_create(x,stride):
	j = 0
	xv = []
	for i in range(0,2*stride+1):
		if ((-1)**i==-1): j = j+1
		xv.append(x+j*(-1)**i)
	return xv
#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************
def line_detector(imagen0,x1,l,side):
	# Busca x1r
	K = True
	stride = 5
	y1 = roi_zone(x1)
	x1v = vec_create(x1,stride)
	while (K==True):
		if (y1+6>299): m = 299-y1
		else: m = stride
		for j in range(y1+m,y1-stride,-1):
			for i in x1v:
				if imagen0[j][i]==255:
					x1 = i
					y1 = j
					K = False
					break
			x1v = vec_create(x1,stride)
			if (K==False): break
		if (K==True): # Insiste en la busqueda
			x1 = x1-1*side
			y1 = roi_zone(x1)

	# Busca x2 a una altura de l cm o menos
	x2 = x1
	y2 = roi_zone(x2)
	x2v = vec_create(x2,stride)
	for j in range(y1-1,y1-l,-1):
		for i in x2v:
			if imagen0[j][i]==255:
				x2 = i
				y2 = j
				K = False
				break
		x2v = vec_create(x2,stride)			
	return x1,y1,x2,y2
#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************
#							CONTROL DEL STEERING
def callback_V(data0):
	global u
	global FT, side_line, x_ref, s
	global x1, x2, x1_h, x2_h
	global th_line

	#____________________________Procesamiento de la imagen	
	imagen0 = bridge.imgmsg_to_cv2(data0, "bgr8") 	# Imagen cv2
	# Crea la mascara del color segmentado (rosa)
	lower = np.array([140,100,100])
	upper = np.array([180,255,255])
	imagenS = cv2.inRange(cv2.cvtColor(imagen0,cv2.COLOR_BGR2HSV),lower,upper)
	#seg = cv2.medianBlur(seg,2*K+1)	
	imagenF = tip(imagenS) 	# TIP

	y1 = 0
	y2 = 0

	#print('--------SEGUIMIENTO DEL CARRIL-----------')
	#________________________________________Busca la linea
	if (FT<=10):
		x1 = s 
		FT = FT+1
	else: x1 = x1_h
	side = 1 # Linea derecha
	x1,y1,x2,y2 = line_detector(imagenF,x1,l,side)
	x1_h = x1
	x2_h = x2
	#________________________________________Determina si sigue la linea derecha o izquierda
	if (x2-x1>=10) and (side_line==True): # and (x2-x2_h>0):#
		print('-----------------CHANGE_LEFT')
		#s = 100
		side_line = False
		x_ref = 89
		FT = 0
	if (x1-x2>10) and (side_line==False):# and (x2-x2_h<0) 
		print('-----------------CHANGE_RIGHT')
		#s = 180
		side_line = True
		x_ref = 121
		FT = 0

	#________________________________________Ley de Control	
	ex = x1-x_ref
	if (x_ref==121):
		kx = -0.04140024959995424
		kth = -0.1512095718256754
	if (x_ref==89):
		kx = -0.025
		kth = -0.15
	# Metodo 1
	#th = np.arctan2(x2-x1,l) #En radianes

	# Metodo 2
	Lh = 0.5 # En metros
	gamma = np.arctan2(x2-x1,l) #En radianes
	num_th = x2-x_ref*np.cos(gamma)
	den_th = Lh+l-x_ref*np.sin(gamma)
	th = np.arctan2(num_th,den_th)

	steering_msg.value = np.arctan(kx*ex+kth*th) #En grados
	print('steering ',steering_msg.value)
	"""
 	#Visualizacion
	#namedWindow("homografia");
	imagenS = cv2.cvtColor(imagenF,cv2.COLOR_GRAY2BGR)
	imagenS = cv2.circle(imagenS,(x1,y1),3,(0, 0, 255),-1)
	imagenS = cv2.circle(imagenS,(x2,y2),3,(0, 0, 255),-1)
	imagenS = cv2.line(imagenS, (x1,y1), (x2,y2), (0, 0, 255), 2) 
	cv2.imshow('homografia',imagenS)	
	cv2.moveWindow("homografia", 400,20)
	cv2.waitKey(1)	
	"""
	Vpub.publish(speed_msg) 
	Spub.publish(steering_msg)

#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************
#																PRINCIPAL
if __name__ == '__main__':
	print("Nodo inicializado: simple_optimal_driver_01.py")
	rospy.init_node('simple_optimal_driver_01',anonymous=True)												
	Vpub = rospy.Publisher('/actuators/speed_pwm',SpeedPWMCommand,queue_size=15)				 
	Spub = rospy.Publisher('/actuators/steering',SteeringCommand,queue_size=15)
	rospy.Subscriber("/sensors/camera/color/image_raw",Image,callback_V)	 						
	rospy.spin()
#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************
