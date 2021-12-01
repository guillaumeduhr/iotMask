import time
import sqlite3
from datetime import datetime

con = sqlite3.connect('example.db')
cur = con.cursor()

while True:
    cur.execute("insert into test values (?, ?)",
                (datetime.now().isoformat(), True))
    con.commit()
    time.sleep(.5)

con.close()
