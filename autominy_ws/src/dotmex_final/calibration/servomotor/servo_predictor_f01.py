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

a1_hat = np.zeros((N[0]))
a2_hat = np.zeros((N[0]))
b_hat = np.zeros((N[0]))
a1_hat[0] = 5.0
a2_hat[0] = 5.0
b_hat[0] = 5.0

alpha1 = 1250.0
alpha2 = 75.0

e1 = -M_gamma[0]
e2 = -DM_gamma[0]
E = []
M_hat = np.zeros((N[0]))
DM_hat = np.zeros((N[0]))
for i in range(1,N[0]):
	#h = t[i]-t[i-1]
	#DDM_hat = (alpha2-a1_hat[i])*DM_gamma[i]+(alpha1-a2_hat[i])*M_gamma[i]+b_hat[i]*S_gamma[i]-alpha2*DM_hat[i]-alpha1*M_hat[i]

	e1 = M_hat[i]-M_gamma[i]
	e2 = DM_hat[i]-DM_gamma[i]
	e1_h = M_hat[i-1]-M_gamma[i-1]
	e2_h = DM_hat[i-1]-DM_gamma[i-1]
	DDM_hat = -a1_hat[i]*DM_gamma[i]-a2_hat[i]*M_gamma[i]+b_hat[i]*S_gamma[i]-alpha2*e2-alpha1*e1
	DDM_hat_h = -a1_hat[i-1]*DM_gamma[i-1]-a2_hat[i-1]*M_gamma[i-1]+b_hat[i-1]*S_gamma[i-1]-alpha2*e2_h-alpha1*e1_h
	
	DM_hat[i] = DM_hat[i-1]+(h/2.0)*(DDM_hat+DDM_hat_h)
	M_hat[i] = M_hat[i-1]+(h/2.0)*(DM_hat[i]+DM_hat[i-1])
	e1 = M_hat[i]-M_gamma[i]
	e2 = DM_hat[i]-DM_gamma[i]
	"""
	a1_hat[i] = a1_hat[i]+h*gamma1*(e2)*DM_gamma[i]
	a2_hat[i] = a2_hat[i]+h*gamma2*(e2)*M_gamma[i]
	b_hat[i] = b_hat[i]-h*gamma3*(e2)*S_gamma[i]
	"""
	Da1_hat = gamma1*(e2)*DM_gamma[i]
	Da1_hat_h = gamma1*(e2_h)*DM_gamma[i-1]
	a1_hat[i] = a1_hat[i-1]+(h/2.0)*(Da1_hat+Da1_hat_h)
	Da2_hat = gamma2*(e2)*M_gamma[i]
	Da2_hat_h = gamma2*(e2_h)*M_gamma[i-1]
	a2_hat[i] = a2_hat[i-1]+(h/2.0)*(Da2_hat+Da2_hat_h)
	Db_hat = -gamma3*(e2)*S_gamma[i]
	Db_hat_h = -gamma3*(e2_h)*S_gamma[i-1]
	b_hat[i] = b_hat[i-1]+(h/2.0)*(Db_hat+Db_hat_h)
	
	E.append(e1)

M_pred = np.zeros((N[0]))
DM_pred = np.zeros((N[0]))
for i in range(1,N[0]):
	DDM_pred = -a1_hat[-1]*DM_pred[i]-a2_hat[-1]*M_pred[i]+b_hat[-1]*S_gamma[i]
	DDM_pred_h = -a1_hat[-1]*DM_pred[i-1]-a2_hat[-1]*M_pred[i-1]+b_hat[-1]*S_gamma[i-1]
	#DDM_pred = -15.0*DM_pred[i]-150.0*M_pred[i]+2.0*S_gamma[i]
	#DDM_pred_h = -15.0*DM_pred[i-1]-150.0*M_pred[i-1]+2.0*S_gamma[i-1]
	DM_pred[i] = DM_pred[i-1]+(h/2.0)*(DDM_pred+DDM_pred_h)
	M_pred[i] = M_pred[i-1]+h*DM_pred[i]

print('e ',e1)
print('a1_hat, a2_hat, b_hat ',a1_hat[-1],a2_hat[-1],b_hat[-1])


plot1 = plt.figure(1)
#plt.plot(t,M_gamma,'r',t,M_hat,'g')
plt.plot(t,M_gamma,'r',t,M_pred,'g',t,M_hat,'b')
#plt.plot(t,a_hat,'r',t,b_hat,'g',t,c_hat,'b')
#plt.plot(t,E,'k')
plt.title('Steering')
plt.xlabel('t [s]')
#plt.xlim([0,xmax])
#plt.ylim([-1,1])
plt.legend(["M_gamma","M_pred","M_hat"])
plt.grid()


plot2 = plt.figure(2)
plt.plot(t,a1_hat,'r',t,a2_hat,'g',t,b_hat,'b')
plt.xlabel('t [s]')
#plt.xlim([0,xmax])
plt.legend(["a1_hat","a2_hat","b_hat"])
plt.grid()

plot3 = plt.figure(3)
plt.plot(t[1:],E,'b')
plt.xlabel('t [s]')
#plt.xlim([0,xmax])
plt.legend(["e1"])
plt.grid()

plt.show()
