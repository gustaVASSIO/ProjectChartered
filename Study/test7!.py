import re
from pytesseract import Output
import pytesseract
import cv2 as cv

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\ANG7CA\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# reading the image with "imgread"
img = cv.imread("./images/img7.png")

rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)

result = pytesseract.image_to_data(img, lang='por', output_type=Output.DICT)


def text_box(result, img, color=(0,100,255)):
    x = result["left"][i]
    y = result["top"][i]
    w = result["width"][i]
    h = result["height"][i]
    cv.rectangle(img, (x,y), (x+w,y+h), color, 2)
    return x, y, img

regular_expression_data = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'

img_copy = rgb.copy()

min_conf = 40

for i in range(0,len(result["text"])):
    confidence = int(result["conf"][i])
    if  confidence > min_conf:#filtrando palavras 
        text = result["text"][i]
        # print(text)
        if re.match(regular_expression_data, text):
            x, y, img = text_box(result, img_copy)

        
        

cv.imshow("Image",rgb)
cv.imshow("Image",img_copy)

cv.waitKey(0)