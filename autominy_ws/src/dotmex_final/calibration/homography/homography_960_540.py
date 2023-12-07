import cv2
import numpy as np
from matplotlib import pyplot as plt
from numpy.linalg import inv

img1 = cv2.imread('undist_960_540_cut.png',1) # Origen (Imagen del suelo)
#**************************************************
#**************************************************
#**************************************************
# Se definen 4 puntos en la imagen de origen. Las unidades son px.
p1_1 = [242,127]
p1_2 = [301,127]	
p1_3 = [466,180]
p1_4 = [164,184]
P1 = np.concatenate(([[p1_1],[p1_2],[p1_3],[p1_4]]),axis=0)
# Se seleccionan 4 puntos en la imagen de destino, se escriben en cm y se usa como referencial 
# al vector de traslacion T. Este se varia segun convenga a la imagen de salida; 
T = [140,233]#[140,233] 
p2_1 = np.add([0.0,0.0],T)
p2_2 = np.add([29.5,0.0],T)			
p2_3 = np.add([29.5,60.5],T) 
p2_4 = np.add([0,60.5],T)
P2 = np.array([p2_1,p2_2,p2_3,p2_4])
H, mask = cv2.findHomography(P1, P2, cv2.RANSAC,5.0) 
#**************************************************
#**************************************************
#**************************************************
print("****************")
print("Matriz de Homografia")
print(H) # Matriz de homografia
#Obtenemos la imagen con correccion de pespectiva
imagenH = cv2.warpPerspective(img1, H, (300,300),borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0)) 			
cv2.imshow('imagenH',imagenH)
cv2.waitKey(0)
cv2.imwrite('homography_960_540.png',imagenH)
cv2.destroyAllWindows()


