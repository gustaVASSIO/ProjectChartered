import cv2 as cv

largura, altura = 320, 320

detector = "./frozen_east_text_detection.pb"

min_confidence = 0.9

img = cv.imread('./Imagens/caneca.jpg')

origin = img.copy()

# print(img.shape)

H = img.shape[0]
W = img.shape[1]

proportion_w = W/float(largura)
proportion_h = H/float(largura)

img = cv.resize(img, (largura, altura))
H = img.shape[0]
W = img.shape[1]


# print(img.shape)

names_layers = ['feature_fusion/Conv_7/Sigmoid', 'feature_fusion/concat_3']

neural_network = cv.dnn.readNet(detector)

blob = cv.dnn.blobFromImage(img, 1.0, (W, H), swapRB=True, crop=False)

# print(blob.shape) 
neural_network.setInput(blob)
scores, gometry = neural_network.forward(names_layers)
# scores => indica as probabilidades de textos estarem presentes em determinada parte da imagem
# geometry => indica as posições dos valores reconhecidos na imagem

lines, columns = scores.shape[2:4]


cv.imshow("IMG",img)

cv.waitKey(0)