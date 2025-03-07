#! /usr/bin/env python
import cv2
import numpy as np

#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
class lidar_f():
#**********************************************************************************************************************************	
#**********************************************************************************************************************************
	def __init__(self):
		pass
#**********************************************************************************************************************************	
#**********************************************************************************************************************************
	def polar_roi(self,R):
		# Toma los puntos en forma polar y devuelve las distancias que hay entre el lidar 
		#	y un objeto enfrente/detras
		R0_i = R[0:29]
		R0_d = R[329:359]
		R0 = np.concatenate((R0_i,R0_d))
		r0 = np.amin(R0)
		r180 = np.amin(R[159:199]) #162,199 #np.amin(self.R[165:205])
		return r0, r180
#**********************************************************************************************************************************	
#**********************************************************************************************************************************
	def lidar4ransac_FT(self,R,ymax,ymin,side):
		# Toma los puntos en forma cartesiana y guarda en una lista aquellos que estan 
		#	en una caja al costado del coche
		if (side == -1):
			lim_inf = ymin
			lim_sup = ymax
		else:
			lim_inf = -ymax
			lim_sup = -ymin
		i = 0
		X_side = []
		Y_side = []
		for r in R:
			x = r*np.cos(i*(np.pi/180.0))
			y = r*np.sin(i*(np.pi/180.0))
			i = i+1
			if (x>=-1.0) and (x<=1.0) and (y>=lim_inf) and (y<=lim_sup):
				X_side.append(100.0*x) # Convierte a [cm]
				Y_side.append(100.0*y)
		return X_side, Y_side
#**********************************************************************************************************************************	
#**********************************************************************************************************************************
	def lidar4ransac(self,R,L,eps):
	# Toma los puntos en forma cartesiana y guarda aquellos que estan cerca de la linea detectada 
	# en la iteracion anterior
		m = L[0]
		b = L[1]
		i = 0
		X = []
		Y = []
		for r in R:
			x = 100.0*r*np.cos(i*(np.pi/180.0)) # Convierte a [cm]
			y = 100.0*r*np.sin(i*(np.pi/180.0))
			i = i+1
			d = abs(y-m*x-b)/np.sqrt(1+m**2)
			if (d<=eps):
				X.append(x)
				Y.append(y)
		return X, Y
#**********************************************************************************************************************************	
#**********************************************************************************************************************************
	def lidar_obj(self,R):
		# Toma los puntos en forma polar y detecta si hay un obstaculo enfrente
		R0_i = R[0:12]
		R0_d = R[359:347]
		R0 = np.concatenate((R0_i,R0_d),axis=None)
		r0 = np.min(R0)
		rb = np.min(R)
		thb = np.argmin(R)

		if (r0<=0.9): obj_f = True
		else: obj_f = False

		if (rb>=0.30) and (179<=thb<=205): obj_b = True
		else: obj_b = False

		return obj_f, obj_b
#**********************************************************************************************************************************	
#**********************************************************************************************************************************
	def vis_lidar(self,m,b,R):
		r_min = np.amin(R)
		th_min = np.argmin(R)
		x1 = -200
		x2 = 200
		y1_r = int(299.0-(m*x1+b))
		y2_r = int(299.0-(m*x2+b))
		x1_r = x1+299
		x2_r = x2+299
		x1_min = int(100.0*r_min*np.cos(th_min)+299.0)
		y1_min = int(299.0-100.0*r_min*np.sin(th_min))
		imagenR = np.zeros((600,600,3))
		font = cv2.FONT_HERSHEY_SIMPLEX
		imagenR =cv2.line(imagenR, (299,299),(329,299), (255,0,0), 2) #ejeX
		imagenR = cv2.putText(imagenR, 'X', (331, 299), font, 0.4, (255,255,255), 1, cv2.LINE_AA)
		imagenR =cv2.line(imagenR, (299,299),(299,269), (0,0,255), 2) #ejeY
		imagenR = cv2.putText(imagenR, 'Y', (299,267), font, 0.4, (255,255,255), 1, cv2.LINE_AA)
		imagenR =cv2.line(imagenR, (x1_r,y1_r),(x2_r,y2_r), (0,125,255), 2)
		imagenR =cv2.line(imagenR, (299,299),(x1_min,y1_min), (255,255,0), 2)
		imagenR = cv2.circle(imagenR,(299,299),2,(255, 255, 255),-1)
		i = 0
		for j in self.R:
			r_l = j*100.0
			th_l = (i)*(np.pi/180.0)
			x = int(r_l*np.cos(th_l)+299.0)
			y = int(299.0-r_l*np.sin(th_l))
			imagenR = cv2.circle(imagenR,(x,y),2,(0, 0, 255),-1)
			i = i+1
		cv2.imshow('lidar',imagenR)
		#cv2.moveWindow("lidar", 400,400)
		cv2.waitKey(1)
#**********************************************************************************************************************************	
#**********************************************************************************************************************************


















