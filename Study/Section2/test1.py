import pytesseract
import numpy as np
import cv2
from cv2 import imshow
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\ANG7CA\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
# reading the image with "imgread"
img = cv2.imread("./images/img2.png")

# showing the image with "imgshow"
# cv2.imshow('Image',img)

# inicialmente a imagem esta em formato BGR
# então utiliza-se o metodo "cvtColot" para transformar para RGB
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imshow('image',rgb)

text = pytesseract.image_to_string(rgb,lang='por')
print(text)

cv2.waitKey(0)