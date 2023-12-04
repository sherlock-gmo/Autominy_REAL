import csv
import numpy as np
import matplotlib.pyplot as plt

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
			#Sgamma.append(float(ROWS[1]))
			#Mgamma.append(float(ROWS[2]))
			Sgamma.append(float(ROWS[2]))
			Mgamma.append(float(ROWS[3]))
		N = len(T)
		T = np.reshape(np.array(T).T,(N,1))
		Sgamma = np.reshape(np.array(Sgamma).T,(N,1))
		Mgamma = np.reshape(np.array(Mgamma).T,(N,1))
	return T, Sgamma, Mgamma
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
# Modelo del servomotor
def f1(M1,M2):
	return M2
def f2(P,S,M1,M2):
	a1,a2,b,c,d = P
	if (abs(M2)>0.0): sDM = M2/abs(M2)
	else: sDM = 0.0
	DM2 = (-a1)*M2+(-a2)*M1-c*sDM+b*S+d
	return DM2
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
def runge_kutta04_2ord(P, S, M20, M10, h):
	k1 = h * f1(M10, M20)
	l1 = h * f2(P, S, M10, M20)
	k2 = h * f1(M10 + k1/2, M20 + l1/2)
	l2 = h * f2(P, S, M10 + k1/2, M20 + l1/2)
	k3 = h * f1(M10 + k2/2, M20 + l2/2)
	l3 = h * f2(P, S, M10 + k2/2, M20 + l2/2)
	k4 = h * f1(M10 + k3, M20 + l3)
	l4 = h * f2(P, S, M10 + k3, M20 + l3)
	M1 = M10 + (k1 + 2*k2 + 2*k3 + k4) / 6
	M2 = M20 + (l1 + 2*l2 + 2*l3 + l4) / 6
	return M2, M1
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#path = '/home/ros/Autominy_REAL/autominy_ws/src/dotmex_final/calibration/servomotor/'
path = '/home/sherlock2204f/Autominy_REAL/autominy_ws/src/dotmex_final/calibration/servomotor/'
#file_csv = '/data/sensors_servo_test_275.csv'
file_csv = 'servo_bag3.csv'
T,S_gamma,M_gamma = get_data(path,file_csv)		# Vector de las mediciones realizadas
T = T-T[0] # Para medir desde el segundo cero

"""
States = np.load('states_ex.npy')
#print(States.shape)
T = States[:,0]
S_gamma = States[:,1]
M_gamma = States[:,2]
DM_gamma = States[:,3]
"""

# Parametros del predictor
h = 0.01
N = T.shape
N = N[0]
E = np.zeros((N,1))
M_pred = np.zeros((N,1))
DM_pred = np.zeros((N,1))
11.8, 107.7, 41.2, 1.2, -2.6
a1 = 11.8 #6.39611649
a2 = 107.7 #113.79916073
c = 1.2 #0.39086748
b = 41.2 #39.96355628
d = -2.6 #1.02886988
P = [a1,a2,b,c,d]
M10 = M_pred[0]
M20 = DM_pred[0]

for i in range(1,N):
	M2, M1 = runge_kutta04_2ord(P, S_gamma[i], M20, M10, h)
	M20 = M2
	M10 = M1
	M_pred[i] = M1 
	DM_pred[i] = M2
	E[i] = M_gamma[i]-M_pred[i]

plot1 = plt.figure(1)
plt.plot(T,S_gamma,'k',T,M_gamma,'r',T,M_pred,'b')
plt.xlabel('t [s]')
plt.legend(["S_gamma","M_gamma","M_pred"])
plt.grid()
"""
plot2 = plt.figure(2)
plt.plot(T,DM_gamma,'r',T,DM_pred,'g')
plt.xlabel('t [s]')
plt.legend(["DM_gamma","DM_pred"])
plt.grid()
"""
plot3 = plt.figure(3)
plt.plot(T,E,'b')
plt.xlabel('t [s]')
plt.legend(["e"])
plt.grid()

plt.show()
