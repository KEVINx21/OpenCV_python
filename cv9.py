import cv2

img = cv2.imread('assets/soccer_practice.jpg', 0) # 0 to directly display BW img
temp = cv2.imread('assets/ball.PNG', 0)

h, w = temp.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img1 = img.copy()

    res = cv2.matchTemplate(img1, temp, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img1, location, bottom_right, 255, 3)

    cv2.imshow(f"Match using {method}", img1)
    cv2.waitKey(0)

cv2.destroyAllWindows()
