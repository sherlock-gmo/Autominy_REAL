import numpy as np
import cv2
import glob
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
from numpy.linalg import inv

n = 4
imagenK = cv2.imread('Undist_0'+str(n)+'.png',1) # Origen (Imagen del suelo)
#**************************************************
#**************************************************
# Se definen 4 puntos en la imagen de origen. Las unidades son px.
p1_1 = [37,84]
p1_2 = [422,27]	
p1_3 = [514,471]
p1_4 = [150,560]
P1 = np.concatenate(([[p1_1],[p1_2],[p1_3],[p1_4]]),axis=0)
# Se seleccionan 4 puntos en la imagen de destino, se escriben en cm y se usa como referencial 
# al vector de traslacion T. Este se varia segun convenga a la imagen de salida; 
T = [32,32]
p2_1 = np.add([0.0,0.0],T)
p2_2 = np.add([276.5,0.0],T)			#338x276.5
p2_3 = np.add([276.5,338.0],T) 
p2_4 = np.add([0.0,338.0],T)
P2 = np.array([p2_1,p2_2,p2_3,p2_4])
H, mask = cv2.findHomography(P1, P2, cv2.RANSAC,5.0) 
#**************************************************
#**************************************************
#**************************************************
print("****************")
print("Matriz de Homografia")
print(H) # Matriz de homografia
#Obtenemos la imagen con correccion de pespectiva
imagenH = cv2.warpPerspective(imagenK, H, (375,430),borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0)) 		
cv2.imwrite('Homography0'+str(n)+'.png',imagenH)
imagenH = cv2.cvtColor(imagenH, cv2.COLOR_BGR2RGB)	
plt.imshow(imagenH, 'gray'), plt.show()
