#replacing Pixels

import cv2

img = cv2.imread('assets/me.jpg')
img1=cv2.resize(img,(400,400))

tag = img1[250:350, 250:350]
img1[120:220, 120:220]=tag

cv2.imshow('new',img1)
cv2.waitKey()
cv2.destroyAllWindows()