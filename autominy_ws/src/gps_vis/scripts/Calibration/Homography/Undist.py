import numpy as np
import cv2

n = 4
imagen0 = cv2.imread('0'+str(n)+'image.png',1) # Origen (Imagen del suelo)
#**************************************************
#**************************************************
#**************************************************
K = np.array([[319.71415651,0.0,344.96615854],[0.0,317.26216773,261.53024149],[0.0, 0.0, 1.0]])
dist_coef = np.array([[-0.3466721,0.14940472,-0.00101803,0.00506543,-0.03453036]])
h,w = imagen0.shape[:2]
w = int(w*1.0)
h = int(h*1.45)
mapx,mapy = cv2.initUndistortRectifyMap(K,dist_coef,None,None,(w,h),5)
imagenK = cv2.remap(imagen0,mapx,mapy,cv2.INTER_LINEAR)
cv2.imwrite('Undist_0'+str(n)+'.png',imagenK)
