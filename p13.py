import cv2

cap=cv2.VideoCapture(0)

if cap.isOpened():
    ret,frame=cap.read()

cv2.imshow('Output',frame)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()