
from pytesseract import Output
import pytesseract
import cv2 as cv

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\ANG7CA\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# reading the image with "imgread"
img = cv.imread("./Section2//images/img8.png")

rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)

config_tesseract = '--psm 11'

result =  pytesseract.image_to_data(rgb, lang='eng',output_type=Output.DICT, config=config_tesseract)

print(result)

def text_box(result, img, color=(0,100,255)):
    x = result["left"][i]
    y = result["top"][i]
    w = result["width"][i]
    h = result["height"][i]
    cv.rectangle(img, (x,y), (x+w,y+h), color, 2)
    return x, y

img_copy = rgb.copy()

min_conf = 40

for i in range(0,len(result["text"])):
    confidence = int(result["conf"][i])
    if  confidence > min_conf:#filtrando palavras 
        text = result["text"][i]
        x, y = text_box(result, img_copy)
        cv.putText(img_copy,text, (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,100, 255))
        

cv.imshow("Image",img)
cv.imshow("Image",img_copy)

cv.waitKey(0)