# coding:utf8

import json

# 读取数据
with open('data/test.json', 'r') as f:
    data = json.load(f)
    print("data['a']=", data["a"])
    print("data['b']=", data["b"])
