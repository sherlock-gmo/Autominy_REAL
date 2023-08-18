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
