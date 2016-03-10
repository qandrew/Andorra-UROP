# March 4 2016 starting to import the data
# Andrew Xia

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
with open('20151120-towersContainerTrip2.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		#print row
		#print len(row)
		towerscsv.append(row)

print towerscsv[1]
print towerscsv[1][9]

def categorize_tower_types(data):
	returndict = {}
	#key is category code, value is list of place_id
	for i in xrange(1,len(data)):
		nums = data[i][9].split(',') #column of category code
		for j in xrange(len(nums)):
			try:
				if int(nums[j]) in returndict.keys():
					returndict[int(nums[j])].append(data[i][0])
				else:
					#not in, create new
					returndict[int(nums[j])] = [data[i][0]]
			except ValueError:
				pass
	return returndict

test = categorize_tower_types(towerscsv)
print len(test[1])
