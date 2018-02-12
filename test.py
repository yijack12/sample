# 假设 data_dict 是您收到的数据字典
data_dict = {
    "home/kitchen/sensor/temp": "25°C",
    "home/bedroom/sensor/temp": "22°C",
    "home/bedroom/sensor/humidity": ""
}

# 检查 data_dict 是否包含所有这些键
keys_to_check = ["home/kitchen/sensor/temp", "home/bedroom/sensor/temp", "home/bedroom/sensor/humidity"]
all_keys_present = all(key in data_dict for key in keys_to_check)

print(all_keys_present)
# print("所有键都存在吗？", all_keys_present)
