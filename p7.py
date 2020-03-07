import cv2
import numpy as np
'''img=np.zeros((250,250,3))
img[:]=0,0,255
img1=np.zeros((250,250,3))
img1[:]=0,255,0
img2=np.zeros((250,250,3))
img2[:]=255,0,0
cv2.imshow("green",img1)
cv2.imshow("red",img)
cv2.imshow("blue",img2)'''

# img3=np.zeros((250,250,3))
# # img3[0:125]=0,0,255
# # img3[125:250]=255,0,0
# # cv2.imshow("combo",img3)

img4=np.zeros((250,250,3))
img4[0:125,0:125]=0,0,0
img4[125:250,125:250]=0,0,0
img4[0:125,125:250]=255,255,255
img4[125:250,0:125]=255,255,255
cv2.imshow("combo",img4)

cv2.waitKey(0)
cv2.destroyAllWindow()