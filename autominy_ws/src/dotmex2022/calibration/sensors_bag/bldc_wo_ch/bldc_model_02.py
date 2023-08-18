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
file_data = 'sensors_bldc_test_275.csv'
T,S_omega,M_omega= gen_vec(file_data)

t = T-T[0]
xmax= int(t[-1])+1
a = 0.89806430058545617
b = 101.44670462178861
N = t.shape
M = np.zeros((N[0]))
for i in range(1,N[0]):
	h = t[i]-t[i-1]
	M[i] = (1.0/(1.0+a*h))*(M[i-1]+b*h*S_omega[i]) #1er Orden
	#M[i] = (1.0-a*h)*M[i-1]+b*h*S_omega[i-1] #1er Orden
	#M[i] = (1.0/(1.0+a*h+b*(h**2)))*((2+a*h)*M[i-1]-M[i-2]+b*(h**2)*S_omega[i]) #2do Orden

plt.plot(t,M_omega,'r',t,M,'g')
plt.title('Speed')
plt.xlabel('t [s]')
plt.xlim([0,xmax])
plt.legend(["M_omega", "M_model"])
plt.grid()
plt.show()
	

