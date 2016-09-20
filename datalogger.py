# Read datalog information from safe, which has these fields, in this order:
# Humidity [0] - Inside safe
# Temperature [1] - Inside Safe
# Voltage [2] - Of LiPo Battery Backup
# Day, Month, Year Hour, Minute, Second [3]
# Hour, Minute, Second [4] - Before 9-19-2016
# Currently logger records every five minutes after 9-19-2016
# Previous data (1 week) will be at 1 minute intervals
# This previous data will also include separate date/time lines
# New data will have the full timestamp on one line (3)


from matplotlib import pyplot, dates
from csv import reader
from dateutil import parser

filename = input("Filename: ")
f = open(filename, 'r')
data = list(reader(f))

temp = [i[1] for i in data[1::]]
time = [parser.parse(i[3]) for i in data[1::]]

pyplot.title('Safe Temp over time')
pyplot.xlabel('Time')
pyplot.ylabel('Temperature/$^\circ$F')
pyplot.plot(time, temp)
pyplot.show()
