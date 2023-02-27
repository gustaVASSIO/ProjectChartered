import cv2 as cv
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\ANG7CA\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# success
img = cv.imread("./Section3/images/img8.png")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

val, thresh = cv.threshold(gray, 180, 255, cv.THRESH_BINARY)
print(val) 

invert = 255 - thresh

# implements ocr
result = pytesseract.image_to_string(invert, lang='por')

cv.imshow("Img", img)
cv.imshow("Thresh",thresh)
cv.imshow("Invert", invert)

cv.waitKey(0)
