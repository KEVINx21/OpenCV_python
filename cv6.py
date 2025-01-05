import numpy as np
import cv2

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    width = int(vid.get(3))
    height = int(vid.get(4))

    line = cv2.line(frame,(0,0),(width,height),(0,255,0),10)
    line1 = cv2.line(line,(0,height),(width,0),(0,0,250),10)

    rect = cv2.rectangle(line1,(100,10),(200,300),(123,123,2),5)
    cir = cv2.circle(rect,(300,250),60,(0,0,0),-1)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(frame,'i am kevin',(100,100),font,1,(0,0,0)),cv2.LINE_AA)

    cv2.imshow('line',img)
    if cv2.waitKey(1) == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()