import cv2 as cv
import numpy as np

img = cv.imread('./Section3/images/img1.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Image",img)
cv.imshow("Gray",gray)
cv.waitKey(0)