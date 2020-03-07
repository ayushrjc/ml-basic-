#pip install opencv-python
import cv2
img=cv2.imread('joker-wallpaper-1366x768-laptop-131184.jpg',0) #0 converts it to gray
cv2.imshow('Original Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

