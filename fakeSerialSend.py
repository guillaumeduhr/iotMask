import serial
import random
import time
from datetime import datetime

ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200)

while True:
    timestamp = datetime.now().timestamp()
    message = str(int(timestamp)) + ";" + \
        str(0 if random.randint(0, 3) == 0 else 1) + "$"
    print(message)
    ser.write((message).encode())

    time.sleep(random.randint(1, 5))
