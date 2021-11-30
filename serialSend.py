import serial
from datetime import datetime

ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200)

message = datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + ";test$"
ser.write((message).encode())
