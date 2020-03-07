import cv2

img=cv2.imread('joker-wallpaper-1366x768-laptop-131184.jpg')

imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV image',imgHSV)

cv2.waitKey(0)

cv2.imshow("Hue Channel",imgHSV[:,:,0])
cv2.waitKey(0)

cv2.imshow("Saturation Channel",imgHSV[:,:,1])
cv2.waitKey(0)

cv2.imshow("Value Channel",imgHSV[:,:,2])
cv2.waitKey(0)

cv2.destroyAllWindows()