#! /usr/bin/env python
import cv2
import rospy
import numpy as np
from sklearn.linear_model import RANSACRegressor, LinearRegression
from sklearn.metrics import mean_squared_error

ransac = RANSACRegressor()
#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
class lane_keep_f():
	#**********************************************************************************************************************************	
	#**********************************************************************************************************************************
	def __init__(self):
		# Vectores y matrices de la camara
		self.H = np.array([[-5.37973506e-02,-1.31762265,1.63979885e+02],[6.45042207e-03,-2.72330382,3.17042324e+02],[2.76842149e-05,-8.84786795e-03,1.0]])
		self.K = np.array([[410.80239519,0.0,469.13953267],[0.0,412.74534584,258.91870387],[0.0,0.0,1.0]])
		self.dist_coeffs = np.array([[-2.80892642e-01,7.20543846e-02,-1.77783135e-04,-9.27152558e-04,-7.49371778e-03]])
		self.nK,_ = cv2.getOptimalNewCameraMatrix(self.K, self.dist_coeffs, (540,960), 1, (540,960))

		# Crea la mascara del color segmentado (anaranjado)
		self.lower = np.array([100,150,200])	#RGB: 100,46,170 # BGR: 0,45,146
		self.upper = np.array([126,255,255])	#RGB:140,255,255 # BGR: 11,255,255

		# Recorte vertical de la imagen
		self.y_cut = 270	

		# Traslacion para recortar la imagen sin distorcion
		self.x_tras = 198 
		self.y_tras = 172

		# Parametros iniciales para el detector
		self.eps = 10.0
		self.n0 = 20.0
		self.alpha = 0.85

		# Se porponen tres lineas iniciales:
		mr = 0.0 
		br = 170.0 
		mc = 0.0 
		bc = 130.0 
		ml = 0.0 
		bl = 90.0 
		self.L = np.array([[mr, mc, ml],[br, bc, bl]])
	#**********************************************************************************************************************************	
	#**********************************************************************************************************************************
	def seg_img(self,imagen0,F):
		K = 1
		# F=True-> Recorta la imagen
		if (F==True): imagen0 = imagen0[self.y_cut:,:]
		imagenHSV = cv2.cvtColor(imagen0,cv2.COLOR_BGR2HSV)
		imagenSeg = cv2.inRange(imagenHSV,self.lower,self.upper)
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
		#x = np.array([punto[0] for punto in coordenadas_lista])
		#y = np.array([punto[1] for punto in coordenadas_lista])
		x = coordenadas_lista[:,1]
		y = coordenadas_lista[:,0]
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
	def ball_finder(self,Z,eps):
		M,_ = Z.shape  
		i = np.random.randint(0,M)
		x = Z[i,0]
		y = Z[i,1]
		p = np.array([x,y])
		d = np.linalg.norm(Z-p,axis=1)
		# Toma los indices de los elementos que son menores a eps
		d = np.where(d<eps)[0] 		
		B = Z[d]
		n,_ = B.shape
		return np.array(B), np.reshape(p,(1,2)), n
	#**********************************************************************************************************************************
	#**********************************************************************************************************************************
	def min_line(self,Z,eps,n0):
		#l = 0
		k = True
		while (k==True):
			B, p, n = self.ball_finder(Z,eps)
			if (n>=n0): 
				# Se intercambian los indices para que X sea el eje de avance y Y el lateral
				p = np.flip(p,axis=1)
				Yb = np.reshape(B[:,0],(n,1))
				Xb = np.reshape(B[:,1],(n,1))
				reg = LinearRegression().fit(Xb,Yb)
				#r = reg.score(Xb, Yb)
				m = reg.coef_[0][0]
				b = reg.intercept_[0]
				k = False
			#l = l+1
		#print(r)
		#print('repeat ',l)
		return p, m, b#, r
	#**********************************************************************************************************************************
	#**********************************************************************************************************************************
	def act_line(self,L,p,m,b,alpha):
		x = p[0][0]
		y = p[0][1]
		d = np.absolute(y-L[0,:]*x-L[1,:])/np.sqrt(1.0+L[0,:]**2)
		i = np.argmin(d)
		L[0,i] = L[0,i]+alpha*(m-L[0,i]) 
		L[1,i] = L[1,i]+alpha*(b-L[1,i]) 
		return L
	#**********************************************************************************************************************************
	#**********************************************************************************************************************************
	def get_lines(self,P,L,eps):
		# Selecciona los puntos dependiendo de su cercania con las lineas de la iteracion anterior
		i_r = np.argmin(L[1,:])
		i_l = np.argmax(L[1,:])
		i_c = 3-i_r-i_l
		# DERECHA		
		d_r = np.absolute(P[:,0]-L[0,i_r]*P[:,1]-L[1,i_r])/np.sqrt(1.0+L[0,i_r]**2)	# Calcula la distancia de tolerancia
		d_r = np.where(d_r<eps)[0]															# Toma los indices de los elementos que son menores a eps
		L_r = P[d_r]
		m_r,b_r,R_r = self.fit_ransac(L_r)											# Hace un ajuste tipo RANSAC
		# CENTRAL
		d_c = np.absolute(P[:,0]-L[0,i_c]*P[:,1]-L[1,i_c])/np.sqrt(1.0+L[0,i_c]**2)	# Calcula la distancia de tolerancia
		d_c = np.where(d_c<eps)[0]															# Toma los indices de los elementos que son menores a eps
		L_c = P[d_c]
		m_c,b_c,R_c = self.fit_ransac(L_c)											# Hace un ajuste tipo RANSAC
		# IZQUIERDA
		d_l = np.absolute(P[:,0]-L[0,i_l]*P[:,1]-L[1,i_l])/np.sqrt(1.0+L[0,i_l]**2)	# Calcula la distancia de tolerancia
		d_l = np.where(d_l<eps)[0]															# Toma los indices de los elementos que son menores a eps
		L_l = P[d_l]
		m_l,b_l,R_l = self.fit_ransac(L_l)											# Hace un ajuste tipo RANSAC
		# Crea la matriz L de salida
		L_ransac = np.array([[m_r, m_c, m_l],[b_r, b_c, b_l]])
		R = np.array([[R_r,R_c,R_l]])
		return	L_ransac, R
	#**********************************************************************************************************************************
	#**********************************************************************************************************************************
	def line_class_FT(self,K,list_px):
		# Se entrena el clasificador de datos durante K iteraciones 
		for k in range (0,K): 
			#	Se busca un punto de forma aleatoria y se hace una regresion lineal con sus vecinos
			p, m, b = self.min_line(list_px,self.eps,self.n0)
			# Se actualizan el clasificador de lineas
			self.L = LKF.act_line(self.L,p,m,b,self.alpha)
	return self.L






