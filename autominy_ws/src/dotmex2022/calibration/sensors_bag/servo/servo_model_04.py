import csv
import numpy as np
from scipy.linalg import solve_continuous_lyapunov as lyp

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
file_data = 'sensors_servo_5.csv'
T,S_gamma,M_gamma= gen_vec(file_data)

t = T-T[0]
xmax= int(t[-1])+1

# 																		PREDICTORS
N = t.shape
fc = 47.7465
wc = 2*np.pi*fc

alpha = 100.0 #100.0
beta = 50.0 #50.0
A = np.array([[0.0,1.0],[-beta,-alpha]])
Q = 1.0*np.array([[1.0,0.0],[0.0,2.0]])
#P = lyp(A,Q)
P = lyp(np.transpose(A),Q)
p2 = P[0][1]
p3 = P[1][1]

gamma1 = 1.0
gamma2 = 2.0 
gamma3 = 3.0 
D = np.zeros((N[0]))
M_hat = np.zeros((N[0]))
E = np.zeros((N[0]))
a_hat = np.zeros((N[0]))
b_hat = np.zeros((N[0]))
c_hat = np.zeros((N[0]))
a_hat[0] = 0.01 #1.0
b_hat[0] = 0.01 #1.0
c_hat[0] = 0.01 #1.0

for i in range(1,N[0]):
	h = t[i]-t[i-1]
	D[i] = (1.0/(1.0+h*wc))*(wc*(M_gamma[i]-M_gamma[i-1])+D[i-1]) #D = (wc*s/s+wc)M_gamma
	#D[i] = (M_gamma[i]-M_gamma[i-1])/h #D = sM_gamma

e1 = 1.0
p = 0
while (abs(e1)>0.001):
	for i in range(2,N[0]):
		h = t[i]-t[i-1]
		M_hat[i] = (1.0/(1.0+alpha*h+beta*h**2))*((h**2)*((alpha-a_hat[i])*D[i]+(beta-b_hat[i])*M_gamma[i]+c_hat[i]*S_gamma[i])+(2+alpha*h)*M_hat[i-1]-M_hat[i-2])
		e1 = M_hat[i]-M_gamma[i]
		e2 = ((M_hat[i]-M_hat[i-1])/h)-D[i]
		a_hat[i] = a_hat[i-1]+h*gamma1*(p2*e1+p3*e2)*D[i]
		b_hat[i] = b_hat[i-1]+h*gamma2*(p2*e1+p3*e2)*M_gamma[i]
		c_hat[i] = c_hat[i-1]-h*gamma3*(p2*e1+p3*e2)*S_gamma[i]
		#E[i] = -alpha*e2-beta*e2

	print(p)
	a_hat[0] = a_hat[-1]
	b_hat[0] = b_hat[-1]
	c_hat[0] = c_hat[-1]
	p = p+1
	if (p>=500): break

print('a_hat, b_hat, c_hat ',a_hat[-1],b_hat[-1],c_hat[-1])
print('e ',e1)

#plt.plot(t,M_gamma,'r',t,M_hat,'g')
plt.plot(t,a_hat,'r',t,b_hat,'g',t,c_hat,'b')
#plt.plot(t,E,'k')
plt.title('Steering')
plt.xlabel('t [s]')
plt.xlim([0,xmax])
#plt.ylim([-1,1])
plt.legend(["M_gamma","M_hat"])
plt.grid()
plt.show()
