# Read datalogger from safe

import csv

# So yeah, get filename, open that file, then print the contents
# Not the most glamorous, but hey, it's a start!
filename = raw_input("Filename: ")
data = open(filename)
dataReader = csv.reader(data)
for row in data:
	print data
