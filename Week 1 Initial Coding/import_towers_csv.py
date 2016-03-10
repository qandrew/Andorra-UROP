# March 3rd 2016 starting to import the data
import os
import csv 
import platform

if platform.system() == 'Windows':
	os.chdir('C:\Users\Andrew\Dropbox (MIT)\Yan_Andrew')
elif platform.system() == 'Linux': #i am operating on my linux
	os.chdir('/home/andrew/Dropbox (MIT)/Yan_Andrew/')
	#print os.getcwd()

#import data
towerscsv = []
with open('towers.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		a = str(row)[2:-2].split(',')
		#print a
		towerscsv.append(a)

#print towerscsv
