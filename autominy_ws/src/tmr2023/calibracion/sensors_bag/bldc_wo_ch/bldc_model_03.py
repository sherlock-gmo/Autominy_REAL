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
file_data = 'sensors_bldc_5.csv'
T,S_omega,M_omega= gen_vec(file_data)

t = T-T[0]
xmax= int(t[-1])+1

# 																		PREDICTORS
N = t.shape
alpha = 5.0
gamma1 = 1.0
gamma2 = 2.0 
M_hat = np.zeros((N[0]))
a_hat = np.zeros((N[0]))
b_hat = np.zeros((N[0]))
E = np.zeros((N[0]))
a_hat[0] = 1.0
b_hat[0] = 1.0 

for i in range(1,N[0]):
	h = t[i]-t[i-1]
	M_hat[i] = (1.0/(1.0+alpha*h))*(M_hat[i-1]+h*(alpha-a_hat[i])*M_omega[i]+h*b_hat[i]*S_omega[i])
	e = M_hat[i]-M_omega[i]
	E[i] = e
	a_hat[i] = a_hat[i-1]+h*gamma1*e*M_omega[i]
	b_hat[i] = b_hat[i-1]-h*gamma2*e*S_omega[i]

"""
for i in range(0,N[0]-1):
	h = t[i+1]-t[i]
	M_hat[i+1] = (1.0-alpha*h)*M_hat[i]+h*(alpha-a_hat[i])*M_omega[i]+h*b_hat[i]*S_omega[i]
	e = M_hat[i]-M_omega[i]
	a_hat[i+1] = a_hat[i]+h*gamma1*e*M_omega[i]
	b_hat[i+1] = b_hat[i]-h*gamma2*e*S_omega[i]
"""
print('a_hat, b_hat ',a_hat[-1],b_hat[-1])
print('e ',e)

plt.plot(t,M_omega,'r',t,M_hat,'g',t,a_hat,'k',t,b_hat,'k')
plt.title('Speed')
plt.xlabel('t [s]')
plt.xlim([0,xmax])
#plt.ylim([-1,1])
plt.legend(["M_omega","M_hat"])
plt.grid()
plt.show()

