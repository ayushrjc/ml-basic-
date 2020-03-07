import cv2
import numpy as np
img=np.ones((500,500,3))
img1=np.zeros((259,250,3))
cv2.imshow("Whtitebackground",img)
cv2.imshow("Blackbackground",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()