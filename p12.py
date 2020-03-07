#webcam :)
import cv2

cap=cv2.VideoCapture(0)

while True:
    #for normal video
    ret,frame = cap.read()
    cv2.imshow("My Live Cam",frame)
    #for canny video
    canny = cv2.Canny(frame, 100, 250)
    cv2.imshow('canny edge', canny)


    if cv2.waitKey(1)==13:
        break
cap.release() #compulsary :'(
cv2.destroyAllWindows()