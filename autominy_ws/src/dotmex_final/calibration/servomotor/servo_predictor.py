import csv
import numpy as np
from scipy.linalg import solve_continuous_lyapunov as lyp
import matplotlib.pyplot as plt

States = np.load('states.npy')
print(States.shape)
T = States[:,0]
S_gamma = States[:,1]
M_gamma = States[:,2]
DM_gamma = States[:,3]

t = T-T[0]
h = 0.01
#xmax= int(t[-1])+1

# 																		PREDICTORS
N = t.shape
gamma1 = 100.0
gamma2 = 200.0
gamma3 = 400.0

#D = np.zeros((N[0]))
M_hat = np.zeros((N[0]))
DM_hat = np.zeros((N[0]))
#E = np.zeros((N[0]))
a1_hat = np.zeros((N[0]))
a2_hat = np.zeros((N[0]))
b_hat = np.zeros((N[0]))
a1_hat[0] = 5.0
a2_hat[0] = 5.0
b_hat[0] = 5.0

M_pred = np.zeros((N[0]))

alpha1 = 1250.0
alpha2 = 75.0

e1 = -M_gamma[0]
e2 = -DM_gamma[0]

for i in range(1,N[0]):
	#h = t[i]-t[i-1]
	DM_hat[i] = DM_hat[i]+h*((alpha2-a1_hat[i])*DM_gamma[i]+(alpha1-a2_hat[i])*M_gamma[i]+b_hat[i]*S_gamma[i]-alpha2*DM_hat[i]-alpha1*M_hat[i])
	M_hat[i] = M_hat[i]+h*DM_hat[i] 
	e1 = M_hat[i]-M_gamma[i]
	e2 = DM_hat[i]-DM_gamma[i]
	a1_hat[i] = a1_hat[i-1]+h*gamma1*(e2)*DM_gamma[i]
	a2_hat[i] = a2_hat[i-1]+h*gamma2*(e2)*M_gamma[i]
	b_hat[i] = b_hat[i-1]-h*gamma3*(e2)*S_gamma[i]

for i in range(1,N[0]):
	M_pred[i] = (2-h*a1_hat[-1]-(h**2)*a2_hat[-1])*M_pred[i]+(h*a1_hat[-1]-1)*M_pred[i-1]+b_hat[-1]*(h**2)*S_gamma[i]

print('e ',e1)
print('a1_hat, a2_hat, b_hat ',a1_hat[-1],a2_hat[-1],b_hat[-1])


plot1 = plt.figure(1)
#plt.plot(t,M_gamma,'r',t,M_hat,'g')
plt.plot(t,M_gamma,'r',t,M_pred,'g')
#plt.plot(t,a_hat,'r',t,b_hat,'g',t,c_hat,'b')
#plt.plot(t,E,'k')
plt.title('Steering')
plt.xlabel('t [s]')
#plt.xlim([0,xmax])
#plt.ylim([-1,1])
plt.legend(["M_gamma","M_hat"])
plt.grid()


plot2 = plt.figure(2)
plt.plot(t,a1_hat,'r',t,a2_hat,'g',t,b_hat,'b')
plt.xlabel('t [s]')
#plt.xlim([0,xmax])
plt.legend(["a1_hat","a2_hat","b_hat"])
plt.grid()


plt.show()
