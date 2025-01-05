import cv2
import numpy as np

vid = cv2.VideoCapture(0)

while True:
    ret,frame = vid.read()
    width = int(vid.get(3))
    height = int(vid.get(4))

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue  = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('hsv',res)
    cv2.imshow('mask',mask)
    
    if cv2.waitKey(1) == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
