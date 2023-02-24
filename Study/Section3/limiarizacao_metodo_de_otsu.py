import cv2 as cv

img = cv.imread('./Section3/images/img2.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

val, thresh = cv.threshold(gray,0, 255, cv.THRESH_OTSU)

cv.imshow("Image",thresh)

print(val)

cv.waitKey(0)