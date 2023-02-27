import cv2 as cv

import numpy as np

#img = cv.imread("./Section3/images/img5.png")
img = cv.imread("./Section3/images/img6.png")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# EROSÂO               #Kernel        #tipo da matriz do kernel  
# erode = cv.erode(gray, np.ones((5,5), dtype=np.uint8))

# DILATAÇÃO
dilate = cv.dilate(gray, np.ones((3,3), np.uint8))

#Abertura - consiste em aplicar a erosão e a dilatação em sequência
erode = cv.erode(gray, np.ones((5,5), dtype=np.uint8))
open = cv.dilate(gray, np.ones((5,5)))

#Fechamento - consistemem aplicar a dilatação e a erosão em sequência
open = cv.dilate(gray, np.ones((5,5)))
erode = cv.erode(open, np.ones((5,5), dtype=np.uint8))

cv.imshow("gray", gray)

cv.imshow("Erode Img",erode)

cv.imshow("Dilate Img",open)

cv.waitKey(0)