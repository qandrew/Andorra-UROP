# Andrew Xia
# March 15 2016
# importing Data for Andorra Media Lab UROP
# goal: make sure i can import a csv file correctly

import os
import csv 

#import data
towers_id = {}
with open('towers_id_dict.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	# i = 0
	for row in spamreader:
		print row
		data = str(row)[2:-2].split(',')
		try:
			towers_id[int(data[0])] = int(data[1])
		except ValueError:
			pass

print towers_id