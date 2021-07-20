import cv2
import time
import numpy as np

vid = cv2.VideoCapture(0)
img = cv2.imread("tajMahal.jpeg")

while True:
    ret,frame = vid.read()
    print(frame)
    frame = cv2.resize(frame,(640,480))
    img = cv2.resize(img,(640,480))
    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])
    mask = cv2.inRange(frame,l_black,u_black)
    res = cv2.bitwise_and(frame,frame,mask = mask)
    f = frame-res
    f = np.where(f ==0,img,f)
    cv2.imshow("vid",frame)
    cv2.imshow("mask",f)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
video.release()
cv2.destroyAllWindows()
