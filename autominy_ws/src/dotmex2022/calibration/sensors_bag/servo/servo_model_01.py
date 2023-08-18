import csv
import numpy as np
import matplotlib.pyplot as plt

path = '/home/sherlock/dotMEX_Autominy_REAL/autominy_ws/src/dotmex2022/calibration/sensors_bag/servo/'
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
def gen_vec(file_csv):
	T = []
	S_gamma = []
	M_gamma = []
	with open(path+file_csv, 'r') as datafile:
		ploting = csv.reader(datafile, delimiter='	',quoting=csv.QUOTE_NONNUMERIC)
		for ROWS in ploting:
			T.append(ROWS[0])
			S_gamma.append(ROWS[1])
			M_gamma.append(ROWS[2])
	return np.array(T),np.array(S_gamma),np.array(M_gamma)
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
file_data = 'sensors_servo_test_250.csv'
T,S_gamma,M_gamma= gen_vec(file_data)

t = T-T[0]
xmax= int(t[-1])+1

fc = 47.7465
wc = 2*np.pi*fc
N = t.shape
D = np.zeros((N[0]))
DD = np.zeros((N[0]))
for i in range(1,N[0]):
	h = t[i]-t[i-1]
	D[i] = (1.0/(1.0+h*wc))*(wc*(M_gamma[i]-M_gamma[i-1])+D[i-1]) #D = (wc*s/s+wc)M_gamma
	#DD[i] = (1.0/(1.0+h*wc))*(wc*(D[i]-D[i-1])+DD[i-1]) #DD = (wc*s/s+wc)D
	DD[i] = (1/h)*(D[i]-D[i-1]) #DD = sD


A = np.transpose(np.array([D,M_gamma,S_gamma]))
#print(A[0,:])
DD = DD.reshape((N[0],1))
P = np.linalg.inv(np.matmul(A.T,A))
Q = np.matmul(P,A.T)
theta = np.matmul(Q,DD)
v,_ = np.linalg.eig(np.matmul(A.T,A))
print('lamda ',v.max()/v.min())
print('theta ',theta)

"""
plt.plot(t,M_gamma,'r')
plt.title('Steering')
plt.xlabel('t [s]')
plt.xlim([0,xmax])
plt.legend(["M_gamma"])
plt.grid()
plt.show()
"""

