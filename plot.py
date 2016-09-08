# From this page
# https://www.raspberrypi.org/learning/astro-pi-flight-data-analysis/graphing/
# Currently just gives temp, needs to be worked on
# Ask for filename, add dates, humidity, etc

from csv import reader
from matplotlib import pyplot
with open('DATALOG3-11to7-20-2016.txt', 'r') as f:
    data = list(reader(f))
temp = [i[1] for i in data]
pyplot.plot(range(len(temp)), temp)
pyplot.show()
