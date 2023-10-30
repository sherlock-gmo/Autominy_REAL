import numpy as np
import math as m
import matplotlib.pyplot as plt

z10 = 0.0
z20 = 0.0

Z1 = []
Z2 = []
S = []
T = []
w = 2.5								# Escala de tiempo del oscilador en [rad/s]
h = 1.0/30.0					# Periodo de muestreo en [s]
Tf = 120.0						# Tiempo de la simulacion en [s]
It = int(round(Tf/h))	# Numero de iteraciones
for i in range(It):
	z1 = z10+h*w*z20
	z2 = z20+h*(w*z1-0.025*z20-0.75*w*(z1**3)+0.3*m.sin(w*i*h))
	s = (3.33/5.89)*z1
	T.append(i*h)
	Z1.append(z1)
	Z2.append(z2)
	S.append(s)
	z10 = z1
	z20 = z2

print(max(S))
print(min(S))

plot1 = plt.figure(1)
plt.plot(T,S,'r')
plt.xlabel('t [s]')
plt.legend(["S"])
plt.grid()

plot2 = plt.figure(2)
plt.plot(T,Z1,'r',T,Z2,'b')
plt.xlabel('t [s]')
plt.legend(["z1", "z2"])
plt.grid()

plt.show()
