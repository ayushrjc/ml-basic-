import cv2
import numpy as np

windowName='Drawing'
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow(windowName)

# def draw_circle(event,x,y,flags,param):
#     if event==cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img,(x,y),60,(0,255,0),-1)
#     if event == cv2.EVENT_RBUTTONDBLCLK:
#         cv2.circle(img, (x, y), 50, (0, 255, 0), -1)
#     if event==cv2.EVENT_RBUTTONDOWN:
#         cv2.circle(img,(x,y),40,(255,0,0),-1)
#     if event==cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img, (x, y), 10, (0,0,0), -1)

abc=False
def draw_circle(event,x,y,flags,param):
    global abc
    if event==cv2.EVENT_LBUTTONDOWN:
        abc=True
        cv2.circle(img,(x,y),5,(0,255,0),-1)
    elif event==cv2.EVENT_MOUSEMOVE:
        if abc==True:
            cv2.circle(img,(x,y),5,(0,255,0),-1)
    else:
        abc=False


cv2.setMouseCallback(windowName,draw_circle)
while(True):
    cv2.imshow(windowName,img)
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()