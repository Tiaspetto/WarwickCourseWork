import csv

# Read csv file and save into memeory 
def CSVReaderMy(file_path='', file_name=''):
	vbuf=open(file_path+file_name,'r').read().split('\n')
	result=zip([x.strip().split(',') for x in vbuf])
	return result

# Compare col difference by col name 
def CSVColDifference(csv_table, col_name1, col_name2):
	# Get col Index
	tableHeader = csv_table[0][0]
	colIndex1 = tableHeader.index(col_name1)
	colIndex2 = tableHeader.index(col_name2)

	# New diction for result 
	result = {}
	lineIndex = 0
	for row in csv_table:
		# Ignore header
		if lineIndex != 0:
			difference = abs(int(row[0][colIndex1]) - int(row[0][colIndex2]))
			result[row[0][0]] = difference
			lineIndex +=1
		else:
			lineIndex +=1
	return result

# Sort
def DictionSrot(dict_input):
	return sorted(dict_input.iteritems(), key=lambda (k, v): (v, k))

filePath = raw_input("Please input file name:")
myCSVfile = CSVReaderMy(filePath)
firstColName = raw_input("Please input first column name:")
secondColName = raw_input("Please input second column name:")
differences = CSVColDifference(myCSVfile,firstColName,secondColName)
differences = DictionSrot(differences)

print differences