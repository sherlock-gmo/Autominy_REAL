#! /usr/bin/env python
import cv2
import rospy
import numpy as np
from sklearn.linear_model import RANSACRegressor
from sklearn.metrics import mean_squared_error
from sklearn.cluster import DBSCAN

ransac = RANSACRegressor()
#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
class lane_keep_f():
	#**********************************************************************************************************************************	
	#**********************************************************************************************************************************
	def __init__(self):
		self.H = np.array([[-5.37973506e-02,-1.31762265,1.63979885e+02],[6.45042207e-03,-2.72330382,3.17042324e+02],[2.76842149e-05,-8.84786795e-03,1.0]])
		self.K = np.array([[410.80239519,0.0,469.13953267],[0.0,412.74534584,258.91870387],[0.0,0.0,1.0]])
		self.dist_coeffs = np.array([[-2.80892642e-01,7.20543846e-02,-1.77783135e-04,-9.27152558e-04,-7.49371778e-03]])
		self.nK,_ = cv2.getOptimalNewCameraMatrix(self.K, self.dist_coeffs, (540,960), 1, (540,960))
		# Recorte vertical de la imagen
		self.y_cut = 270	
		# Traslacion para recortar la imagen sin distorcion
		self.x_tras = 198 
		self.y_tras = 172
	#**********************************************************************************************************************************	
	#**********************************************************************************************************************************
	def seg_img(self,imagen0):
		K = 1
		imagen0 = imagen0[self.y_cut:,:]
		# Color anaranjado BGR
		#lower = np.array([0,125,100])
		#upper = np.array([25,255,255])
		# Color anaranjado RGB
		lower = np.array([100,150,200])
		upper = np.array([126,255,255])
		imagenHSV = cv2.cvtColor(imagen0,cv2.COLOR_BGR2HSV)
		imagenSeg = cv2.inRange(imagenHSV,lower,upper)
		imagenSeg = cv2.medianBlur(imagenSeg,2*K+1)
		return imagenSeg
	#**********************************************************************************************************************************
	#**********************************************************************************************************************************
	def get_list(self,imagenSeg):
		# Encontrar las coordenadas de los pixeles blancos
		list_px = cv2.findNonZero(imagenSeg)				
		# Suma y_cut a la coordenada y para mantener el sistema coordenado correcto
		list_px[:,:, 1] += self.y_cut #270 							
		list_px = list_px.astype(np.float32)
		list_px = cv2.undistortPoints(list_px, self.K, self.dist_coeffs, R=None, P=self.nK)
		# Traslacion necesaria para antener el sistema coordenado correcto
		list_px[:,:, 0] -= self.x_tras #198						
		list_px[:,:, 1] -= self.y_tras #172							
		list_px = cv2.perspectiveTransform(list_px, self.H)
		N,_,_ = list_px.shape	
		list_px = np.reshape(list_px,(N,2))
		return list_px
	#**********************************************************************************************************************************
	#**********************************************************************************************************************************
	def fit_ransac(self,coordenadas_lista):
		# Convertir la lista de puntos en dos arrays separados para las coordenadas x e y
		y = np.array([punto[0] for punto in coordenadas_lista])
		x = np.array([punto[1] for punto in coordenadas_lista])
		# Reshape para que los arrays tengan la forma adecuada para scikit-learn
		x = x.reshape(-1, 1)
		y = y.reshape(-1, 1)
		# Ajustar el modelo a los puntos
		ransac.fit(x, y)
		# Obtener los inliers y outliers del modelo ajustado
		inliers_mask = ransac.inlier_mask_
		#outliers_mask = np.logical_not(inliers_mask)
		# Obtener la pendiente y el termino independiente del modelo ajustado
		m = ransac.estimator_.coef_[0][0]
		b = ransac.estimator_.intercept_[0]
		# Calcular el error cuadratico medio de los inliers
		r = mean_squared_error(y[inliers_mask], ransac.predict(x[inliers_mask]))
		# Imprimir los resultados
		#print("m: ",m)
		#print("b: ", b)
		#print("Error cuadratico medio de los inliers: ", inliers_error)
		return m,b,r
	#**********************************************************************************************************************************
	#**********************************************************************************************************************************
	def get_lines(self,coordenadas):
		# Definir el algoritmo DBSCAN con el radio de vecindad y el numero minimo de puntos para formar un grupo
		eps = 25  																			# Radio de vecindad
		min_samples = 50  															# Numero minimo de puntos en un grupo
		dbscan = DBSCAN(eps=eps, min_samples=min_samples)
		etiquetas = dbscan.fit_predict(coordenadas)			# Aplicar el algoritmo DBSCAN a las coordenadas
		sublistas = {}																	# Crear un diccionario para almacenar las sublistas de puntos agrupados
		# Recorre las etiquetas y agrupa los puntos en sublistas
		for i, etiqueta in enumerate(etiquetas):
			if etiqueta not in sublistas: sublistas[etiqueta] = []
			sublistas[etiqueta].append(coordenadas[i])
		A = sublistas.items()	
		M = []
		B = []
		R = []
		Y0 = []
		for _ , sublista in A:
			m,b,r = self.fit_ransac(sublista)
			y0 = m*299.0+b #(299.0-b)/m
			if (y0>=0.0) and (y0<=299.0):
				M.append(m)
				B.append(b)
				R.append(r)
				Y0.append(y0)
		return M, B, R, Y0
	#**********************************************************************************************************************************
	#**********************************************************************************************************************************
	def seg_lines(self,Y0,M,B,R,l):
		# Quita las lineas con un MSE mayor a 2.0
		k = 0
		for mse in R:
			#print('k ',k)
			#print('mse ',mse)
			if (mse>2.0):
				del Y0[k]
				del M[k]
				del B[k]
			k = k+1

		# Linea Der.
		i = np.argmax(np.array(Y0))
		x2_d = 299
		y2_d = int(round(Y0[i]))
		x1_d = 299-l
		y1_d = int(round(x1_d*M[i]+B[i]))
		
		# Linea Izq.
		j = np.argmin(np.array(Y0))
		x2_i = 299
		y2_i = int(round(Y0[j]))
		x1_i = 299-l
		y1_i = int(round(x1_i*M[j]+B[j]))
			
		# Linea C.
		N = len(Y0)
		for k in range(N):
			if (Y0[j]<Y0[k]<Y0[i]):
				x2_c = 299
				y2_c = int(round(Y0[k]))
				x1_c = 299-l
				y1_c = int(round(x1_c*M[k]+B[k]))

		Pd = [x1_d,y1_d,x2_d,y2_d]
		Pc = [x1_c,y1_c,x2_c,y2_c]
		Pi = [x1_i,y1_i,x2_i,y2_i]
		return Pd, Pc, Pi
	#**********************************************************************************************************************************
	#**********************************************************************************************************************************

























"""
#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************
def roi_zone(x):
	assert (x>=0) and (x<=199), 'x out of limits'
	if (x>118) and (x<=199):
		y = int(round(-2.0998*x+546.6584))
	if (x>=81) and (x<=118):
		y = 299
	if (x>=0) and (x<81):
		y = int(round(1.8765*x+147.0))
	return y
#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************
def vec_create(x,stride,side):
	if(side==1):
		xi = x+stride
		xd = x-stride
	else:
		xi = x-stride
		xd = x+stride
	if(xi<0): xi = 0
	if(xi>199): xi = 199
	if(xd<0): xi = 0
	if(xd>199): xi = 199
	xv = np.arange(xi,xd,(-1)*side)
	return xv
#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************
def line_detector(imagen0,x1,l,side):
	K = True
	stridex = 12
	stridey = 12
	y1 = roi_zone(x1)
	x1v = vec_create(x1,stridex,side)
	while (K==True):
		m = y1+stridey
		if (m>=299): m = 299
		for j in range(m,y1-stridey,-1):
			for i in x1v:
				if imagen0[j][i]==255:
					x1 = i
					y1 = j
					K = False
					break
			x1v = vec_create(x1,stridex,side)
			if (K==False): break
		if (K==True):
			x1 = x1-1*side
			y1 = roi_zone(x1)
	x2 = x1
	x2v = vec_create(x2,stridex,side)
	for j in range(y1-1,y1-l,-1):
		for i in x2v:
			if imagen0[j][i]==255:
				x2 = i
				y2 = j
				K = False
				break
		x2v = vec_create(x2,stridex,side)
	return x1,y1,x2,y2
"""
