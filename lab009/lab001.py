# coding:utf8

import requests

r = requests.get("https://api.github.com/events")
print(r.text)

# form
r = requests.post('http://httpbin.org/post', data={'key': 'value'})
print(r.text)

# 参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)
print(r.text)

# 这是header
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get("http://httpbin.org/get", headers=headers)
print(r.text)
