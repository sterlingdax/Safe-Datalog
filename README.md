# Safe Datalog

##What it is:
***
A Python program to read the information saved in the Arduino Safe Datalogger

##How:
***
Using the CSV file created on the datalogger, have the Python program read, extract, then display the information in a meaningful way

###Parts:
***
Feather [Adalogger](https://www.adafruit.com/products/2795)

DS3231 RTC [Featherwing](https://www.adafruit.com/products/3028)

Featherwing [Proto](https://www.adafruit.com/products/2884)

DHT22 Temp [Sensor](https://www.adafruit.com/products/385)

#Scratch:
***

Here is a small example of the output from the program, it is saved in this order:

Humidity

Temperature

Voltage

Day, Month, Year Hour, Minute, Second - Most Recent Arduino code is 5 minute interval and no comma between data and time fields.





 49.40,  76.64, 4.30, 11/3/2016, 20:44:23
 
 52.70,  76.46, 4.23, 11/3/2016, 20:44:29
 
 52.80,  76.46, 4.23, 11/3/2016, 20:44:36
 
 51.40,  76.46, 4.22, 11/3/2016, 20:44:42
 
 50.60,  76.64, 4.23, 11/3/2016, 20:44:48
 
 50.00,  76.64, 4.23, 11/3/2016, 20:44:55
 
 49.50,  76.64, 4.22, 11/3/2016, 20:45:1
 
 49.20,  76.64, 4.22, 11/3/2016, 20:45:7
 
 49.20,  76.64, 4.22, 11/3/2016, 20:45:14
 
 49.20,  76.64, 4.22, 11/3/2016, 20:45:20
