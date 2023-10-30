import csv
import numpy as np
from scipy.linalg import solve_continuous_lyapunov as lyp
import matplotlib.pyplot as plt

path = '/home/sherlock2204f/Autominy_REAL/autominy_ws/src/dotmex_final/calibration/servomotor/data/'
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
def gen_vec(file_csv):
	T = []
	S_gamma = []
	M_gamma = []
	DM_gamma = []
	with open(path+file_csv, 'r') as datafile:
		ploting = csv.reader(datafile, delimiter='	',quoting=csv.QUOTE_NONNUMERIC)
		for ROWS in ploting:
			T.append(ROWS[0])
			S_gamma.append(ROWS[1])
			M_gamma.append(ROWS[2])
			DM_gamma.append(ROWS[3])
	N,_ = T.shape
	T = np.reshape(np.array(T).T,(N,1))
	S_gamma = np.reshape(np.array(S_gamma).T,(N,1))
	M_gamma = np.reshape(np.array(M_gamma).T,(N,1))
	DM_gamma = np.reshape(np.array(DM_gamma).T,(N,1))
	return T, S_gamma, M_gamma, DM_gamma
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
#file_data = 'sensors_servo_5.csv'
#file_data = 'sensors_servo_3.csv'

States = np.load('states.npy')
print(States.shape)
T = States[:,0]
S_gamma = States[:,1]
M_gamma = States[:,2]
DM_gamma = States[:,3]

#T,S_gamma,M_gamma,DM_gamma= gen_vec(file_data)
t = T-T[0]

h = 0.01
xmax= int(t[-1])+1

# 																		PREDICTORS
N = t.shape
alpha = 100.0 #100.0

gamma1 = 100.0
gamma2 = 200.0

M_hat = np.zeros((N[0]))
DM_hat = np.zeros((N[0]))
E = np.zeros((N[0]))

a_hat = np.zeros((N[0]))
b_hat = np.zeros((N[0]))
a_hat[0] = 2.5
b_hat[0] = 0.9


M_pred = np.zeros((N[0]))
e = -M_gamma[0]
for i in range(1,N[0]):
	M_hat[i] = (1-alpha*h)*M_hat[i-1]+h*((alpha-a_hat[i])*M_gamma[i]+b_hat[i]*S_gamma[i])
	e = M_hat[i]-M_gamma[i]
	a_hat[i] = a_hat[i-1]+h*gamma1*e*M_gamma[i]
	b_hat[i] = b_hat[i-1]-h*gamma2*e*S_gamma[i]


for i in range(1,N[0]):
	M_pred[i] = (1-a_hat[-1]*h)*M_pred[i-1]+h*b_hat[-1]*S_gamma[i]



print('e ',e)
print('a_hat, b_hat ',a_hat[-1],b_hat[-1])


plot1 = plt.figure(1)
plt.plot(t,M_gamma,'r',t,M_pred,'g')
plt.xlabel('t [s]')
plt.xlim([0,xmax])
plt.legend(["M_gamma","M_pred"])
plt.grid()


plot2 = plt.figure(2)
plt.plot(t,a_hat,'r',t,b_hat,'b')
plt.xlabel('t [s]')
plt.legend(["a_hat","b_hat"])
plt.grid()


plt.show()
