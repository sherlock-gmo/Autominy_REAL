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
beta = 50.0 #50.0

A = np.array([[0.0,1.0],[-beta,-alpha]])
Q = 1.0*np.array([[1.0,0.0],[0.0,2.0]])
#P = lyp(A,Q)
P = lyp(np.transpose(A),Q)
p2 = P[0][1]
p3 = P[1][1]

gamma1 = 10.0
gamma2 = 20.0
gamma3 = 40.0
D = np.zeros((N[0]))
M_hat = np.zeros((N[0]))
DM_hat = np.zeros((N[0]))
E = np.zeros((N[0]))
a_hat = np.zeros((N[0]))
b_hat = np.zeros((N[0]))
c_hat = np.zeros((N[0]))
a_hat[0] = 0.01
b_hat[0] = 0.01
c_hat[0] = 0.01

M_pred = np.zeros((N[0]))

"""
for i in range(1,N[0]):
	h = t[i]-t[i-1]
	D[i] = (1.0/(1.0+h*wc))*(wc*(M_gamma[i]-M_gamma[i-1])+D[i-1]) #D = (wc*s/s+wc)M_gamma
	#D[i] = (M_gamma[i]-M_gamma[i-1])/h #D = sM_gamma
"""
alpha2 = 100.0
alpha1 = 100.0
e1 = -M_gamma[0]
e2 = -DM_gamma[0]
for i in range(1,N[0]):
	#h = t[i]-t[i-1]
	#M_hat[i] = (1.0/(1.0+alpha*h+beta*h**2))*((h**2)*((alpha-a_hat[i])*DM_gamma[i]+(beta-b_hat[i])*M_gamma[i]+c_hat[i]*S_gamma[i])+(2+alpha*h)*M_hat[i-1]-M_hat[i-2])
	#M_hat[i] = 2*M_hat[i-1]-M_hat[i-2]+(-a_hat[i]*DM_gamma[i]-b_hat[i]*M_gamma[i]+c_hat[i]*S_gamma[i]-alpha2*e2-alpha1*e1)*h**2	

	DM_hat[i] = DM_hat[i-1]+h*(-a_hat[i]*DM_gamma[i]-b_hat[i]*M_gamma[i]+c_hat[i]*S_gamma[i]-alpha2*e2-alpha1*e1)
	M_hat[i] = M_hat[i-1]+h*DM_hat[i] 
	
	e1 = M_hat[i]-M_gamma[i]
	e2 = DM_hat[i]-DM_gamma[i]
	#a_hat[i] = a_hat[i-1]+h*gamma1*(p2*e1+p3*e2)*DM_gamma[i]
	#b_hat[i] = b_hat[i-1]+h*gamma2*(p2*e1+p3*e2)*M_gamma[i]
	#c_hat[i] = c_hat[i-1]-h*gamma3*(p2*e1+p3*e2)*S_gamma[i]

	a_hat[i] = a_hat[i-1]+h*gamma1*(e2)*DM_gamma[i]
	b_hat[i] = b_hat[i-1]+h*gamma2*(e2)*M_gamma[i]
	c_hat[i] = c_hat[i-1]-h*gamma3*(e2)*S_gamma[i]

for i in range(2,N[0]):
	M_pred[i] = (1.0/(1.0+alpha*h+beta*h**2))*((h**2)*((alpha-a_hat[-1])*DM_gamma[i]+(beta-b_hat[-1])*M_gamma[i]+c_hat[-1]*S_gamma[i])+(2+alpha*h)*M_pred[i-1]-M_pred[i-2])

	#E[i] = -alpha*e2-beta*e2
	#print('a_hat, b_hat, c_hat ',a_hat[i],b_hat[i],c_hat[i])

print('e ',e1)
print('a_hat, b_hat, c_hat ',a_hat[-1],b_hat[-1],c_hat[-1])


plot1 = plt.figure(1)
#plt.plot(t,M_gamma,'r',t,M_hat,'g')
plt.plot(t,M_gamma,'r',t,M_pred,'g')
#plt.plot(t,a_hat,'r',t,b_hat,'g',t,c_hat,'b')
#plt.plot(t,E,'k')
plt.title('Steering')
plt.xlabel('t [s]')
plt.xlim([0,xmax])
#plt.ylim([-1,1])
plt.legend(["M_gamma","M_hat"])
plt.grid()


plot2 = plt.figure(2)
plt.plot(t,a_hat,'r',t,b_hat,'g',t,c_hat,'b')
plt.xlabel('t [s]')
#plt.xlim([0,xmax])
plt.legend(["a_hat","b_hat","c_hat"])
plt.grid()


plt.show()
