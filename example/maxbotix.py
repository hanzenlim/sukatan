#!/usr/bin/python3
# Filename: maxSonarTTY.py

# Reads serial data from Maxbotix ultrasonic rangefinders
# Gracefully handles most common serial data glitches
# Use as an importable module with "import MaxSonarTTY"
# Returns an integer value representing distance to target in millimeters

from time import time, sleep

import serial 
serialDevice = "/dev/ttyUSB0" # default for RaspberryPi
maxwait = 5 # seconds to try for a good reading before quitting

def measure(portName):
    ser = serial.Serial(portName, 57600, 8, serial.PARITY_NONE, serial.STOPBITS_ONE)
    timeStart = time()
    valueCount = 0

    while time() < timeStart + maxwait:
        if ser.inWaiting():
#            ser.flushInput() 
            bytesToRead = ser.inWaiting()
            valueCount += 1
            if valueCount < 2: # 1st reading may be partial number; throw it out
                continue
            testData = ser.read(5)
            if not testData.startswith(b'R'):
                # data received did not start with R
                continue
            try:
                sensorData = testData.decode('utf-8').lstrip('R')
            except UnicodeDecodeError:
		print 'Unicode decode error'
                # data received could not be decoded properly
                continue
            try:
                mm = int(sensorData)
            except ValueError:
		print 'Value is not a number::' + sensorData
                # value is not a number
                continue

            ser.close()
            return(mm)

    ser.close()
    raise RuntimeError("Expected serial data not received")

if __name__ == '__main__':
    measurement = measure(serialDevice)
    print("distance =",measurement)





