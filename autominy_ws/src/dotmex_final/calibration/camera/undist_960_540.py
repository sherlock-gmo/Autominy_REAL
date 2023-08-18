import cv2
import numpy as np

K = np.array([[410.80239519,0.0,469.13953267],[0.0,412.74534584,258.91870387],[0.0,0.0,1.0]])
dist = np.array([[-2.80892642e-01,7.20543846e-02,-1.77783135e-04,-9.27152558e-04,-7.49371778e-03]])
img = cv2.imread('imagen149_960_540.png')
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


