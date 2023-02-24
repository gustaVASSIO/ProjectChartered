import cv2 as cv

img = cv.imread('./Section3/images/img3.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Neste caso o metodo de otsu não é o melhor para essa imagem, pois
# ela possui pontos de luminosidades diferentes, sendo necessário colocar
# mais de um intervalo de limiarização para ele funcionar

# A limiarização adaptativa é utilizada para imagens que possuem pontos de luminosidades diferentes
val, thresh = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)
adaptive_media = cv.adaptiveThreshold(gray, 255, adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv.THRESH_BINARY, blockSize=11, C=9)

cv.imshow("OTSU",thresh)
print(val)
cv.imshow("Adaptive",adaptive_media)




cv.waitKey(0)