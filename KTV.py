# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import time
import random
#import pymongo
#from pymongo import MongoClient
from BeautifulSoup import BeautifulSoup
#import grep

def GetData(appName):
	result = []
	post={}
	post['Chk_LangCode'] = 1
	post['LangCode'] = 4
	post['Order_Num'] = 10
	#post['Page'] = 3

	url = 'http://www.cashboxparty.com/mysong/MySong_Search_R.asp'

	for page in range(0,90):
		post['Page'] = page
		print page
		try:
			data = urllib.urlencode(post)																		
			html = urllib2.urlopen(url,data).read()
			result.append( html )
		except:
			pass
		time.sleep(random.randint(2,3))

	return result

def Filter(data):
	check = 1
	author = []
	song = []

	soup = BeautifulSoup(''.join(data))
	Name = soup.findAll(attrs={"style":"text-align: left; height: 26px;"})
	
	for index, line in enumerate(Name, 1):
		if index % 2 == 1:
			author.append( line.string.strip() )
		if index % 2 == 0:
			song.append( line.string.strip() )

	if len( author ) == len( song ):
		result = [(x,y) for x,y in zip(author,song)]


	return result
		


def Process(appName):
	data = GetData(appName)
	result = Filter(data)
	Output(result)

def Output(data):
	g = open("out.txt","w")
	#print data
	for line in data:
		author = line[0].encode("utf-8").strip()
		song = line[1].encode("utf-8").strip()
		g.write( author + ":" + song + "\n")

	g.close()
		

if __name__ == '__main__':
	Process("appName")
	#for appName in applist:
		#time.sleep(random.randint(10,20))
		