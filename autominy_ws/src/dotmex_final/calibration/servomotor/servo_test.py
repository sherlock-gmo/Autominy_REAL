import csv
import numpy as np
from scipy.linalg import solve_continuous_lyapunov as lyp
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
			Sgamma.append(float(ROWS[1]))
			Mgamma.append(float(ROWS[2]))
		N = len(T)
		T = np.reshape(np.array(T).T,(N,1))
		Sgamma = np.reshape(np.array(Sgamma).T,(N,1))
		Mgamma = np.reshape(np.array(Mgamma).T,(N,1))
	return T, Sgamma, Mgamma, N
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************

# Mediciones de la posición del auto
path = '/home/sherlock2204f/Autominy_REAL/autominy_ws/src/dotmex_final/calibration/servomotor/data/'
file_csv = 'sensors_servo_test_175.csv'
T,S_gamma,M_gamma,N = get_data(path,file_csv)

# Parametros del modelo
h = 0.01											# Periodo de muestreo [s]
a1 = 19.032740012596516
a2 = 147.17125360229312
b = 22.604313181810728
c = -0.5623202467002375
d = 0.9664690408863311

E = np.zeros((N,1))
M_pred = np.zeros((N,1))
DM_pred = np.zeros((N,1))
signDM = 0.0
signDM_h = 0.0
for i in range(1,N):
	DDM_pred = -a1*DM_pred[i]-a2*M_pred[i]-c*signDM+b*S_gamma[i]+d 
	DDM_pred_h = -a1*DM_pred[i-1]-a2*M_pred[i-1]-c*signDM_h+b*S_gamma[i-1]+d 
	DM_pred[i] = DM_pred[i-1]+(h/2.0)*(DDM_pred+DDM_pred_h)
	M_pred[i] = M_pred[i-1]+(h/2.0)*(DM_pred[i]+DM_pred[i-1])
	E[i] = M_gamma[i]-M_pred[i]
	if (abs(DM_pred[i])>0.0):
		signDM = DM_pred[i]/abs(DM_pred[i])
	else:
		signDM = 0.0
	if (abs(DM_pred[i-1])>0.0):
		signDM_h = DM_pred[i-1]/abs(DM_pred[i-1])
	else:
		signDM_h = 0.0

plot1 = plt.figure(1)
plt.plot(T,S_gamma,'k',T,M_gamma,'r',T,M_pred,'b')
plt.xlabel('t [s]')
plt.legend(["S_gamma","M_gamma","M_pred","M_hat"])
plt.grid()

plot3 = plt.figure(3)
plt.plot(T,E,'b')
plt.xlabel('t [s]')
plt.legend(["e"])
plt.grid()

plt.show()
