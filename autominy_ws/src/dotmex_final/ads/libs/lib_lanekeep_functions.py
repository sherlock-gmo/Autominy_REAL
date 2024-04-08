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
		self.lower = np.array([0,180,180])	#RGB: 100,46,170 # BGR: 0,45,146
		self.upper = np.array([20,255,255])	#RGB:140,255,255 # BGR: 11,255,255
		# Recorte vertical de la imagen
		self.y_cut = 270
		# Traslacion para recortar la imagen sin distorcion
		self.x_tras = 198
		self.y_tras = 172
		# Parametros iniciales para el detector
		self.eps = 15.0
		self.n0 = 30.0
		self.alpha = 0.85 #0.85
		self.L = self.init_L()
	#**********************************************************************************************************************************	
	#**********************************************************************************************************************************
	def init_L(self):
		# Se porponen dos lineas iniciales:
		mr = 0.0
		br = 180.0
		ml = 0.0
		bl = 120.0
		L = np.array([[mr, ml],[br, bl]])
		return L
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
	def get_list(self,imagenSeg,l):
		# Encontrar las coordenadas de los pixeles blancos
		list_px = cv2.findNonZero(imagenSeg)
		# Suma y_cut a la coordenada y para mantener el sistema coordenado correcto
		list_px[:,:, 1] += self.y_cut #270
		list_px = list_px.astype(np.float32)
		list_px = cv2.undistortPoints(list_px, self.K, self.dist_coeffs, R=None, P=self.nK)
		# Traslacion necesaria para mantener el sistema coordenado correcto
		list_px[:,:, 0] -= self.x_tras #198
		list_px[:,:, 1] -= self.y_tras #172
		list_px = cv2.perspectiveTransform(list_px, self.H)
		# Toma los indices de los elementos cuya coordenada y esta entre 299 y 299-l
		cond1 = list_px[:,:,1]>=299-l
		cond2 = list_px[:,:,1]<=299
		COND = cond1 & cond2
		list_px = list_px[COND[:,0],:,:]
		N,_,_ = list_px.shape
		list_px = np.reshape(list_px,(N,2))
		return list_px,N
	#**********************************************************************************************************************************
	#**********************************************************************************************************************************
	def fit_ransac(self,coordenadas_lista):
		# Convertir la lista de puntos en dos arrays separados para las coordenadas x e y
		x = coordenadas_lista[:,1]
		y = coordenadas_lista[:,0]
		# Reshape para que los arrays tengan la forma adecuada para scikit-learn
		x = x.reshape(-1, 1)
		y = y.reshape(-1, 1)
		# Ajustar el modelo a los puntos
		ransac.fit(x, y)
		# Obtener los inliers y outliers del modelo ajustado
		inliers_mask = ransac.inlier_mask_
		# Obtener la pendiente y el termino independiente del modelo ajustado
		m = ransac.estimator_.coef_[0][0]
		b = ransac.estimator_.intercept_[0]
		# Calcular el error cuadratico medio de los inliers
		r = mean_squared_error(y[inliers_mask], ransac.predict(x[inliers_mask]))
		return m,b,r
	#**********************************************************************************************************************************
	#**********************************************************************************************************************************
	def ball_finder(self,Z,eps):
		# Toma la lista de puntos Z, agarra un punto p de forma aleatoria y crea una bola B
		# de radio eps, centrada en p. Devuelve la bola, el punto p y la cantidad de elementos que tiene
		M,_ = Z.shape
		i = np.random.randint(0,M)
		x = Z[i,0]
		y = Z[i,1]
		p = np.array([x,y])
		d = np.linalg.norm(Z-p,2,axis=1)
		# Toma los indices de los elementos que son menores a eps
		cond = d<=eps
		B = Z[cond,:]
		n,_ = B.shape
		return np.array(B), np.reshape(p,(1,2)), n
	#**********************************************************************************************************************************
	#**********************************************************************************************************************************
	def min_line(self,Z,eps,n0):
		#l = 0
		k = True
		while (k==True):
			# Crea una bola de radio eps, centrada en un punto p aleatorio
			B, p, n = self.ball_finder(Z,eps)
			# Si la bola tiene menos de n0 elementos, busca otro punto p
			if (n>=n0):
				# Se intercambian los indices para que X sea el eje de avance y Y el lateral
				p = np.flip(p,axis=1)
				Yb = np.reshape(B[:,0],(n,1))
				Xb = np.reshape(B[:,1],(n,1))
				# Se hace una regresion lineal con los puntos de la bola
				reg = LinearRegression().fit(Xb,Yb)
				#r = reg.score(Xb, Yb)
				m = reg.coef_[0][0]
				b = reg.intercept_[0]
				k = False
		return p, m, b
	#**********************************************************************************************************************************
	#**********************************************************************************************************************************
	def parallel_crit(self,i,L):
		# Verifica si las lineas detectadas son paralelas.
		# Si no, modifica una de las lineas para que lo sean
		j = 1-i		# si i=0 => j=1 || si i=1 => j=0
		#th1 = np.arctan(L[0,i])
		#th2 = np.arctan(L[0,j])
		#M = abs(th1-th2)
		#B = abs(L[1,i]-L[1,j]) # Separacion de las lineas
		# No son paralelas si forman un angulo de 40deg o estan separadas 32+-15 cm
		#if (abs(B)<50.0): # or (M>0.35):
		L[0,j] = L[0,i]
		L[1,j] = L[1,i]+60.0*(2*i-1)
		return L
	#**********************************************************************************************************************************
	#**********************************************************************************************************************************
	def act_line(self,L,p,m,b,alpha):
		# Las lineas que se esperan obtener son 2 y sus parametros se guardan en una matriz L
		# L = np.array([[mr, mc, ml],[br, bc, bl]])
		# Esta funcion actualiza los elementos de L en funcion de los parametros m y b que se obtuvieron
		# de la regresion lineal de la bola
		x = p[0][0]
		y = p[0][1]
		# Se calcula la distancia entre el punto p y las rectas definidas por L
		dr = abs(y-L[0,0]*x-L[1,0])/np.sqrt(1.0+L[0,0]**2)
		dl = abs(y-L[0,1]*x-L[1,1])/np.sqrt(1.0+L[0,1]**2)
		#dr = np.sqrt((m-L[0,0])**2+(b-L[1,0])**2)
		#dl = np.sqrt((m-L[0,1])**2+(b-L[1,1])**2)
		# Se actualiza solo la columna con menor distancia
		i = np.argmin([dr,dl])
		#if (min(dr,dl)<15.0):
			# Regla de actualizacion con parametro de aprendizaje alfa (Regla delta)
		L[0,i] = L[0,i]+alpha*(m-L[0,i])
		L[1,i] = L[1,i]+alpha*(b-L[1,i])
		# Verifica si son paralelas
		#L = self.parallel_crit(i,L)
		# Verifica que la matriz L esta ordenada de manera correcta,
		# es decir, si la primera columna es la linea de la derecha
		yr = L[0,0]*299.0+L[1,0]
		yl = L[0,1]*299.0+L[1,1]
		if (yr<yl): L[:,[0,1]]=L[:,[1,0]]
		return L
	#**********************************************************************************************************************************
	#**********************************************************************************************************************************
	def get_lines(self,P,L,eps):
		# Selecciona los puntos de P dependiendo de su cercania con las lineas de L de la iteracion anterior
		# L = np.array([[mr, mc, ml],[br, bc, bl]])
		# P es la lista de pixeles
		# eps es la distancia de tolerancia en [cm]
		# Obtiene el indice de las lineas derecha e izquierda
		i_l = 1 #np.argmin(L[1,:])
		i_r = 0 #np.argmax(L[1,:])
		L_ransac = L

		#______________________DERECHA______________________
		# Calcula la distancia entre los puntos de P y la linea Lr(mr,br)
		d_r = np.absolute(P[:,0]-L[0,i_r]*P[:,1]-L[1,i_r])/np.sqrt(1.0+L[0,i_r]**2)
		# Toma los indices de los puntos mas cercanos a Lr (distancias menores a eps)
		d_r = np.where(d_r<=eps)[0]
		# Hace un ajuste tipo RANSAC
		if (d_r.size>50):
			m_r,b_r,R_r = self.fit_ransac(P[d_r])
			L_ransac[:,0] = [m_r,b_r]
		else:
			print('No se ve l. derecha')
			R_r = 100.0
		#______________________IZQUIERDA______________________
		# Calcula la distancia entre los puntos de P y la linea Ll(ml,bl)
		d_l = np.absolute(P[:,0]-L[0,i_l]*P[:,1]-L[1,i_l])/np.sqrt(1.0+L[0,i_l]**2)
		# Toma los indices de los puntos mas cercanos a Ll (distancias menores a eps)
		d_l = np.where(d_l<=eps)[0]
		# Hace un ajuste tipo RANSAC
		if (d_l.size>50):
			m_l,b_l,R_l = self.fit_ransac(P[d_l])
			L_ransac[:,1] = [m_l,b_l]
		else:
			print('No se ve l. izquierda')
			R_l = 100.0

		# Si solo aparece una linea, crea una linea paralela a la que si existe
		if (R_r>0.8 or R_l>0.8):
                        i = np.argmin(np.array([R_r,R_l]))
                        L_ransac = self.parallel_crit(i,L_ransac)
		"""
		print('R_r ',R_r)
		print(d_r.size)
		print('R_l ',R_l)
		print(d_l.size)
		print('*************************')
		"""
		yr = L_ransac[0,0]*299.0+L_ransac[1,0]
		yl = L_ransac[0,1]*299.0+L_ransac[1,1]
		# Verifica si no se han juntado las lineas por un error
		if (abs(yr-yl)<50.0):
			i = np.argmin(np.array([R_r,R_l]))
			L_ransac = self.parallel_crit(i,L_ransac)
		# Verifica que la matriz L esta ordenada de manera correcta,
		# es decir, si la primera columna es la linea de la derecha
		if (yr<yl): L_ransac[:,[0,1]]=L_ransac[:,[1,0]]
		return	L_ransac
	#**********************************************************************************************************************************
	#**********************************************************************************************************************************
	def line_class_FT(self,K,list_px,L):
		# Se entrena el clasificador de datos durante K iteraciones
		for k in range (0,K):
			#	Se busca un punto de forma aleatoria y se hace una regresion lineal con sus vecinos
			p, m, b = self.min_line(list_px,self.eps,self.n0)
			# Se actualiza el clasificador de lineas
			L = self.act_line(L,p,m,b,self.alpha)
		return L
	#**********************************************************************************************************************************
	#**********************************************************************************************************************************
	def vis_lines(self,list_px,L,l):
		# VISUALIZACION
		x1r = 299-l
		x2r = 299
		y1r = int(round(x1r*L[0,0]+L[1,0]))
		y2r = int(round(x2r*L[0,0]+L[1,0]))
		x1l = 299-l
		x2l = 299
		y1l = int(round(x1l*L[0,1]+L[1,1]))
		y2l = int(round(x2l*L[0,1]+L[1,1]))
		imagenH = np.zeros((300,300,3))
		for x,y in list_px: imagenH = cv2.circle(imagenH, (int(x), int(y)), 2, (0, 255, 0), -1)
		imagenH =cv2.line(imagenH, (y1r,x1r),(y2r,x2r), (0,0,255), 2)
		imagenH =cv2.line(imagenH, (y1l,x1l),(y2l,x2l), (255,0,0), 2)
		cv2.imshow('test',imagenH)
		cv2.waitKey(1)
	#**********************************************************************************************************************************
	#**********************************************************************************************************************************










