import cv2
import numpy as np

K = np.array([[901.93659457,0.0,951.48766685],[0.0,903.03351126,517.14560046],[0.0,0.0,1.0]])
dist = np.array([[-0.34029507,0.10715362,0.0004996,-0.00253667,-0.01368018]])
img = cv2.imread('imagen134.png')
h, w = img.shape[:2]
h = int(h*1.75)
w = int(w*1.45)
#newcameramtx, roi = cv2.getOptimalNewCameraMatrix(K, dist, (w,h), 1, (w,h))


mapx, mapy = cv2.initUndistortRectifyMap(K, dist, None, None, (w,h), 5)
dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
# crop the image
#x, y, w, h = roi
#dst = dst[y:y+h, x:x+w]
cv2.imwrite('undist.png', dst)


