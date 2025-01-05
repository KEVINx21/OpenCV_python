#basic image loaing and saving

import cv2

img = cv2.imread('assets/me.jpg')
img = cv2.resize(img,(400,400 ))
cv2.imshow('img',img)
cv2.imwrite('new1.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()