import cv2.cv as cv
import pytesseract
<<<<<<< HEAD

from PIL import Image

img = Image.open('captcha.bmp')
img = img.convert("RGBA")

pixdata = img.load()
	 


for y in xrange(img.size[1]):
 	for x in xrange(img.size[0]):
 		if pixdata[x, y][0] < 90:
 			pixdata[x, y] = (0, 0, 0, 255)

for y in xrange(img.size[1]):
 	for x in xrange(img.size[0]):
 		if pixdata[x, y][1] < 136:
 			pixdata[x, y] = (0, 0, 0, 255)

for y in xrange(img.size[1]):
 	for x in xrange(img.size[0]):
 		if pixdata[x, y][2] > 0:
 			pixdata[x, y] = (255, 255, 255, 255)

img.save("input-black.gif", "GIF")

#   Make the image bigger (needed for OCR)
im_orig = Image.open('input-black.gif')
big = im_orig.resize((116, 56), Image.NEAREST)
ext = ".tif"
big.save("input-NEAREST" + ext)
	
#   Perform OCR using pytesser library
from pytesseract import *
image = Image.open('input-NEAREST.tif')
print image_to_string(image)
=======
gray = cv.LoadImage('.\gray1_captcha.png', cv.CV_LOAD_IMAGE_GRAYSCALE)
cv.Threshold(gray, gray, 231, 255, cv.CV_THRESH_BINARY)
api = pytesseract.TessBaseAPI()
api.Init(".","eng",tesseract.OEM_DEFAULT)
api.SetVariable("tessedit_char_whitelist", "0123456789abcdefghijklmnopqrstuvwxyz")
api.SetPageSegMode(tesseract.PSM_SINGLE_WORD)
pytesseract.SetCvImage(gray,api)
print api.GetUTF8Text()
>>>>>>> 93a39b1381b52a3430a747b5b4623fc346335bfa
