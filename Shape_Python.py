import numpy as np
import cv2

#Load the image
img = cv2.imread("inp_img.png")

#Convert image to grayscale
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Apply thresholding
_, thrash = cv2.threshold (imgGrey, 240, 255, cv2.THRESH_BINARY)

#Find contours
contours,_ = cv2.findContours (thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#Draw shapes based on contours

for contour in contours:
    #Approximate the contour
    approx = cv2.approxPolyDP (contour, 0.01 *cv2.arcLength (contour, True), True)
    #Draw contour
    cv2.drawContours (img, (approx), 0, (0, 0, 0), 5)
    #Get position for putting text
    x= approx.ravel()[0]
    y= approx.ravel() [1] -5
    
    if len(approx)==3:
        cv2.putText (img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) ==4:
        xl, yl, w, h= cv2.boundingRect(approx)
        aspectRatio = float(w) /h
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText (img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx)== 5:
        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) ==10:
        cv2.putText (img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        cv2.putText (img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))


cv2.imshow("shapes", img)
cv2.waitKey(0)
