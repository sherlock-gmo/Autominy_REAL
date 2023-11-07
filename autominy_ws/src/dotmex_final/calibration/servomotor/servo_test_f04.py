import csv
import numpy as np
from scipy.linalg import solve_continuous_lyapunov as lyp
import matplotlib.pyplot as plt

# Se cargan los datos del regresor
States = np.load('states02.npy')
print(States.shape)
T = States[:,0]
S_gamma = States[:,1]
M_gamma = States[:,2]
DM_gamma = States[:,3]


# Parametros del predictor
t = T-T[0]
h = 0.01
N = t.shape
sDM_gamma = np.zeros((N[0]))
i = 0
for d in DM_gamma: 
	sDM_gamma[i] = d/abs(d)
	i = i+1
E = np.zeros((N[0]))

a1 = 13.30273827111085
a2 = 139.25735617192942
c = 2.3055177886410507
b = 21.85109769735648
d = 1.0156779722818359
M_pred = np.zeros((N[0]))
DM_pred = np.zeros((N[0]))
for i in range(1,N[0]):
	DDM_pred = -a1*DM_pred[i]-a2*M_pred[i]-c*sDM_gamma[i]+b*S_gamma[i]+d
	DDM_pred_h = -a1*DM_pred[i-1]-a2*M_pred[i-1]-c*sDM_gamma[i-1]+b*S_gamma[i-1]+d
	DM_pred[i] = DM_pred[i-1]+(h/2.0)*(DDM_pred+DDM_pred_h)
	M_pred[i] = M_pred[i-1]+(h/2.0)*(DM_pred[i]+DM_pred[i-1])
	E[i] = M_gamma[i]-M_pred[i]

plot1 = plt.figure(1)
plt.plot(t,S_gamma,'k',t,M_gamma,'r',t,M_pred,'b')
plt.xlabel('t [s]')
plt.legend(["S_gamma","M_gamma","M_pred"])
plt.grid()

plot2 = plt.figure(2)
plt.plot(t,DM_gamma,'r',t,DM_pred,'g')
plt.xlabel('t [s]')
plt.legend(["DM_gamma","DM_pred"])
plt.grid()

plot3 = plt.figure(3)
plt.plot(t,E,'b')
plt.xlabel('t [s]')
plt.legend(["e"])
plt.grid()

plt.show()
