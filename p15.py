import cv2
#detecting the face
face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('abc.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=9)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),5)
    cv2.imshow('Face recognised',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
