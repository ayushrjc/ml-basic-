import cv2,time

from datetime import datetime

frame=None
statusL=[None,None]
times=[]
df=pandas.DataFrame(columns=["Start","End"])
video=cv2.VideoCapture(0)
while True:
    ch,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if frame is None:
        frame=gray
        continue
    dframe=cv2.absdiff(frame,gray)
    tdelta=cv2.threshold(dframe,30,255,cv2.THRESH_BINARY)[1]
    tdelta=cv2.dilate(tdelta,None,iterations=0)
    (_,cnts,_)=cv2.findContours(tdelta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour)<1000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(2,255,0),3)
        statusL.append(status)
        statusL=statusL[-2:]

        if statusL[-1]==1 and statusL[-2]==0:
            times.append(datetime.now())
        if statusL[-1]==0 and statusL[-2]==1:
            times.append(datetime.now())
        print(statusL)
        print(times)
    for i in range(0,len(times),2):
        df=df.append("start:",times[i],"End:",times[i+1],ignore_index=True)
        df.to_csv("Times.csv")

    cv2.imshow('frame',frame)
video.release()
cv2.destroyAllWindows()

