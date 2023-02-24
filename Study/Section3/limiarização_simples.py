import cv2 as cv

img = cv.imread('./Section3/images/img2.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# para o metodo "threshold" é necessário fornecer como parâmetros:
# - A imagem
# - O valor de limiarização
# - O valor que os pixels irão assumir se eles estiverem acima ou abaixo desse parâmetro 
val, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)


cv.imshow("Image",thresh)

cv.waitKey(0)