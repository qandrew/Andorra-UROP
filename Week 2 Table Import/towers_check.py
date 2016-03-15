# March 4 2016
# Andrew Xia importing Data for Andorra Media Lab UROP
# input: towers.csv. 
# goal: as each tower may have multiple IDs, we will create a data structure
# to check if ID has a duplicate; if so, use the lowest value for the tower ID. 
# generates tower_id_dict.csv

import os
import csv 

#import data
towers_by_loc = {}
towers_id = {}
with open('../../towers.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	# i = 0
	for row in spamreader:
		#print row
		data = str(row)[2:-2].split(',')
		try:
			#print data[1]
			if (float(data[1]),float(data[2])) not in towers_by_loc.keys():
				towers_by_loc[(float(data[1]),float(data[2]))] = [int(data[0])]
			else:
				towers_by_loc[(float(data[1]),float(data[2]))].append(int(data[0]))
		except ValueError:
			pass

		# i += 1
		# if i >= 20:
		# 	break

print len(towers_by_loc)

for location in towers_by_loc:#
	samelist = towers_by_loc[location]
	samelist.sort()
	for iden in samelist:
		towers_id[iden] = samelist[0]
		#set lowest value

print "towers id, ", towers_id
print "by location, ", towers_by_loc

with open('towers_id_dict.csv', 'w') as csvfile:
    fieldnames = ['tower_id','lowest_key']
    # person, start time, end time, cell tower, call number, phone type
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for iden in towers_id:
    	writer.writerow({'tower_id':iden, 'lowest_key':towers_id[iden]})

print 'completed'
