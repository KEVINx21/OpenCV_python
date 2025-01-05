# random pixels into image

import cv2
import random

img = cv2.imread('assets/me.jpg')
cv2.imshow('img',img)
img2=cv2.resize(img,(400,400))
print(img2[399,123])

for i in range (100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()