import time
import zenoh
from random import uniform
from zenoh import Sample

key = "home/bedroom/sensor/temp"

zenoh.init_logger()

conf = zenoh.Config.from_json5('{"mode": "peer"}')
session = zenoh.open(conf)
pub = session.declare_publisher(key)
temp = 27.0

while True:
    timestamp = time.time()
    temp += uniform(-1.0, 1.0) 
    data = f"temperature: {temp}, timestamp: {timestamp}"
    pub.put(data)
    time.sleep(1.6)
