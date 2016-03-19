# March 4 2016


import os
import csv
print 'started'

# print os.getcwd()
#os.chdir('/run/user/1000/gvfs/sftp:host=andorra.media.mit.edu/home/data_commons/cdrs')
#print os.getcwd()

#import tower data, convention is to use the lowest value for each duplicate value for the tower id
towers_id = {}
with open('towers_id_dict.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	# i = 0
	for row in spamreader:
		data = str(row)[2:-2].split(',')
		try:
			towers_id[int(data[0])] = int(data[1])
		except ValueError:
			pass
# print towers_id

#import people data, all 9 months
file_name_base = '../data_commons/cdrs/DWFET_CDR_CELLID_20150'
for i in xrange(1,10):
	file_name = '../data_commons/cdrs/DWFET_CDR_CELLID_20150' + str(i) + '.csv' 
	spreadsheet_name = 'cellid_20150' + str(i) + '.csv'
	#file_name[-5] = str(i) #ex 201501 becomes 201502
	print 'importing', file_name[-10:]

	people_data = {}
	with open(file_name, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
		i = 0
		for row in spamreader:
			# if i >= 50: #run only subset of table when testing
			# 	break
			if i%50000 == 0:
				print 'got to', i
			i += 1
			if row[0] not in people_data and i > 1: #not a duplicate
				if int(row[6]) in towers_id:  #do this to factor in duplicate towers
					tower = towers_id[int(row[6])]
					# print 'changed', row[6], 'to', tower
				else:
					tower = int(row[6])
					# print 'did not change', tower
				person_data = row[3], row[4],  tower, row[-3], row[-1]
				people_data[row[0]] = person_data
				#key = person
				#value = start time, finish time, cell tower, number called, kind of phone

	print 'number of people', len(people_data)

	# removing column head (if it gets imported)
	if 'DS_CDNUMORIGEN' in people_data:
		del people_data['DS_CDNUMORIGEN'] #don't need column name

	print 'exporting', file_name[-10:]
	#spreadsheet_name[-5] = str(i)
	with open(spreadsheet_name, 'w') as csvfile:
		fieldnames = ['DS_CDNUMORIGEN_unique', 'DT_CDDATAINICI', 'DT_CDDATAFI', 'ID_CELLA_INI_modified', 'DS_CDNUMDESTI', 'TAC_IMEI']
		# person, start time, end time, cell tower, call number, phone type
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		writer.writeheader()
		for entry in people_data:
			writer.writerow({'DS_CDNUMORIGEN_unique':entry, 'DT_CDDATAINICI':people_data[entry][0], 'DT_CDDATAFI':people_data[entry][1], 
				'ID_CELLA_INI_modified':people_data[entry][2], 'DS_CDNUMDESTI':people_data[entry][3], 'TAC_IMEI':people_data[entry][4]})

print 'completed'
