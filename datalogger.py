#! /usr/bin/env python3
# Read datalogger from safe
import csv

filename = input("Filename: ")
data = open(filename)
dataReader = csv.reader(data)
for row in dataReader:
	print('Row #' + str(dataReader.line_num) + ' ' + str(row))
	
# Keep up with row numbers, and see if there is a header in the file
# that would show what the data is per row

# change line 8 to just read data and it's not a list of lists, it's numbers, hrmmm
# Maybe have the program kick out a certain number of entries to make it smaller and
# or easier to graph