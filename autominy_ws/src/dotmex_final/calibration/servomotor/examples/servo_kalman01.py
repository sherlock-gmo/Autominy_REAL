import csv
import numpy as np
import matplotlib.pyplot as plt
from lib_kalman_01 import linear_kalman_filter

Kalman = linear_kalman_filter()

#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
def get_data(path,file_csv):
	T = []
	Sgamma = []
	Mgamma = []
	with open(path+file_csv, 'r') as datafile:
		ploting = csv.reader(datafile, delimiter='\t')
		for ROWS in ploting:
			T.append(float(ROWS[0]))
			Sgamma.append(float(ROWS[1]))
			Mgamma.append(float(ROWS[2]))
		N = len(T)
		T = np.reshape(np.array(T).T,(N,1))
		Sgamma = np.reshape(np.array(Sgamma).T,(N,1))
		Mgamma = np.reshape(np.array(Mgamma).T,(N,1))
	return T, Sgamma, Mgamma
#**************************************************************************************************
# Calculo de la matriz de transicion de estados
def F_calc(c,a2,k,h):
	F11 = np.exp(c*h)*(np.cos(k*h)-(c/k)*np.sin(k*h))
	F12 = (1/k)*np.exp(c*h)*np.sin(k*h)
	F21 = (-a2/k)*np.exp(c*h)*np.sin(k*h)
	F22 = np.exp(c*h)*(np.cos(k*h)+(c/k)*np.sin(k*h))
	F = np.array([[F11,F12],[F21,F22]])
	return F
#**************************************************************************************************
# Calculo de la matriz Bd
def Bd_calc(b,c,k,h):
	Bd1 = (b/(k*(c**2+k**2)))*(np.exp(c*h)*(c*np.sin(k*h)-k*np.cos(k*h))+k)
	Bd2 = (b/(c**2+k**2))*(np.exp(c*h)*(k*np.sin(k*h)+c*np.cos(k*h))-c)+((b*c)/(k*(c**2+k**2)))*(np.exp(c*h)*(c*np.sin(k*h)-k*np.cos(k*h))+k)
	Bd = np.array([[Bd1],[Bd2]])
	return Bd
#**************************************************************************************************
# Calculo de la matriz de ruido Q
def Q_calc(sigma_Mgamma,h):
	Q = (sigma_Mgamma**2)*np.array([[1, 1/h],[1/h, 1/(h**2)]])
	return Q
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************

#****************************************************************PARAMETROS INICIALES
# Mediciones de la posición del auto
path = '/home/sherlock2204f/Autominy_REAL/autominy_ws/src/dotmex_final/calibration/servomotor/data/'
file_csv = 'sensors_servo_test_200.csv'

# Parametros del filtro
h = 0.01											# Periodo de muestreo [s]
sigma_Mgamma = 0.0000001			# Des. Est. de la medición de la posicion del servomotor
# Parametros del modelo
b = 2.0
a1 = 15.0
a2 = 150.0
# Parametros auxiliares
c = -a1/2.0
k = np.sqrt(a2-(a1**2/4.0))
# Matrices para el filtro de Kalman
F = F_calc(c,a2,k,h)
Bd = Bd_calc(b,c,k,h)
Q = Q_calc(sigma_Mgamma,h)
R = np.array([[sigma_Mgamma**2]]) # Si es un escalar, definirlo como matriz de 1x1
H = np.array([[1, 0]])
T,S_gamma,M_gamma = get_data(path,file_csv)		# Vector de las mediciones realizadas
T = T-T[0] # Para medir desde el segundo cero
#*********************************INICIO DEL CICLO*********************************
# Inicializacion
X0 = np.array([0.0,0.0])		# Estado inicial
X0 = np.reshape(X0,(2,1))
P0 = np.diag((0.1,0.1))
# Algoritmo de Kalman
Xk = Kalman.alg_kalman_offline(X0,P0,F,Bd,S_gamma,H,R,Q,M_gamma)
# Guardado de datos
states = np.concatenate((T,S_gamma),axis=1)
states = np.concatenate((states,Xk[:,0]),axis=1)
states = np.concatenate((states,Xk[:,1]),axis=1)
np.save('states.npy', states)
print(states.shape)

# Coparacion con la derivada numerica y el filtro pasa-altos
Dn = []
Df = []
N,_ = T.shape
fc = 47.7465
wc = 2*np.pi*fc
df0 = 0.0
for i in range (0,N):
	df = (1.0/(1.0+h*wc))*(wc*(M_gamma[i]-M_gamma[i-1])+df0) #D = (wc*s/s+wc)M_gamma
	dn = (M_gamma[i]-M_gamma[i-1])/h 
	df0 = df
	Dn.append(dn)
	Df.append(df)
Dn = np.array(Dn)
Df = np.array(Df)


# Graficas
plot1 = plt.figure(1)
plt.plot(T,M_gamma,'r-',T,Xk[:,0],'bo')
plt.xlabel('[s]')
plt.ylabel('M_gamma')
plt.legend(['mediciones','actualizaciones'])
plt.grid()

plot2 = plt.figure(2)
plt.plot(T,Xk[:,0],'r',T,Xk[:,1],'b')
plt.xlabel('[s]')
plt.legend(['M_gamma','DM_gamma'])
plt.grid()

plot3 = plt.figure(3)
plt.plot(T[1:],Xk[1:,1],'b',T,Dn,'r',T,Df,'y')
plt.xlabel('[s]')
plt.legend(['DM_gamma','Dnum_gamma','Df_gamma'])
plt.grid()

plt.show()
