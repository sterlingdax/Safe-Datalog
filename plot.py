# From this page
# https://www.raspberrypi.org/learning/astro-pi-flight-data-analysis/graphing/
# Ask for filename, add dates, humidity, etc

from csv import reader
from matplotlib import pyplot
from dateutil import parser

with open('test.csv', 'r') as f:
    data = list(reader(f))
temp = [i[1] for i in data]
humidity = [i[0] for i in data]
battery = [i[2] for i in data]
#date = [i[3] for i in data]
#time = [parser.parse(i[4]) for i in data[1::]]
pyplot.title('Safe Temp vs Time')
pyplot.xlabel('Time/hours')
pyplot.ylabel('Temp/brrr!')
#pyplot.plot(time,temp)
pyplot.plot(range(len(temp)), temp)
pyplot.plot(range(len(humidity)), humidity)
pyplot.plot(range(len(battery)), battery)
#pyplot.plot(range(len(date)), date)
#pyplot.plot(range(len(time)), time)
pyplot.show()
