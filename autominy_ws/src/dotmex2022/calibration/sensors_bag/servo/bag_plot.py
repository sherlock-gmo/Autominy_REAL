import csv
import numpy as np
import matplotlib.pyplot as plt

path = '/home/sherlock/dotMEX_Autominy_REAL/autominy_ws/src/dotmex2022/calibration/sensors_bag/servo/'
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
def gen_vec(file_csv):
	T = []
	S_servo = []
	M_servo = []
	with open(path+file_csv, 'r') as datafile:
		ploting = csv.reader(datafile, delimiter='	',quoting=csv.QUOTE_NONNUMERIC)
		for ROWS in ploting:
			T.append(ROWS[0])
			S_servo.append(ROWS[1])
			M_servo.append(ROWS[2])
	return np.array(T),np.array(S_servo,dtype=float),np.array(M_servo,dtype=float)
#**************************************************************************************************
#**************************************************************************************************
#**************************************************************************************************
file_data = 'sensors_servo_5'
T,S_servo,M_servo= gen_vec(file_data+'.csv')

t = T-T[0]
M_servo_N = (1.0/0.38)*M_servo
xmax= int(t[-1])+1

plt.plot(t,S_servo,'b',t,M_servo_N,'r')
plt.title('Steering')
plt.xlabel('t [s]')
plt.xlim([0,xmax])
plt.legend(["S_servo_N", "M_servo_N"], loc='lower right',)
plt.grid()
plt.show()


