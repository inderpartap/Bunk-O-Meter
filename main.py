import parse

import time
import os
import datetime
import codecs
#import cv2
#from PIL import Image
import getpass

import urllib2
from bs4 import BeautifulSoup
import requests

#sudo apt-get install xvfb and pip install pyvirtualdisplay to run it in background
from pyvirtualdisplay import Display
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

display = Display(visible=0, size=(800, 600))
display.start()

baseurl = "http://academicscc.vit.ac.in/student/stud_login.asp"
regno = raw_input("Registration Number: ")
passwd = getpass.getpass('Password:')


xpaths = { 'usernameTxtBox' : "html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input[@name='regno']",
           'passwordTxtBox' : "html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input[@name='passwd']",
           'captchaTxtBox' : "html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[5]/td/input[@name='vrfcd']",
	   'submitButton' :   "html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[6]/td/input[1]"
         }

mydriver = webdriver.Firefox()
test = mydriver.get(baseurl)
mydriver.maximize_window()

mydriver.execute_script('document.getElementById("imgCaptcha").oncontextmenu = "return true"')


# now that we have the preliminary stuff out of the way time to get that image :D
#element = mydriver.find_element_by_xpath(".//*[@id='imgCaptcha']") # finding part of the captcha
#location = element.location
#size = element.size
#mydriver.save_screenshot('screenshot.jpg') # save screenshot of entire page


#im = Image.open('screenshot.jpg') # uses PIL library to open image in memory

#left = location['x']
#top = location['y']
#right = location['x'] + size['width']
#bottom = location['y'] + size['height']


#im = im.crop((left, top, right, bottom)) # define crop points
#im.save('screenshot.jpg') # save new cropped image


#Clear Username TextBox if already allowed "Remember Me" 
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

#Write Username in Username TextBox
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(regno)

#Clear Password TextBox if already allowed "Remember Me" 
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

#Write Password in password TextBox
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(passwd)

#autofill captcha
mydriver.execute_script(open("./captcha.js").read())

#Get Captcha from the user
#vrfcd = raw_input("Please enter the captcha: ")

#Clear Captcha TextBox if already allowed "Remember Me" 
#mydriver.find_element_by_xpath(xpaths['captchaTxtBox']).clear()

#Write Captcha in captcha TextBox
#mydriver.find_element_by_xpath(xpaths['captchaTxtBox']).send_keys(vrfcd)

#Click Login button
mydriver.find_element_by_xpath(xpaths['submitButton']).click()

time.sleep(1)

fromdate = "01-Jan-2017"
todate = datetime.date.today().strftime ("%d-%b-%Y")
attendanceurl = "https://academicscc.vit.ac.in/student/attn_report.asp?sem=WS&fmdt="+fromdate+"&todt="+todate
mydriver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
mydriver.get(attendanceurl)
html_source = mydriver.page_source

filename=regno+".html"
text_file = codecs.open(filename, "w", 'utf-8')
text_file.write(html_source)
text_file.close()

parse.parseatt(filename)

mydriver.quit()
display.stop()