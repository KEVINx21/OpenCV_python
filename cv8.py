import cv2
import numpy as np

def nothing(x):         # placeholder function for creatinga trackbar
    pass

cv2.namedWindow('Trackbars')

cv2.createTrackbar('H', 'Trackbars', 0, 180, nothing)
cv2.createTrackbar('S', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('V', 'Trackbars', 0, 255, nothing)

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h = cv2.getTrackbarPos('H', 'Trackbars')
    s = cv2.getTrackbarPos('S', 'Trackbars')
    v = cv2.getTrackbarPos('V', 'Trackbars')

    lower_hsv = np.array([h, s, v])
    upper_hsv = np.array([180, 255, 255])

    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Original', frame)
    cv2.imshow('Masked', res)

    if cv2.waitKey(1) == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()