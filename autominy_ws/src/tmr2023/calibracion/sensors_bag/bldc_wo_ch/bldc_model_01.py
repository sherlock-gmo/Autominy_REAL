import csv
import numpy as np
import matplotlib.pyplot as plt

path = '/home/sherlock/dotMEX_Autominy_REAL/autominy_ws/src/dotmex2022/calibration/sensors_bag/bldc_wo_ch/'
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
def gen_vec(file_csv):
	T = []
	S_omega = []
	M_omega = []
	with open(path+file_csv, 'r') as datafile:
		ploting = csv.reader(datafile, delimiter='	',quoting=csv.QUOTE_NONNUMERIC)
		for ROWS in ploting:
			T.append(ROWS[0])
			S_omega.append(ROWS[1])
			M_omega.append(ROWS[2])
	return np.array(T),np.array(S_omega),np.array(M_omega)
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
file_data = 'sensors_bldc_test_300.csv'
T,S_omega,M_omega= gen_vec(file_data)

t = T-T[0]
xmax= int(t[-1])+1

fc = 47.7465
wc = 2*np.pi*fc
N = t.shape
D = np.zeros((N[0]))
DD = np.zeros((N[0]))
for i in range(1,N[0]):
	h = t[i]-t[i-1]
	D[i] = (1.0/(1.0+h*wc))*(wc*(M_omega[i]-M_omega[i-1])+D[i-1]) #D=(wc*s/s+wc)(M_omega)
	#D[i] = (1.0/h)*(M_omega[i]-M_omega[i-1]) #D=(s)(M_omega)
	DD[i] = (1/h)*(D[i]-D[i-1]) #DD = sD

A = np.transpose(np.array([D, M_omega, S_omega]))
DD = DD.reshape((N[0],1))
P = np.linalg.inv(np.matmul(A.T,A))
Q = np.matmul(P,A.T)
v,_ = np.linalg.eig(np.matmul(A.T,A))
theta = np.matmul(Q,DD)

print('lambda ',v.max()/v.min())
print('theta ',theta)

"""
plt.plot(t,M_omega,'r')
plt.title('Speed')
plt.xlabel('t [s]')
plt.xlim([0,xmax])
plt.legend(["M_omega"])
plt.grid()
plt.show()
"""
