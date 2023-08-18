import cv2
import numpy as np
from sklearn.linear_model import RANSACRegressor
from sklearn.metrics import mean_squared_error
from sklearn.cluster import DBSCAN


#**********************************************************************************************************************************	
#**********************************************************************************************************************************
#**********************************************************************************************************************************
def seg_img(imagen0,y_cut):
	imagen0 = imagen0[y_cut:,:]
	K = 1
	# Color anaranjado
	lower = np.array([0,125,100])
	upper = np.array([25,255,255])
	imagenHSV = cv2.cvtColor(imagen0,cv2.COLOR_BGR2HSV)
	imagenSeg = cv2.inRange(imagenHSV,lower,upper)
	imagenSeg = cv2.medianBlur(imagenSeg,2*K+1)
	return imagenSeg
#**********************************************************************************************************************************
#**********************************************************************************************************************************
def get_list(imagenSeg,y_cut,x_tras,K,dist_coeffs,nK):
	# Encontrar las coordenadas de los pixeles blancos
	list_px = cv2.findNonZero(imagenSeg)				
	# Suma y_cut a la coordenada y para mantener el sistema coordenado correcto
	list_px[:,:, 1] += y_cut #270 							
	list_px = list_px.astype(np.float32)
	list_px = cv2.undistortPoints(list_px, K, dist_coeffs, R=None, P=nK)
	# Traslacion necesaria para antener el sistema coordenado correcto
	list_px[:,:, 0] -= x_tras #228							
	list_px = cv2.perspectiveTransform(list_px, H)
	N,_,_ = list_px.shape	
	list_px = np.reshape(list_px,(N,2))
	return list_px
#**********************************************************************************************************************************
#**********************************************************************************************************************************
def fit_ransac(coordenadas_lista):
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
	# Obtener la pendiente y el término independiente del modelo ajustado
	m = ransac.estimator_.coef_[0][0]
	b = ransac.estimator_.intercept_[0]
	# Calcular el error cuadrático medio de los inliers
	r = mean_squared_error(y[inliers_mask], ransac.predict(x[inliers_mask]))
	# Imprimir los resultados
	#print("m: ",m)
	#print("b: ", b)
	#print("Error cuadrático medio de los inliers: ", inliers_error)
	return m,b,r
#**********************************************************************************************************************************
#**********************************************************************************************************************************
def get_lines(coordenadas):
	# Definir el algoritmo DBSCAN con el radio de vecindad y el numero minimo de puntos para formar un grupo
	eps = 20  																			# Radio de vecindad
	min_samples = 200  															# Numero minimo de puntos en un grupo
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
		m,b,r = fit_ransac(sublista)
		y0 = m*299.0+b #(299.0-b)/m
		if (y0>=0.0) and (y0<=299.0):
			M.append(m)
			B.append(b)
			R.append(r)
			Y0.append(y0)
	return M, B, R, Y0
	
#**********************************************************************************************************************************
#**********************************************************************************************************************************
def seg_lines(Y0,M,B,R,l):
	# Quita las lineas con un MSE mayor a 2.0
	k = 0
	for mse in R:
		#print('k ',k)
		#print('mse ',mse)
		if (mse>2.0):
			del Y0[k]
			del M[k]
			del B[k]

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
#						PRINCIPAL
#**********************************************************************************************************************************
#**********************************************************************************************************************************
# Crear un estimador RANSACRegressor para ajuste lineal
ransac = RANSACRegressor()

H = np.array([[-7.10413148e-02,-1.05243615,1.63532529e+02],[-3.40016154e-02,-2.17357369,3.17446522e+02],[-1.10253784e-04,-7.04538511e-03,1.0]])
K = np.array([[410.80239519,0.0,469.13953267],[0.0,412.74534584,258.91870387],[0.0,0.0,1.0]])
dist_coeffs = np.array([[-2.80892642e-01,7.20543846e-02,-1.77783135e-04,-9.27152558e-04,-7.49371778e-03]])
nK, _ = cv2.getOptimalNewCameraMatrix(K, dist_coeffs, (540,960), alpha=1)

y_cut = 270	# Recorte vertical de la imagen
x_tras = 228	# Traslacion para recortar la imagen sin distorcion

# Adquiere la imagen
imagen0 = cv2.imread('image_960_540_r.png')									
# Segmenta la imagen
imagenSeg =seg_img(imagen0,y_cut)	
# Obtiene los pixeles blancos y les aplica quita la distorcion radial y tangencial, y aplica la homografia
list_px = get_list(imagenSeg,y_cut,x_tras,K,dist_coeffs,nK) 
# Le aplica RANSAC a los puntos y los separa en grupos
# El eje vertical de la imagen es el eje x
# El eje horizontal de la imagen es el eje y
M, B, R, Y0 = get_lines(list_px) 														
print('M ',M)
print('B ',B)
print('R ',R)
print('Y0 ',Y0)

l = 200 #[cm]
Pd, Pc, Pi = seg_lines(Y0,M,B,R,l)
x1_d,y1_d,x2_d,y2_d = Pd
x1_c,y1_c,x2_c,y2_c = Pc
x1_i,y1_i,x2_i,y2_i = Pi
print(Pd)
print(Pc)
print(Pi)

imagenH = cv2.imread('homography_960_540_r.png')
print(imagenSeg.shape)
h,w = imagenSeg.shape
#imagenH = np.zeros((300,300,3))
for x,y in list_px:	imagenR = cv2.circle(imagenH, (int(x), int(y)), 1, (0, 255, 0), -1)
imagenR =cv2.line(imagenR, (y2_d,x2_d),(y1_d,x1_d), (255,0,0), 2)
imagenR =cv2.line(imagenR, (y2_i,x2_i),(y1_i,x1_i), (0,0,255), 2)
imagenR =cv2.line(imagenR, (y2_c,x2_c),(y1_c,x1_c), (255,255,255), 2)


cv2.imshow('original',imagen0)
cv2.imshow('homography',imagenR)
cv2.waitKey(0)
cv2.imwrite('homography_960_540_FINAL_mask2.png',imagenR)
cv2.destroyAllWindows()







