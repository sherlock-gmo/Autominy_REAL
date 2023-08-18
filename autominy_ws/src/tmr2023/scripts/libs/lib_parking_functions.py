#! /usr/bin/env python
import numpy as np
from sklearn.linear_model import RANSACRegressor

ransac = RANSACRegressor()
#**********************************************************************************************************************************
def fit_ransac(R,rmax):
	L = len(R)
	X = []
	Y = []
	for i in range (0,L):
		if (R[i]<rmax) and (R[i]>0.0):
			r = R[i]*100.0 # Convierte de [m] a [cm]
			th = i*(np.pi/180.0)
			X.append(r*np.cos(th))
			Y.append(r*np.sin(th))
	L = len(X)
	X = np.reshape(np.array(X),(L,1))
	Y = np.reshape(np.array(Y),(L,1))
	reg = ransac.fit(X,Y)
	x1 = 0
	x2 = 1
	X_m = np.array([[x1], [x2]]) #np.reshape(np.array([x1, x2]),(2,1))
	y1,y2 = reg.predict(X_m)
	m = (y2-y1)/(x2-x1)
	b = y2-m*x2
	return(m,b)
#**********************************************************************************************************************************
def steer_control(m,b,d_ref):
	Ky = -0.2
	Kth = -9.2
	d = b/np.sqrt(m**2+1)
	e_y = d_ref-d
	e_th = -np.arctan(m)
	u = np.arctan(Ky*e_y+Kth*e_th)*(1.0/(np.pi/2.0)) #unidades normalizadas
	return(u,d)
#**********************************************************************************************************************************
def measure_D(r_min,th_min):
	if (th_min<4.7124): D_est = 2*r_min*np.sin(4.7124-th_min)
	else: D_est = 0.0
	return D_est
