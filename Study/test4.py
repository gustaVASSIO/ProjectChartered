from PIL import Image
import pytesseract
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\ANG7CA\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

img = Image.open(r"S:\PM\ter\ets\Inter_Setor\COMPARTILHADO\APRENDIZES\MEIO_OFICIAIS\GUSTAVO_SANTIMARIA_ANACLETO\ProjectChartered\Study\images\img5.png")


plt.imshow(img)

# error
config_tesseract = "--dpi"
print(pytesseract.image_to_osd(img,config='--psm 3'))

plt.waitforbuttonpress(0)