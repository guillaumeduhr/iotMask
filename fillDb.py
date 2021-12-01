import random
import time
# import sqlite3
from datetime import datetime
from influxdb import InfluxDBClient


client = InfluxDBClient(host='localhost', port=8086)
# client.drop_database('maskamera')
client.create_database('maskamera')
client.switch_database('maskamera')

while True:
    json_body = [
        {
            "measurement": "maskCheck",
            "time": datetime.now().isoformat(),
            "fields": {
                "mask": 0 if random.randint(0, 5) == 0 else 1
            }
        }
    ]
    client.write_points(json_body)
    print("Added new measurement at " + datetime.now().isoformat())
    time.sleep(random.randint(1, 5))

# con = sqlite3.connect('example.db')
# cur = con.cursor()

# while True:
#     cur.execute("insert into test values (?, ?)",
#                 (datetime.now().timestamp(), True))
#     con.commit()
#     time.sleep(.5)

# con.close()
