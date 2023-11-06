import csv
import numpy as np
from scipy.linalg import solve_continuous_lyapunov as lyp
import matplotlib.pyplot as plt

# Se cargan los datos del regresor
States = np.load('states.npy')
print(States.shape)
T = States[:,0]
S_gamma = States[:,1]
M_gamma = States[:,2]
DM_gamma = States[:,3]

# Parametros del predictor
t = T-T[0]
h = 0.01
N = t.shape
alpha1 = 75 #50 #75 #150.0 
alpha2 = 15 #15 #20 #25.0 
gamma1 = 200 #200.0 #1000.0 #100.0
gamma2 = 400 #400.0 #2000.0 #200.0
gamma3 = 100 
gamma4 = 100 #800.0 #4000.0 #400.0
gamma5 = 1.0

E = []
M_hat = np.zeros((N[0]))
DM_hat = np.zeros((N[0]))
sDM_gamma = np.zeros((N[0]))
i = 0
for d in DM_gamma: 
	sDM_gamma[i] = d/abs(d)
	i = i+1
a1_hat = np.zeros((N[0]))
a2_hat = np.zeros((N[0]))
c_hat = np.zeros((N[0]))
b_hat = np.zeros((N[0]))
d_hat = np.zeros((N[0]))
a1_hat[0] = 100.0 #100.0 
a2_hat[0] = 100.0 #100.0 
c_hat[0] = 50.0 #50.0 
b_hat[0] = 50.0 #50.0 
d_hat[0] = 1.0 #1.0

for i in range(1,N[0]):
	# Regresor
	DDM_hat = (alpha2-a1_hat[i])*DM_gamma[i]+(alpha1-a2_hat[i])*M_gamma[i]-c_hat[i]*sDM_gamma[i]+b_hat[i]*S_gamma[i]+d_hat[i]-alpha2*DM_hat[i]-alpha1*M_hat[i]
	DDM_hat_h = (alpha2-a1_hat[i-1])*DM_gamma[i-1]+(alpha1-a2_hat[i-1])*M_gamma[i-1]-c_hat[i-1]*sDM_gamma[i-1]+b_hat[i-1]*S_gamma[i-1]+d_hat[i-1]-alpha2*DM_hat[i-1]-alpha1*M_hat[i-1]
	DM_hat[i] = DM_hat[i-1]+(h/2.0)*(DDM_hat+DDM_hat_h)
	M_hat[i] = M_hat[i-1]+(h/2.0)*(DM_hat[i]+DM_hat[i-1])
	e1 = M_hat[i]-M_gamma[i]
	e2 = DM_hat[i]-DM_gamma[i]
	e2_h = DM_hat[i-1]-DM_gamma[i-1]
	# Regla de actualizacion
	Da1_hat = gamma1*(e2)*DM_gamma[i]
	Da1_hat_h = gamma1*(e2_h)*DM_gamma[i-1]
	a1_hat[i] = a1_hat[i-1]+(h/2.0)*(Da1_hat+Da1_hat_h)

	Da2_hat = gamma2*(e2)*M_gamma[i]
	Da2_hat_h = gamma2*(e2_h)*M_gamma[i-1]
	a2_hat[i] = a2_hat[i-1]+(h/2.0)*(Da2_hat+Da2_hat_h)

	Dc_hat = gamma3*(e2)*sDM_gamma[i]
	Dc_hat_h = gamma3*(e2_h)*sDM_gamma[i-1]
	c_hat[i] = c_hat[i-1]+(h/2.0)*(Dc_hat+Dc_hat_h)

	Db_hat = -gamma4*(e2)*S_gamma[i]
	Db_hat_h = -gamma4*(e2_h)*S_gamma[i-1]
	b_hat[i] = b_hat[i-1]+(h/2.0)*(Db_hat+Db_hat_h)
	
	Dd_hat = -gamma5*(e2)
	Dd_hat_h = -gamma5*(e2_h)
	d_hat[i] = d_hat[i-1]+(h/2.0)*(Dd_hat+Dd_hat_h)

	# Error de prediccion
	E.append(e1)

M_pred = np.zeros((N[0]))
DM_pred = np.zeros((N[0]))
for i in range(1,N[0]):
	#DDM_pred = -a1_hat[-1]*DM_pred[i]-a2_hat[-1]*M_pred[i]+10.0*S_gamma[i] 
	#DDM_pred_h = -a1_hat[-1]*DM_pred[i-1]-a2_hat[-1]*M_pred[i-1]+10.0*S_gamma[i-1] 
	DDM_pred = -a1_hat[-1]*DM_pred[i]-a2_hat[-1]*M_pred[i]-c_hat[-1]*sDM_gamma[i]+b_hat[-1]*S_gamma[i]+d_hat[-1] 
	DDM_pred_h = -a1_hat[-1]*DM_pred[i-1]-a2_hat[-1]*M_pred[i-1]-c_hat[-1]*sDM_gamma[i-1]+b_hat[-1]*S_gamma[i-1]+d_hat[-1] 
	DM_pred[i] = DM_pred[i-1]+(h/2.0)*(DDM_pred+DDM_pred_h)
	M_pred[i] = M_pred[i-1]+(h/2.0)*(DM_pred[i]+DM_pred[i-1])

print('e ',e1)
print('a1_hat, a2_hat, c_hat, b_hat d_hat',a1_hat[-1],a2_hat[-1],c_hat[-1],b_hat[-1],d_hat[-1])


plot1 = plt.figure(1)
plt.plot(t,S_gamma,'k',t,M_gamma,'r',t,M_pred,'g',t,M_hat,'b')
plt.xlabel('t [s]')
plt.legend(["S_gamma","M_gamma","M_pred","M_hat"])
plt.grid()

plot2 = plt.figure(2)
plt.plot(t,DM_gamma,'r',t,DM_pred,'g',t,DM_hat,'b')
plt.xlabel('t [s]')
plt.legend(["DM_gamma","DM_pred","DM_hat"])
plt.grid()

plot3 = plt.figure(3)
plt.plot(t[1:],E,'b')
plt.xlabel('t [s]')
plt.legend(["e1"])
plt.grid()

plot4 = plt.figure(4)
plt.plot(t,a1_hat,'r',t,a2_hat,'g',t,c_hat,'m',t,b_hat,'b',t,d_hat,'y')
plt.xlabel('t [s]')
plt.legend(["a1_hat","a2_hat","c_hat","b_hat","d_hat"])
plt.grid()

plt.show()
