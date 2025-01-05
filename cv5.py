import numpy as np
import cv2

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    image = np.zeros(frame.shape, np.uint8)
    width = int(vid.get(3))
    height = int(vid.get(4))

    smaller_frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)

    image[height//2: , width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[:height//2 , :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2: ,:width//2] = smaller_frame
    image[:height//2 , width//2:] = smaller_frame
    
    cv2.imshow('frame',image)

    if cv2.waitKey(1)== ord('q'):
        break

vid.release()
cv2.destroyAllWindows()