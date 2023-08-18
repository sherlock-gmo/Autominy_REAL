#! /usr/bin/env python
import numpy as np
#********************************************************************************
#********************************************************************************
def lidar_roi(R):
	Rf = False
	Rl = False
	Rr = False
	count_f = 0
	count_l = 0
	count_r = 0
	i = 0
	for r in R:
		x = r*np.cos(i*(np.pi/180.0))
		y = r*np.sin(i*(np.pi/180.0))
		i = i+1
		if (x>=-0.2) and (x<=2.0) and (y>=-0.18) and (y<=0.18): count_f = count_f+1
		if (x>=-0.3) and (x<=0.3) and (y>=0.15) and (y<=0.35): count_l = count_l+1
		if (x>=-0.4) and (x<=0.3) and (y>=-0.75) and (y<=0.0): count_r = count_r+1
	if (count_f>=5): Rf = True
	if (count_l>=5): Rl = True #1
	if (count_r>=5): Rr = True
	return Rf, Rl, Rr
#********************************************************************************
#********************************************************************************
def lidar_ev(R):
	#i = 0
	cont1 = 0
	cont2 = 0
	for i in range(0,155):
		r = R[i]
		#x = r*np.cos(i*(np.pi/180.0))
		#y = r*np.sin(i*(np.pi/180.0))
		#i = i+1
		#if (-0.2<=x<=0.1) and (0<=y<=0.5): cont1 = cont1+1
		#if (-0.3<=x<=-0.1) and (-0.30<=y<=-0.1): rear_cont = rear_cont+1
		#if (115<i<135) and (r<0.38): cont = cont+1
		if (135<i<155) and (0.35<=r<=0.55): cont1 = cont1+1
		if (0<i<=135) and (r<0.35): cont2 = cont2+1

	if (cont1>=10) and (cont2==0): end_ev = True
	else: end_ev = False
	return end_ev
#********************************************************************************
#********************************************************************************
def lidar_left(R,rmax,rmin):
	i = 0
	R_left = []
	for r in R:
		x = r*np.cos(i*(np.pi/180.0))
		y = r*np.sin(i*(np.pi/180.0))
		i = i+1
		if (x>=-1.0) and (x<=1.0) and (y>=rmin) and (y<=0.35): R_left.append(r)
		else: R_left.append(rmax)
	return R_left
