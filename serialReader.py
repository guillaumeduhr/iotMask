import serial
import time
from datetime import datetime
from influxdb import InfluxDBClient


client = InfluxDBClient(host='localhost', port=8086)
# client.drop_database('maskamera')
client.create_database('maskamera')
client.switch_database('maskamera')

ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200)

while (True):

    reading = ser.readline().decode()

    if reading.startswith('...'):
        # print('Message recu: ' + reading)
        reading = reading[3:len(reading)-2]
        readingArr = reading.split(";")
        print(readingArr)
        isoDate = datetime.fromtimestamp(int(readingArr[0])).isoformat()
        maskOn = int(readingArr[1])
        json_body = [
            {
                "measurement": "maskCheck",
                "time": isoDate,
                "fields": {
                    "mask": maskOn
                }
            }
        ]

        client.write_points(json_body)
        print("Added new measurement at " +
              isoDate + " with value: " + str(maskOn))

    time.sleep(0.01)
