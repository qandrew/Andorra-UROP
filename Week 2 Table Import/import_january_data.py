# March 4 2016
# Andrew Xia importing Data for Andorra Media Lab UROP
# input: DWFET_CDR_CELLID_201501.csv. 
# we want day, city, hour, cell phone tower (and others also)


import os
import csv 
print 'started'

# print os.getcwd()
#os.chdir('/run/user/1000/gvfs/sftp:host=andorra.media.mit.edu/home/data_commons/cdrs')
#print os.getcwd()

#import data
people_data = {}
with open('../data_commons/cdrs/DWFET_CDR_CELLID_201501.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	# firstrow = True
	# i = 0
	for row in spamreader:
		# if i >= 20:
		# 	break
		# i += 1
		if row[0] not in people_data.keys(): #not a duplicate
			person_data = row[3], row[4],  row[6], row[-3], row[-1]
			people_data[row[0]] = person_data
			#key = person
			#value = start time, finish time, cell tower, number called, kind of phone

#print people_data
#print len(people_data)

if 'DS_CDNUMORIGEN' in people_data.keys():
	del people_data['DS_CDNUMORIGEN']

with open('january.csv', 'w') as csvfile:
    fieldnames = ['DS_CDNUMORIGEN', 'DT_CDDATAINICI', 'DT_CDDATAFI', 'ID_CELLA_INI', 'DS_CDNUMDESTI', 'TAC_IMEI']
    # person, start time, end time, cell tower, call number, phone type
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for entry in people_data:
    	writer.writerow({'DS_CDNUMORIGEN':entry, 'DT_CDDATAINICI':people_data[entry][0], 'DT_CDDATAFI':people_data[entry][1], 
    		'ID_CELLA_INI':people_data[entry][2], 'DS_CDNUMDESTI':people_data[entry][3], 'TAC_IMEI':people_data[entry][4]})

print 'completed'