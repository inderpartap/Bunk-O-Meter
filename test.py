import time
import os
import datetime
import codecs
import cv2

import urllib2
from bs4 import BeautifulSoup
import requests

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

baseurl = "http://academicscc.vit.ac.in/student/stud_login.asp"
regno = raw_input("Registration Number: ")
passwd = raw_input("Password: ")


xpaths = { 'usernameTxtBox' : "html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input[@name='regno']",
           'passwordTxtBox' : "html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input[@name='passwd']",
           'captchaTxtBox' : "html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[5]/td/input[@name='vrfcd']",
	   'submitButton' :   "html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[6]/td/input[1]"
         }

mydriver = webdriver.Firefox()
test = mydriver.get(baseurl)
mydriver.maximize_window()

mydriver.execute_script('document.getElementById("imgCaptcha").oncontextmenu = "return true"')


#taking screenshot to save the captcha
mydriver.save_screenshot("screenshot.png")
img = cv2.imread("screenshot.png")
crop_img = img[280:320, 650:800] # Crop from x, y, w, h -> 100, 200, 300, 400
# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)
cv2.imwrite('captcha.png',crop_img)
gray_image = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_captcha.png',gray_image)


#Clear Username TextBox if already allowed "Remember Me" 
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

#Write Username in Username TextBox
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(regno)

#Clear Password TextBox if already allowed "Remember Me" 
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

#Write Password in password TextBox
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(passwd)

#Get Captcha from the user
vrfcd = raw_input("Please enter the captcha: ")

#Clear Captcha TextBox if already allowed "Remember Me" 
mydriver.find_element_by_xpath(xpaths['captchaTxtBox']).clear()

#Write Captcha in captcha TextBox
mydriver.find_element_by_xpath(xpaths['captchaTxtBox']).send_keys(vrfcd)

#Click Login button
mydriver.find_element_by_xpath(xpaths['submitButton']).click()

time.sleep(1)

fromdate = "01-Jan-2017"
todate = datetime.date.today().strftime ("%d-%b-%Y")
attendanceurl = "https://academicscc.vit.ac.in/student/attn_report.asp?sem=WS&fmdt="+fromdate+"&todt="+todate
mydriver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
mydriver.get(attendanceurl)
html_source = mydriver.page_source

text_file = codecs.open("attendance.html", "w", 'utf-8')
text_file.write(html_source)
text_file.close()

