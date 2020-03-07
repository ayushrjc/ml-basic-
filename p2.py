# pip install opencv-python
import cv2
img=cv2.imread('joker-wallpaper-1366x768-laptop-131184.jpg')
print(img.shape)
print("Height of the image:",int(img.shape[0]),"pixel")
print("Height of the image:",int(img.shape[1]),"pixel")
