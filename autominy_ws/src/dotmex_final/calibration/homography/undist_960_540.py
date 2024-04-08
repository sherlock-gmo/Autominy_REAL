import cv2
import numpy as np

img = cv2.imread('image_960_540_wl.png')
K = np.array([[410.80239519,0.0,469.13953267],[0.0,412.74534584,258.91870387],[0.0,0.0,1.0]])
dist = np.array([[-2.80892642e-01,7.20543846e-02,-1.77783135e-04,-9.27152558e-04,-7.49371778e-03]])
u,v,_ = img.shape #[960,540]
nK,_ = cv2.getOptimalNewCameraMatrix(K, dist, (u,v), 1, (u,v))

undistorted_image = cv2.undistort(img, K, dist, None, nK)
cv2.imwrite('undist_960_540_uncut.png', undistorted_image)

undistorted_image = undistorted_image[172:422, 198:714] # Se guardan los parametros x_tras=198, y_tras=172
cv2.imwrite('undist_960_540_cut.png', undistorted_image)


