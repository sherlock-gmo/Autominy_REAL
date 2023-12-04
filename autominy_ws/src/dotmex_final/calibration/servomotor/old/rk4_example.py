import numpy as np
import matplotlib.pyplot as plt

# Definimos la ecuación diferencial dy/dx = f(x, y)
def f(x, y):
    return x**2 + y**2
def g(y):
    return 1-y

# Función que realiza un paso del método de Runge-Kutta de cuarto orden
def runge_kutta_step(x, y, h):
    k1 = h * f(x, y)
    k2 = h * f(x + h/2, y + k1/2)
    k3 = h * f(x + h/2, y + k2/2)
    k4 = h * f(x + h, y + k3)
    y_new = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    x_new = x + h
    return x_new, y_new

# Función que realiza un paso del método de Runge-Kutta de cuarto orden
def runge_kutta_step2(y, h):
    k1 = h * g(y)
    k2 = h * g(y + k1/2)
    k3 = h * g(y + k2/2)
    k4 = h * g(y + k3)
    y_new = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    return y_new

# Parámetros iniciales
x0 = 0  # Valor inicial de x
y0 = 0.0  # Valor inicial de y
h = 0.1  # Tamaño del paso
x_final = 5.0  # Valor final de x

# Crear listas para almacenar los valores de x e y
x_values = [x0]
y_values = [y0]

# Realizar iteraciones para resolver la ecuación diferencial
i = 0
t = 0.0
T = [t]
while t < 5.0:
    y0 = runge_kutta_step2(y0, h)
    t = i*h
    y_values.append(y0)
    T.append(t)
    i = i+1

# Imprimir los resultados
#for x, y in zip(x_values, y_values):
#    print(f'x = {x}, y = {y}')

plot1 = plt.figure(1)
plt.plot(T,y_values,'b')
#plt.xlabel('t [s]')
#plt.legend(["e1"])
plt.grid()


plt.show()
