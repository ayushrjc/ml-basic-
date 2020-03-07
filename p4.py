#pip install opencv-python
import cv2
img=cv2.imread('joker-wallpaper-1366x768-laptop-131184.jpg')
cv2.imshow('Original Image',img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

