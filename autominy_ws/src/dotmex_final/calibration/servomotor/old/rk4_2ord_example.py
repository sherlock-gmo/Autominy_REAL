import numpy as np
import matplotlib.pyplot as plt

# Definimos las ecuaciones diferenciales de primer orden
def f(x, y, z):
    return z

def g(x, y, z):
    return -2.0*y-0.5*z #-x**2 * y

def m(x, y, z):
	p = 0.5*np.exp(-0.25*x)
	return -2.0*y-p*z #-x**2 * y

# Función que realiza un paso del método de Runge-Kutta de cuarto orden
def runge_kutta_step(x, y, z, h):
    k1 = h * f(x, y, z)
    l1 = h * m(x, y, z)
    
    k2 = h * f(x + h/2, y + k1/2, z + l1/2)
    l2 = h * m(x + h/2, y + k1/2, z + l1/2)
    
    k3 = h * f(x + h/2, y + k2/2, z + l2/2)
    l3 = h * m(x + h/2, y + k2/2, z + l2/2)
    
    k4 = h * f(x + h, y + k3, z + l3)
    l4 = h * m(x + h, y + k3, z + l3)
    
    y_new = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    z_new = z + (l1 + 2*l2 + 2*l3 + l4) / 6
    x_new = x + h
    
    return x_new, y_new, z_new

# Parámetros iniciales
x0 = 0  # Valor inicial de x
y0 = 1  # Valor inicial de y
z0 = 0  # Valor inicial de z
h = 0.1  # Tamaño del paso
x_final = 50.0  # Valor final de x

# Crear listas para almacenar los valores de x, y y z
x_values = [x0]
y_values = [y0]
z_values = [z0]

# Realizar iteraciones para resolver las ecuaciones diferenciales
while x0 < x_final:
    x0, y0, z0 = runge_kutta_step(x0, y0, z0, h)
    x_values.append(x0)
    y_values.append(y0)
    z_values.append(z0)


plot1 = plt.figure(1)
plt.plot(x_values,y_values,'b',x_values,z_values,'r')
#plt.xlabel('t [s]')
#plt.legend(["e1"])
plt.grid()


plt.show()
