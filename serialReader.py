import serial
import time

ser = serial.Serial(port='/dev/ttyACM1', baudrate=115200)

while (True):

    reading = ser.readline().decode()

    if reading.startswith('...'):
        # print('Message recu: ' + reading)
        reading = reading[3:len(reading)-2]
        readingArr = reading.split(";")
        print(readingArr)

    time.sleep(0.01)
