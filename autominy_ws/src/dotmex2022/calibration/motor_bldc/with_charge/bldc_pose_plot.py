import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

path = '/home/ros/dotMEX_Autominy_REAL/autominy_ws/src/dotmex2022/calibration/motor_bldc/with_charge/'
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
def gen_vec(file_csv):
	X = []
	Y = []
	T = []
	V = []
	with open(path+file_csv, 'r') as datafile:
		ploting = csv.reader(datafile, delimiter='	')
		for ROWS in ploting:
			T.append(float(ROWS[0]))
			X.append(float(ROWS[1]))
			Y.append(395.0-float(ROWS[2]))
	return np.array(T),np.array(X),np.array(Y)
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
file_gps_vis = 'position_v250.csv'
T,X,Y= gen_vec(file_gps_vis)
plt.plot(X,Y,marker='.')
plt.title('Pose 2D')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()

