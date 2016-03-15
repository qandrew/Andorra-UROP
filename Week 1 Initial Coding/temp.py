c = {1:3, 4:6}

print 1 in c.keys()

file_name = list('../data_commons/cdrs/DWFET_CDR_CELLID_201501.csv')
file_name[-5] = 3
file_name = str(file_name)
print file_name