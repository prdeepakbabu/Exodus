#import urllib
#response = urllib.urlopen('https://in.yahoo.com/?p=us')
#html=response.read()
from pyquery import PyQuery as pq
from pymatch import Filter
import urllib2
from os import listdir
import os
import urllib
import urllib2
import Image
import wget
import imghdr
from urlparse import urlparse
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import socket
from random import randint
	
#class HeadRequest(urllib2.Request):
#    def get_method(self):
#        return 'HEAD'
f = Filter(file('easylist.txt'))
writefile = urllib.URLopener()

def getads(file):
	fl=open(file,'r')
	html=fl.read()
	d=pq(html)
	#d=pq(url='https://in.yahoo.com/?p=us')
	x=d('img')
	landing_page=""
	#y=d('title')
	#y=d('a')	
	for i in range(len(x))	: 
		#print x.eq(i).attr('src') 
		#print f.match(x.eq(i).attr('src'))
		try:
			tmp=str(f.match(x.eq(i).attr('src')))
		except:
			tmp="0"			
			pass	
		if  tmp == "1":
			#print file
			tmp_file=file.split(".");
			del tmp_file[-1];
			tmp_file_full=  ".".join(tmp_file) 
			aa=tmp_file_full.split("_");
			time=aa[-1];
			date=aa[-2];
			source=aa[-3];
			url=x.eq(i).attr('src')
			try:
				landing_page=x.eq(i).parent().attr('href')
			except:
				landing_page=""
			if landing_page is  None:
				landing_page="NA"
			try:
				rd=randint(100,900)
				tgtfile="img"+date+time+str(rd)
				localfl=open(tgtfile,"w")
				webrd=urllib2.urlopen(url,None,2)
				localfl.write(webrd.read())
				localfl.close()
				webrd.close()
				#imgtmp= urllib.urlretrieve(url,tgtfile)
				#dl_img=imgtmp[0]
				dl_img=tgtfile				
			except  Exception,e:
				#print str(e)
				dl_img=""
				pass
			if dl_img != "":
				try:
					im=Image.open(dl_img);
					width,height=im.size
					filetype=imghdr.what(dl_img)
					size=os.stat(dl_img).st_size
				except:
					width=0
					height=0
					filetype=""
					size=0
					pass
			else:
				width=0
				height=0
				filetype=""	
				size=0
			#print filetype,size
			if filetype not in ('jpeg','jpg','png','giff','gif','bmp','tiff','tif') or size < 1000:
				try:
					os.remove(dl_img)
				except:
					pass
			else:				
				gauth = GoogleAuth()
				gauth.LoadCredentialsFile("mycreds.txt")
				drive=GoogleDrive(gauth)
				file1=drive.CreateFile()
				file1.SetContentFile(dl_img)
				file1.Upload()
				dl_url = "https://drive.google.com/open?id="+file1['id']
				#print x.eq(i).attr('src'),time,date,source,dl_img,width,height,filetype,size,dl_url
				print str(time) + "|||" + str(date) + "|||" + source + "|||" + dl_img + "|||" + str(width) + "|||" + str(height) + "|||" + filetype + "|||" + str(size) + "|||" + dl_url + "|||" + landing_page




#for i in range(len(y))	: 
	#print y.eq(i).attr('href') 
	#print f.match(x.eq(i).attr('src'))
	#tmp=str(f.match(y.eq(i).attr('href')))
	#if  tmp == "1":
	#	print y.eq(i).attr('href')	

#scrapy startproject getads
#vim items.py
#response.xpath('//img')
#scrapy crawl myads -o data.csv -t csv


#a=['yahoosports.htm','yahoosports2.htm','yahoosports3.htm','yahoosports4.htm','yahoosports5.htm']
#a=['yh_20150816_110947.htm']
#a=["input/"+f for f in listdir("input")]
a=[fx for fx in listdir("input")]
os.chdir("input/")
print os.getcwd()
for i in range(0,len(a)):
	getads(a[i])

#python simple2.py >> url.csv
