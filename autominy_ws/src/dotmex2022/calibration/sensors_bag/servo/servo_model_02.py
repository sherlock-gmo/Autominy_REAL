import csv
import numpy as np
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
file_data = 'sensors_servo_test_175.csv'
T,S_gamma,M_gamma= gen_vec(file_data)

t = T-T[0]
xmax= int(t[-1])+1

a = 1.1891850075536386e-05 #2.47594434
b = 0.0005239980341020188 #1.62469849
c = 0.00043064898652480206
N = t.shape
M = np.zeros((N[0]))
for i in range(1,N[0]): #2
	h = t[i]-t[i-1]
	#M[i] = (1.0/(1.0+a*h))*(M[i-1]+b*h*S_gamma[i]) #1er Orden
	M[i] = (1.0/(1.0+a*h+b*(h**2)))*((2+a*h)*M[i-1]-M[i-2]+c*(h**2)*S_gamma[i]) #2do Orden

plt.plot(t,M_gamma,'r',t,M,'g')
plt.title('Steering')
plt.xlabel('t [s]')
plt.xlim([0,xmax])
plt.legend(["M_gamma", "M_model"])
plt.grid()
plt.show()
	

