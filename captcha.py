import cv2.cv as cv
import pytesseract

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