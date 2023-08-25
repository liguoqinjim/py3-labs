import json
import sys
import datetime

import requests

# 从参数中获取key
key = sys.argv[1]
url = f"https://devapi.qweather.com/v7/astronomy/sun?location=101020100&date=20230825&key={key}"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)

data = json.loads(response.text)
print(data)

# 处理时间
sunrise_time = data['sunrise']
sunset_time = data['sunset']
# sunrise转换为datetime
sunrise_time = datetime.datetime.strptime(sunrise_time, '%Y-%m-%dT%H:%M%z')
print(sunrise_time)
# 只保留时间
sunrise_time = sunrise_time.time()
print(sunrise_time)
