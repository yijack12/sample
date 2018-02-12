import time
import zenoh
from zenoh import Sample
import re

def handler(sample: Sample, data_dict, temperature_dict, humidity_dict):
    sampleKey = str(sample.key_expr)
    sampleValue = sample.payload.decode('utf-8')
    data_dict[sampleKey] = sampleValue
    timestamp = time.time()

    keys_to_check = ["home/kitchen/sensor/temp", "home/bedroom/sensor/temp", "home/bedroom/sensor/humidity"]
    all_keys_present = all([key in data_dict for key in keys_to_check])

    if all_keys_present:
        kitchen_temp = f">> [Subscriber] Received {sample.kind} ('home/kitchen/sensor/temp': '{data_dict['home/kitchen/sensor/temp']}')"
        bedroom_temp = f">> [Subscriber] Received {sample.kind} ('home/bedroom/sensor/temp': '{data_dict['home/bedroom/sensor/temp']}')"
        bedroom_humidity = f">> [Subscriber] Received {sample.kind} ('home/bedroom/sensor/humidity': '{data_dict['home/bedroom/sensor/humidity']}')"
# <<< add
        kitchen_temp_val = re.findall(r"temperature: (.*?),", kitchen_temp)[0]
        bedroom_temp_val = re.findall(r"temperature: (.*?),", bedroom_temp)[0]
        bedroom_humidity_val = re.findall(r"humidity: (.*?),", bedroom_humidity)[0]

        if kitchen_temp_val in temperature_dict:
            temperature_dict[kitchen_temp_val].append(timestamp)
            print(f"has same temperture as {temperature_dict[kitchen_temp_val]}")
        else:
            temperature_dict[kitchen_temp_val] = [timestamp]

        if bedroom_temp_val in temperature_dict:
            temperature_dict[bedroom_temp_val].append(timestamp)
            print(f"has same temperture as {temperature_dict[bedroom_temp_val]}")
        else:
            temperature_dict[bedroom_temp_val] = [timestamp]

        if bedroom_humidity_val in humidity_dict:
            humidity_dict[bedroom_humidity_val].append(timestamp)
            print(f"has same humidity as {humidity_dict[bedroom_humidity_val]}")
        else:
            humidity_dict[bedroom_humidity_val] = [timestamp]
# >>>

        print(kitchen_temp)
        print(bedroom_temp)
        print(bedroom_temp)
        data_dict.clear()

zenoh.init_logger()

conf = zenoh.Config.from_json5('{"mode": "peer"}')
session = zenoh.open(conf)

data_dict = {}
temperature_dict = dict()
humidity_dict = dict()

sub = session.declare_subscriber("**/sensor/*", lambda sample: handler(sample, data_dict, temperature_dict, humidity_dict))
