#! /usr/bin/env python3
# Read datalogger from safe
import csv

filename = input("Filename: ")
data = open(filename)
dataReader = csv.reader(data)
for row in data:
	print('Row #' + str(dataReader.line_num) + ' ' + str(row))
	
# Keep up with row numbers, and see if there is a header in the file
# that would show what the data is per row

