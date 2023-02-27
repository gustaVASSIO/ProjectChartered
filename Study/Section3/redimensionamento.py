import cv2 as cv

img = cv.imread('./Section3/images/img1.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

bigger1 = cv.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv.INTER_CUBIC)
# bigger2 = cv.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv.INTER_LINEAR)
# bigger3 = cv.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv.INTER_AREA)
# bigger4 = cv.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv.INTER_NEAREST)
# bigger5 = cv.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv.INTER_LANCZOS4)

smaller = cv.resize(gray, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)

cv.imshow("Gray",gray)

cv.imshow("Maior 1",bigger1)
# cv.imshow("Maior 2",bigger2)
# cv.imshow("Maior 3",bigger3)
# cv.imshow("Maior 4",bigger4)
# cv.imshow("Maior 5",bigger5)

cv.imshow("Menor", smaller)

cv.waitKey(0)