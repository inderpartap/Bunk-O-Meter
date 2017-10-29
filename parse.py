# import urllib2
from bs4 import BeautifulSoup
import requests
from array import *
from operator import truediv
import math
import numpy as np


def parseatt(user):
	page = open(user)
	soup =  BeautifulSoup(page, "html.parser")
	page.close()
	#print(soup.prettify())
	#print soup('table')[4].prettify() 
	c=0
	for row in soup('table')[4].findAll('tr'):
	    tds = row('td')
	    c = c+1

	result =[[] for i in range(8)]

	#Course Code
	i=1
	ccode=[]
	for i in range(1,c):
		ccode.append(soup('table')[4].findAll('tr')[i].findAll('td')[1].string)
	result[0] = ccode

	#Course Name
	i=1
	cname=[]
	for i in range(1,c):
		cname.append(soup('table')[4].findAll('tr')[i].findAll('td')[2].string)
	result[1] = cname

	#Course Type
	i=1
	ctype=[]
	for i in range(1,c):
		ctype.append(soup('table')[4].findAll('tr')[i].findAll('td')[3].string)
	result[2] = ctype

	#Class Attended
	i=1
	attend=[]
	for i in range(1,c):
		attend.append(float(int(soup('table')[4].findAll('tr')[i].findAll('td')[6].string)))
	attend = np.array(attend)

	#Total Classes
	i=1
	total=[]
	for i in range(1,c):
		total.append(float(int(soup('table')[4].findAll('tr')[i].findAll('td')[7].string)))
	total = np.array(total)

	#Calculating Attendance
	attendance= (attend/total)*100
	attendance = np.ceil(np.array(attendance)).astype(int)
	for i in range(0,c-1):
		if (attendance[i] < 0):
			attendance[i]=0
	result[3] = attendance
	# print attendance

	#Attendance if you go today
	att_going = ((attend+1)/(total+1))*100
	att_going = np.ceil(np.array(att_going)).astype(int)
	result[4] = att_going
	# print att_going

	#Attendance if you miss today
	att_miss = ((attend)/(total+1))*100
	i=0
	for i in range(0,c-1):
		if (ctype[i] == "Embedded Lab"):
			att_miss[i] = ((attend[i])/(total[i]+2))*100
	att_miss = np.ceil(np.array(att_miss)).astype(int)
	result[5] = att_miss
	# print att_miss


	#How many classes you can miss
	no_miss = ((attend/0.75)-total)
	i=0
	for i in range(0,c-1):
		if (ctype[i] == "Embedded Lab"):
			no_miss[i] = ((attend[i]/0.75)-total[i])/2
		if (no_miss[i]<0):
			no_miss[i]=0

	no_miss = np.floor(np.array(no_miss)).astype(int)
	result[6] = no_miss
	# print no_miss

	#If debarred, no. of classes you need to attend
	no_bar = (((0.75*total)-attend)/0.25)
	no_bar = np.ceil(np.array(no_bar)).astype(int)
	i=0
	for i in range(0,c-1):
		if (no_bar[i]<0):
			no_bar[i]=0
	result[7] = no_bar
	# print no_bar

	return result


def parsetimetable():
	return 0
def parsemarks():
	return 0
def parsehistory(user):
	page = open(user)
	soup =  BeautifulSoup(page, "html.parser")
	page.close()
	c=0
	for row in soup('table')[2].findAll('tr'):
	    tds = row('td')
	    c = c+1

	result =[[] for i in range(7)]

	#Sl. No.
	i=1
	slno=[]
	for i in range(1,c):
		slno.append(soup('table')[2].findAll('tr')[i].findAll('td')[0].string)
	result[0] = slno

	#Course Code
	i=1
	ccode=[]
	for i in range(1,c):
		ccode.append(soup('table')[2].findAll('tr')[i].findAll('td')[1].string)
	result[1] = ccode

	#Course Name
	i=1
	cname=[]
	for i in range(1,c):
		cname.append(soup('table')[2].findAll('tr')[i].findAll('td')[2].string)
	result[2] = cname

	#Course Type
	i=1
	ctype=[]
	for i in range(1,c):
		ctype.append(soup('table')[2].findAll('tr')[i].findAll('td')[3].string)
	result[3] = ctype

	#Credits
	i=1
	credit=[]
	for i in range(1,c):
		credit.append(soup('table')[2].findAll('tr')[i].findAll('td')[4].string)
	result[4] = credit

	#Grade
	i=1
	grade=[]
	for i in range(1,c):
		grade.append(soup('table')[2].findAll('tr')[i].findAll('td')[5].string)
	result[5] = grade

	#Course Exam date
	i=1
	exdate=[]
	for i in range(1,c):
		exdate.append(soup('table')[2].findAll('tr')[i].findAll('td')[6].string)
	result[6] = exdate


	#credit detials
	c=4
	credits =[[] for i in range(1)]
	i=1
	creditregis=[]
	for i in range(0,c):
		creditregis.append(soup('table')[3].findAll('tr')[1].findAll('td')[i].string)
	credits[0] = creditregis

	return result,credits
if __name__ == '__main__':
    parseatt()
