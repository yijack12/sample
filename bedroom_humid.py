import time
import zenoh
from random import uniform
from zenoh import Sample

key = "home/bedroom/sensor/humidity"

zenoh.init_logger()

conf = zenoh.Config.from_json5('{"mode": "peer"}')
session = zenoh.open(conf)
pub = session.declare_publisher(key)
humidity = 55.0

while True:
    timestamp = time.time()
    humidity += uniform(-7.0, 8.0) 
    data = f"humidity: {humidity}, timestamp: {timestamp}"
    pub.put(data)
    time.sleep(0.75)
