import parse
import time
import os
import datetime
import codecs
import getpass
import json
# import urllib2
from bs4 import BeautifulSoup
import requests

#sudo apt-get install xvfb and pip install pyvirtualdisplay to run it in background
#from pyvirtualdisplay import Display
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def attendance(username,password):
#	display = Display(visible=0, size=(800, 600))
#	display.start()

	baseurl = "http://academicscc.vit.ac.in/student/stud_login.asp"
	regno = username
	passwd = password


	xpaths = { 'usernameTxtBox' : "html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input[@name='regno']",
	           'passwordTxtBox' : "html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input[@name='passwd']",
	           'captchaTxtBox' : "html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[5]/td/input[@name='vrfcd']",
		   'submitButton' :   "html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[6]/td/input[1]"
	         }

#	mydriver = webdriver.Firefox()
	mydriver = webdriver.PhantomJS()
	mydriver.set_window_size(1120, 550)
	test = mydriver.get(baseurl)
	#mydriver.maximize_window() this stopped working, dont know why. will check this later
	

	mydriver.execute_script('document.getElementById("imgCaptcha").oncontextmenu = "return true"')


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

	time.sleep(3)

	#adding info like date and current semester to the URL's
	fromdate = "01-Jan-2017"
	todate = datetime.date.today().strftime ("%d-%b-%Y")
	month = datetime.datetime.now().strftime("%m")
	sem="FS"
	if 1<=month and month<=6 or month==12:
		sem="WS"
	elif month>=7 and month <=11:
		sem="FS"

	#URL for student profile - html/body/table/tbody/tr/td[2]/table[3]/tbody/tr[2]/td[2]
	profileurl = "https://academicscc.vit.ac.in/student/profile_personal_view.asp"
	#URL for timetable
	timetableurl = "https://academicscc.vit.ac.in/student/course_regular.asp?sem="+sem
	#URL for CAT marks (whenever available)
	marksurl = "https://academicscc.vit.ac.in/student/marks.asp?sem="+sem
	#URL for Academic History
	historyurl = "https://academicscc.vit.ac.in/student/student_history.asp"
	#URL for attendance
	attendanceurl = "https://academicscc.vit.ac.in/student/attn_report.asp?sem="+sem+"&fmdt="+fromdate+"&todt="+todate
	
	mydriver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
	mydriver.get(attendanceurl)
	html_source = mydriver.page_source

	filename=regno+".html"
	text_file = codecs.open(filename, "w", 'utf-8')
	text_file.write(html_source)
	text_file.close()
	result =[[] for i in range(8)]
	result = parse.parseatt(filename)
	mydriver.quit()

	return result