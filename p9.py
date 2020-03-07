'''

\\\|||///
  O   O      <--- vismaya
    U
   ---


    '''

import cv2
img=cv2.imread('joker-wallpaper-1366x768-laptop-131184.jpg',0)
sobel_x=cv2.Sobel(img,cv2.CV_8U,dx=1,dy=0,ksize=-1)
sobel_y=cv2.Sobel(img,cv2.CV_8U,dx=0,dy=1,ksize=-1)
sobel_f=cv2.bitwise_or(sobel_x,sobel_y)#All edges are highlighted

cv2.imshow('sobel X-image',sobel_x)
cv2.imshow('sobel Y-image',sobel_y)
cv2.imshow('sobel F-image',sobel_f)

lapl=cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow('Laplacian image',lapl)

canny=cv2.Canny(img,100,250)
cv2.imshow('canny edge',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

