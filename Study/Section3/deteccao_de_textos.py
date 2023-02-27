import cv2 as cv 
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\ANG7CA\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

img = cv.imread('./Section3/images/img3.png')

# implementando tratamento de imagens
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# fail
# val, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

limiarImg = cv.adaptiveThreshold(gray, 255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv.THRESH_BINARY, blockSize=11, C=9)

bigger = cv.resize(limiarImg, None, fx=1.1, fy=1.1, interpolation=cv.INTER_CUBIC)

# fail
# erode = cv.erode(gray, np.ones((5,5), np.uint8))

filter_binary = cv.bilateralFilter(bigger, 15, 55, 45)

# implementando o reconhecimento de textos
result = pytesseract.image_to_string(bigger, lang='por', config='--psm 6')
print(result)

cv.imshow("Adaptative Median Limiar",limiarImg)
cv.imshow("Adaptative Median Limiar Resized",bigger)
cv.imshow("Adaptative Median Limiar Erode",filter_binary)


cv.waitKey(0)