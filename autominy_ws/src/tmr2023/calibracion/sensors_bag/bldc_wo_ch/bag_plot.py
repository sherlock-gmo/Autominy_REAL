import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

path = '/home/sherlock/dotMEX_Autominy_REAL/autominy_ws/src/dotmex2022/calibration/sensors_bag/bldc_wo_ch/'
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
def gen_vec(file_csv):
	T = []
	S_Omega = []
	M_Omega = []
	with open(path+file_csv, 'r') as datafile:
		ploting = csv.reader(datafile, delimiter='	',quoting=csv.QUOTE_NONNUMERIC)
		for ROWS in ploting:
			#print(ROWS)
			T.append(ROWS[0])
			S_Omega.append(ROWS[1])
			M_Omega.append(ROWS[2])
	return np.array(T),np.array(S_Omega,dtype=float),np.array(M_Omega,dtype=float)
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
file_data = 'sensors_bldc_4'
T,S_Omega,M_Omega= gen_vec(file_data+'.csv')

t = T-T[0]
S_Omega_N = (1.0/1000.0)*S_Omega
M_Omega_N = (1.0/4.815)*M_Omega
xmax= int(t[-1]-t[0])+1

plt.plot(t,S_Omega_N,'b',t,M_Omega_N,'r')
plt.title('Speed')
plt.xlabel('t [s]')
plt.xlim([0,xmax])
plt.legend(["S_Omega_N", "M_Omega_N"], loc='lower right',)
plt.grid()
plt.show()


