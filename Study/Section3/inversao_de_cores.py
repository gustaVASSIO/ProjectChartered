import cv2 as cv

img = cv.imread('./Section3/images/img1.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# para o tesseract é melhor a imagem estar com o fundo branco e o texto preto
# por conta disso implementa-se a inversão de cores na imagem de escala cinza

imgInvert  = 255 - gray



cv.imshow("Gray",gray)
cv.imshow("Img Invert",imgInvert)

cv.waitKey(0)