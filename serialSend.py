import serial
import random
from datetime import datetime

ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200)

# message = datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + ";test$"
# 14 char => 2 pour ; et 0 ou 1 donc il reste 12 pour date et heure
# message = "12345678911234$"
timestamp = datetime.now().timestamp()
# print(timestamp)
# print(datetime.fromtimestamp(int(timestamp)).isoformat())
message = str(int(timestamp)) + ";" + \
    str(0 if random.randint(0, 3) == 0 else 1) + "$"
print(message)
ser.write((message).encode())
