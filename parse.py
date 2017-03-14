import urllib2
from bs4 import BeautifulSoup
import requests
from array import *
from operator import truediv
import math
import numpy as np

page = open('attendance.html')
soup =  BeautifulSoup(page, "html.parser")
page.close()
#print(soup.prettify())

#print soup('table')[4].prettify() 
c=0
for row in soup('table')[4].findAll('tr'):
    tds = row('td')
    c = c+1

#Course Code
i=1
ccode=[]
for i in range(1,c):
	ccode.append(soup('table')[4].findAll('tr')[i].findAll('td')[1].string)

#Course Name
i=1
cname=[]
for i in range(1,c):
	cname.append(soup('table')[4].findAll('tr')[i].findAll('td')[2].string)

#Course Type
i=1
ctype=[]
for i in range(1,c):
	ctype.append(soup('table')[4].findAll('tr')[i].findAll('td')[3].string)

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
print attendance

#Attendance if you go today
att_going = ((attend+1)/(total+1))*100
att_going = np.ceil(np.array(att_going)).astype(int)
print att_going

#Attendance if you miss today
att_miss = ((attend)/(total+1))*100
att_miss = np.ceil(np.array(att_miss)).astype(int)
print att_miss

#How many classes you can miss
no_miss = ((attend/0.75)-total)
no_miss = np.floor(np.array(no_miss)).astype(int)
i=0
for i in range(0,c-1):
	if (no_miss[i]<0):
		no_miss[i]=0

print no_miss

#If debarred, no. of classes you need to attend
no_bar = (((0.75*total)-attend)/0.25)
no_bar = np.ceil(np.array(no_bar)).astype(int)
i=0
for i in range(0,c-1):
	if (no_bar[i]<0):
		no_bar[i]=0
print no_bar
