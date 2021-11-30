from datetime import datetime
# import serial
# import time
import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()
# cur.execute("create table test (date, mask)")

cur.execute("insert into test values (?, ?)", (datetime.now(), False))

con.commit()
con.close()
# ser = serial.Serial(port='/dev/ttyACM1', baudrate=115200)

# while (True):

#     reading = ser.readline().decode()

#     if reading.startswith('...'):
#         # print('Message recu: ' + reading)
#         reading = reading[3:len(reading)-2]
#         readingArr = reading.split(";")
#         print(readingArr)

#     time.sleep(0.01)
