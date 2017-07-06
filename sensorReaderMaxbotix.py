from time import time, sleep
import serial 

def read_distance(portName):
    maxwait = 5 # seconds to try for a good reading before quitting
    try:
      ser = serial.Serial(portName, 57600, 8, serial.PARITY_NONE, serial.STOPBITS_ONE)
    except:
      print "Could not open serial port"
      return False 

    timeStart = time()
    valueCount = 0

    while time() < timeStart + maxwait:
        if ser.inWaiting():
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

