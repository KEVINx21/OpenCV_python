import numpy as np
import cv2

lower = {'red':([0, 100, 80]),'green':([50, 50, 120]),'blue':([97, 100, 117]),'yellow':([23, 59, 119]),'orange':([0, 50, 80]),'purple':([130, 80, 80]),"light blue":([60,130,35])}
upper = {'red': ([14, 255, 255]), 'green': ([70, 255, 255]), 'blue': ([117,255, 255]), 'yellow': ([54, 255, 255]),'orange': ([20, 255, 255]), 'purple': ([150, 255, 255]),
         "light blue": ([130, 255, 246])}
colors = {'yellow': (0, 255, 217), 'red': (0, 0, 255), 'blue': (255, 0, 0),'green': (0, 255, 0),'orange': (0, 140, 255), 'purple': (211, 0, 148), "light blue":(255, 213, 15)}

frame = cv2.imread("imagegog.png")
blurred = cv2.GaussianBlur(frame, (11, 11), 0)
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
mlist = []
clist = []
ks = []

for (key, value) in upper.items():
    kernel = np.ones((2, 2), np.uint8)
    mask = cv2.inRange(hsv, np.array(lower[key]), np.array(upper[key]))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.dilate(mask, kernel, iterations=1)
    mlist.append(mask)
    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) >= 1:
       clist.append(contours[-1])
       ks.append(key)

for i, cnt in enumerate(clist):
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    x, y, w, h = cv2.boundingRect(cnt)

    if len(approx) == 3:
        cv2.putText(frame, ks[i] + " Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.1, colors[ks[i]], 2)
    elif len(approx) == 4:
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            cv2.putText(frame, ks[i] + " Square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, colors[ks[i]], 2)
        else:
            cv2.putText(frame, ks[i] + " Rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, colors[ks[i]], 2)
    elif len(approx) == 5:
        cv2.putText(frame, ks[i] + " Pentagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, colors[ks[i]], 2)
    else:
        cv2.putText(frame, ks[i] + " Circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, colors[ks[i]], 2)

cv2.imshow("Frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
