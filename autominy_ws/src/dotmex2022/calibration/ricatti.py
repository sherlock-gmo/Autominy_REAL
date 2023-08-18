import sys
import numpy as np
import scipy.linalg
# Frec. de muestreo de la senal de control(Hz)
f = 20.0 #C.Lidar 20 // S.Lidar 30
# Periodo de muestreo de la senal de control (s)
h = 1/f
# Velocidad de avance del auto (rpm) 
vrpm = 200
# Velocidad de avance del auto (m/s)
v = 1.0 #vrpm*(0.588/200)
# Separacion de los ejes (m)
L = 0.26
# Distancia entre las llantas traseras y la base de la homografia (m)
Lh = 0.375 
# Matrices del modelo cinematico usado
A = np.matrix ([[1,v*h], [0,1]])
B = (v*h/L)*np.matrix([[Lh+v*h/2], [1]])
C = np.matrix([[1,0], [0,1]])
# Matrices de ponderacion propuestas
Q = 0.15*np.matrix([[1,0],[0,1]]) # dir. prop. a Ke
R = 5.0	# inv. prop. a Ke
print("-------------------------------------------")
print('v_rpm',vrpm)
print('v',v)
print('R',R)
print('Q',Q)
print("-------------------------------------------")
P = np.matrix(scipy.linalg.solve_discrete_are(A,B,Q,R))
#print('P',P)
print("-------------------------------------------")
print('Ganancias del Optimal Controller Ky Kth')
K = np.matrix(scipy.linalg.inv(B.T*P*B+R)*(B.T*P*A))
print('K',K)
"""
print("-------------------------------------------")
print('Ganancias del Preview Controller Ke Kth')
for i in range(1,5):
	fi = np.matrix(scipy.linalg.inv(B.T*P*B+R)*B.T*(((A-B*K).T)**(i-1))*C.T*Q)
	print(i)
	print(fi)
"""
