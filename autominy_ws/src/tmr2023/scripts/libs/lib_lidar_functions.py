#! /usr/bin/env python
import cv2
import numpy as np
"""
#********************************************************************************
#********************************************************************************
def lidar_roi(R,side):
	side_space = True
	count_side = 0
	i = 0
	for r in R:
		x = r*np.cos(i*(np.pi/180.0))
		y = r*np.sin(i*(np.pi/180.0))
		i = i+1
		k = (-1)*side
		if (side == -1):
			lim_inf = 0.15
			lim_sup = 0.35
		else:
			lim_inf = -0.35
			lim_sup = -0.15
		if (x>=-0.35) and (x<=0.25) and (y>=lim_inf) and (y<=lim_sup): count_side = count_side+1
	if (count_side>=2): side_space = False
	return side_space, count_side
#********************************************************************************
#********************************************************************************
def lidar_roi2(R,side):
	side_space = True
	count_side = 0
	i = 0
	for r in R:
		x = r*np.cos(i*(np.pi/180.0))
		y = r*np.sin(i*(np.pi/180.0))
		i = i+1
		k = (-1)*side
		if (side == -1):
			lim_inf = 0.15
			lim_sup = 0.7
		else:
			lim_inf = -0.7
			lim_sup = -0.15
		if (x>=-0.25) and (x<=0.15) and (y>=lim_inf) and (y<=lim_sup): count_side = count_side+1
	if (count_side>=2): side_space = False
	return side_space, count_side
"""
#********************************************************************************
#********************************************************************************
def lidar_roi_f(R,side,depth):
	side_space = True
	count_side = 0
	i = 0
	for r in R:
		x = r*np.cos(i*(np.pi/180.0))
		y = r*np.sin(i*(np.pi/180.0))
		i = i+1
		k = (-1)*side
		if (side == -1):
			lim_inf = 0.15
			lim_sup = depth
		else:
			lim_inf = -depth
			lim_sup = -0.15
		#if (x>=-0.25) and (x<=0.15) and (y>=lim_inf) and (y<=lim_sup): count_side = count_side+1 #tmr2023_final_1_2_3.py
		#if (x>=-0.1) and (x<=0.3) and (y>=lim_inf) and (y<=lim_sup): count_side = count_side+1 #tmr2023_final_1_2_3_b.py
		if (x>=-0.1) and (x<=0.4) and (y>=lim_inf) and (y<=lim_sup): count_side = count_side+1 #tmr2023_final_1_2_3_c.py
	if (count_side>=2): side_space = False
	return side_space


#****************************************************************************************************************
def lidar_roi_f3(R,side,depth,x_p,x_n):
        side_space = True
        count_side = 0
        i = 0
        for r in R:
                x = r*np.cos(i*(np.pi/180.0))
                y = r*np.sin(i*(np.pi/180.0))
                i = i+1
                k = (-1)*side
                if (side == -1):
                        lim_inf = 0.15
                        lim_sup = depth
                else:
                        lim_inf = -depth
                        lim_sup = -0.15
                if (x>=x_n) and (x<=x_p) and (y>=lim_inf) and (y<=lim_sup): count_side = count_side+1 #tmr2023_fi1nal_1_2_3_c.py
        if (count_side>=2): side_space = False
        return side_space

#********************************************************************************
#********************************************************************************
def lidar_ev(R):
	cont1 = 0
	cont2 = 0
	for i in range(0,155):
		r = R[i]
		if (135<i<155) and (0.35<=r<=0.55): cont1 = cont1+1
		if (0<i<=135) and (r<0.35): cont2 = cont2+1
	if (cont1>=10) and (cont2==0): end_ev = True
	else: end_ev = False
	return end_ev
"""
#********************************************************************************
#********************************************************************************
def lidar_side(R,rmax,rmin,side):
	i = 0
	R_side = []
	for r in R:
		x = r*np.cos(i*(np.pi/180.0))
		y = r*np.sin(i*(np.pi/180.0))
		i = i+1
		if (side == -1):
			lim_inf = rmin
			lim_sup = 0.3 #0.35
		else:
			lim_inf = -0.3
			lim_sup = -rmin
		if (x>=-2.0) and (x<=2.0) and (y>=lim_inf) and (y<=lim_sup): R_side.append(r)
		else: R_side.append(rmax)
	return R_side
#********************************************************************************
#********************************************************************************
def lidar_side2(R,ymax,ymin,side):
	i = 0
	R_side = []
	for r in R:
		x = r*np.cos(i*(np.pi/180.0))
		y = r*np.sin(i*(np.pi/180.0))
		i = i+1
		if (side == -1):
			lim_inf = ymin
			lim_sup = ymax #0.35
		else:
			lim_inf = -ymax
			lim_sup = -ymin
		if (x>=-1.5) and (x<=1.5) and (y>=lim_inf) and (y<=lim_sup): R_side.append(r)
		else: R_side.append(3.0)
	return R_side
"""
#********************************************************************************
#********************************************************************************
def lidar4ransac(R,ymax,ymin,side):
	i = 0
	R_side = []
	for r in R:
		x = r*np.cos(i*(np.pi/180.0))
		y = r*np.sin(i*(np.pi/180.0))
		i = i+1
		if (side == -1):
			lim_inf = ymin
			lim_sup = ymax #0.35
		else:
			lim_inf = -ymax
			lim_sup = -ymin
		if (x>=-2.5) and (x<=2.5) and (y>=lim_inf) and (y<=lim_sup): R_side.append(r)
		else: R_side.append(3.0)
	return R_side
#********************************************************************************
#********************************************************************************
def vis_lidar(m,b,R):
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
#********************************************************************************
#********************************************************************************







#********************************************************************************
#********************************************************************************
def lidar_roi_f2(R,side):
	side_space = True
	count_side = 0
	i = 0
	for r in R:
		x = r*np.cos(i*(np.pi/180.0))
		y = r*np.sin(i*(np.pi/180.0))
		i = i+1
		k = (-1)*side
		if (side == -1):
			lim_inf = 0.15
			lim_sup = 0.6
		else:
			lim_inf = -0.6
			lim_sup = -0.15
		#if (x>=-0.25) and (x<=0.25) and (y>=lim_inf) and (y<=lim_sup): count_side = count_side+1 #tmr2023_final_1_2_3.py
		if (x>=-0.1) and (x<=0.25) and (y>=lim_inf) and (y<=lim_sup): count_side = count_side+1 #tmr2023_final_1_2_3_b.py

	if (count_side>=2): side_space = False
	return side_space






