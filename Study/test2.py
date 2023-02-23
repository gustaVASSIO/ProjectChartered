import pytesseract
import numpy as np
import cv2
from cv2 import imshow
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\ANG7CA\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# reading the image with "imgread"
img = cv2.imread("./images/img3.png")

rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imshow('image',rgb)

config_tesseract = '--psm 6'
text = pytesseract.image_to_string(rgb,lang='por', config=config_tesseract)
print(text)

cv2.waitKey(0)