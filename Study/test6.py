from pytesseract import Output
import pytesseract
import cv2 as cv

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\ANG7CA\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# reading the image with "imgread"
img = cv.imread("./images/img2.png")

rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)

cv.imshow('image',rgb)

resultado = pytesseract.image_to_data(img,lang='por',output_type=Output.DICT)

print(resultado)


def text_box(resultado, img, cor = (255, 100, 0)):
  x = resultado['left'][i]
  y = resultado['top'][i]
  w = resultado['width'][i]
  h = resultado['height'][i]

  cv.rectangle(img, (x, y), (x + w, y + h), cor, 2)

  return x, y, img

img_copy = rgb.copy()
min_confidence = 40
for i in range(0, len(resultado["text"])):
    confidence = int(resultado["conf"][i])
    if confidence > min_confidence:
        # resgatando a função de contruir a caixa nos textos
        # a função tem acesso a variavel "i" pois ela esta definida no "for"
        x, y, img = text_box(resultado, img_copy)
        
        text = resultado["text"][i]

        cv.putText(img_copy,text, (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 1.1, (0,100, 255))
        
        print("X:"+str(x), "Y:"+str(y))

cv.imshow("Image copy",img_copy)        

cv.waitKey(0)

