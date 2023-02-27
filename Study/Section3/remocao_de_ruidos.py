import cv2 as cv

img = cv.imread('./Section3/images/img7.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Desfoque Média - utliza a média dos pixeis da imagem
desfoque_media = cv.blur(gray, (5,5))

# Desfoque Gaussiano - desfoca majoritariamente o centro da imagem
desfoque_gaussiano = cv.GaussianBlur(src=gray, ksize=(5,5), sigmaX=0)

# Desfoque por Mediana - pega o valor da mediana entre os pixeis do recorte da imagem
desfoque_mediana = cv.medianBlur(gray, 5)

# Desfoque por filtro
desfoque_filtro = cv.bilateralFilter(gray, 15, 55, 45)
cv.imshow("Image", gray)
cv.imshow("Desfoque Media", desfoque_media)
cv.imshow("Desfoque Gaussiano", desfoque_gaussiano)
cv.imshow("Desfoque Mediana", desfoque_mediana)
cv.imshow("Desfoque Bilateral", desfoque_filtro)
cv.waitKey(0)