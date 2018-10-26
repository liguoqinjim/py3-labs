# coding:utf8
import datetime
import time

ticks = int(time.time())
print(ticks)
print("当前时间戳为:", ticks)

now = datetime.datetime.now()
print(now)

print(int(round(time.time() * 1000)))  # 毫秒级时间戳
