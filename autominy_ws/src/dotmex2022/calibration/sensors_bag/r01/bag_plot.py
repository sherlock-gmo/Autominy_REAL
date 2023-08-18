import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

path = '/home/sherlock/dotMEX_Autominy_REAL/autominy_ws/src/dotmex2022/calibration/sensors_bag/r01/'
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
def gen_vec(file_csv):
	T = []
	S_Omega = []
	M_Omega = []
	S_gamma = []
	M_gamma = []
	with open(path+file_csv, 'r') as datafile:
		ploting = csv.reader(datafile, delimiter=' ',quoting=csv.QUOTE_NONNUMERIC)
		for ROWS in ploting:
			#print(ROWS)
			T.append(ROWS[0])
			S_Omega.append(ROWS[2])
			M_Omega.append(ROWS[5])
			S_gamma.append(ROWS[8])
			M_gamma.append(ROWS[11])
	return np.array(T),np.array(S_Omega,dtype=float),np.array(M_Omega,dtype=float),np.array(S_gamma),np.array(M_gamma)
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
file_data = 'sensors_bag_300.csv'
T,S_Omega,M_Omega,S_gamma,M_gamma= gen_vec(file_data)

t = T-T[0]
S_Omega_N = (1.0/1000.0)*S_Omega
M_Omega_N = (1.0/5.0)*M_Omega
xmax= 13

plt.subplot(211)
plt.plot(t,S_Omega_N,'b',t,M_Omega_N,'r')
plt.title('Speed')
plt.xlabel('t [s]')
plt.xlim([0,xmax])
plt.legend(["S_Omega_N", "M_Omega_N"])
plt.grid()

plt.subplot(212)
plt.plot(t,S_gamma,'b',t,M_gamma,'r')
plt.title('Steering')
plt.xlabel('t [s]')
plt.xlim([0,xmax])
plt.legend(["S_gamma", "M_gamma"])

plt.grid()
plt.show()

