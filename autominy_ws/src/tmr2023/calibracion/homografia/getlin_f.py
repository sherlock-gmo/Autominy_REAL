import numpy as np

# Coordenadas del trapecio de izquierda a derecha
p1 = 1.0*np.array([0,139])
p2 = 1.0*np.array([80,299])
p3 = 1.0*np.array([119,299])
p4 = 1.0*np.array([199,141])

print('L. Base ')
print(p2[0],p3[0])

bI = p1[1]
mI = (p2[1]-p1[1])/(p2[0]-p1[0])
print('L. Izquierda')
print('mI bI')
print(mI,bI)

mD = float((p3[1]-p4[1])/(p3[0]-p4[0]))
bD = p3[1]-mD*p3[0]
print('L. Derecha')
print('mD bD')
print(mD,bD)
