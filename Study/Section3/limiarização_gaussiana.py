import cv2 as cv

img = cv.imread('./Section3/images/img4.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

adaptive_media = cv.adaptiveThreshold(gray, 255, adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv.THRESH_BINARY, blockSize=11, C=9)

adaptive_gaussian = cv.adaptiveThreshold(gray, 255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv.THRESH_BINARY, blockSize=11, C=9)

cv.imshow("Adaptive Media",adaptive_media)

cv.imshow("Adaptive Gaussian",adaptive_gaussian)

cv.waitKey(0)