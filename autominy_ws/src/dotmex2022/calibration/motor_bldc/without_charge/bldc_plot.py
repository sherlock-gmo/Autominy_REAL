import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

path = '/home/ros/dotMEX_Autominy_REAL/autominy_ws/src/dotmex2022/calibration/motor_bldc/without_charge/' 
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
def gen_vec(file_csv):
	T = []
	S_omega = []
	M_omega = []
	with open(path+file_csv, 'r') as datafile:
		ploting = csv.reader(datafile, delimiter='	')
		for ROWS in ploting:
			T.append(float(ROWS[0]))
			S_omega.append(float(ROWS[1]))
			M_omega.append(float(ROWS[2]))
	return np.array(T),np.array(S_omega),np.array(M_omega)
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
i = 50
for i in range(50,501,50):
	file_gps_vis = 'bldc0_v'+str(i)+'.csv'
	T,S_omega,M_omega= gen_vec(file_gps_vis)
	plt.plot(T,M_omega,'r')

for i in range(600,1001,100):
	file_gps_vis = 'bldc0_v'+str(i)+'.csv'
	T,S_omega,M_omega= gen_vec(file_gps_vis)
	plt.plot(T,M_omega,'r')

plt.title('Pose 2D')
plt.xlabel('T [s]')
plt.ylabel('M_omega')
plt.grid()
plt.show()

