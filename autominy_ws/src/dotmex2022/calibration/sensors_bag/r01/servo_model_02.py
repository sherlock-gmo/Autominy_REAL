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
	S_gamma = []
	M_gamma = []
	with open(path+file_csv, 'r') as datafile:
		ploting = csv.reader(datafile, delimiter=' ',quoting=csv.QUOTE_NONNUMERIC)
		for ROWS in ploting:
			T.append(ROWS[0])
			S_gamma.append(ROWS[8])
			M_gamma.append(ROWS[11])
	return np.array(T),np.array(S_gamma),np.array(M_gamma)
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
file_data = 'sensors_bag_225.csv'
T,S_gamma,M_gamma= gen_vec(file_data)

t = T-T[0]
M_gamma_N = (1.0/0.3508)*M_gamma
xmax= 26

a = 5.9649
b = 2.3134
fc = 47.7465
wc = 2*np.pi*fc
N = t.shape
M = np.zeros((N[0]))
for i in range(1,N[0]): #2
	h = t[i]-t[i-1]
	M[i] = (1.0/(1.0+a*h))*(M[i-1]+b*h*S_gamma[i]) #1er Orden
	#M[i] = (1.0/(1.0+a*h+b*(h**2)))*((2+a*h)*M[i-1]-M[i-2]+b*(h**2)*S_gamma[i]) #2do Orden

plt.plot(t,M_gamma,'r',t,M,'g')
plt.title('Steering')
plt.xlabel('t [s]')
plt.xlim([0,xmax])
plt.legend(["M_gamma", "M_model"])
plt.grid()
plt.show()
	


"""
plt.plot(t,S_gamma,'b',t,M_gamma_N,'r')
plt.title('Steering')
plt.xlabel('t [s]')
plt.xlim([0,xmax])
plt.legend(["S_gamma", "M_gamma"])
plt.grid()
plt.show()
"""
