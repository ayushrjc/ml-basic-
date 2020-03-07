import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)

# cv2.imshow('output',img)
# cv2.waitKey(0)
'''
#rows
cv2.line(img,(0,102),(512,102),(0,0,255),10)
cv2.line(img,(0,204),(512,204),(0,0,255),10)
cv2.line(img,(0,306),(512,306),(0,0,255),10)
cv2.line(img,(0,408),(512,408),(0,0,255),10)
#coloms
cv2.line(img,(102,0),(102,512),(0,0,255),10)
cv2.line(img,(204,0),(204,512),(0,0,255),10)
cv2.line(img,(306,0),(306,512),(0,0,255),10)
cv2.line(img,(408,0),(408,512),(0,0,255),10)


#circle
cv2.circle(img,center=(250,250),radius=(100),color=(0,255,0),thickness=-6)

#rectangle
cv2.rectangle(img,(100,100),(400,400),(0,255,0),5)

#to put text
name='ayush'
cv2.putText(img,name,(150,450),cv2.FONT_HERSHEY_TRIPLEX,2,(0,255,0,5))
'''
cv2.imshow('Line',img)
cv2.waitKey(0)
cv2.destroyAllWindows()