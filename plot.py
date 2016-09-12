# From this page
# https://www.raspberrypi.org/learning/astro-pi-flight-data-analysis/graphing/
# Ask for filename, add dates, humidity, etc

from csv import reader
from matplotlib import pyplot, dates
from dateutil import parser

with open('smalllogfrom2nd.txt', 'r') as f:
    data = list(reader(f))
temp = [i[1] for i in data]
time = [parser.parse(i[4]) for i in data]
pyplot.title('Safe Temp vs Time')
pyplot.xlabel('Time/hours')
pyplot.ylabel('Temp/brrr!')
pyplot.plot(time, temp)
pyplot.show()
