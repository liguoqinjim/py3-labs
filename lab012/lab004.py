import time
import datetime

# unix样例
# 1670038783 <-> 2022-12-03 11:39:43

# 获得当前时间戳01
print(int(time.time()))

# 获得当前时间戳02
now = datetime.datetime.now()
print(int(time.mktime(now.timetuple())))

# unix->datetime
d1 = datetime.datetime.fromtimestamp(1670038783)
print(d1)

# datetime->str
s1 = d1.strftime("%Y-%m-%d")
print(s1)

# str->datetime
s2 = '2022-12-03'
d2 = datetime.datetime.strptime(s2, "%Y-%m-%d")
print(d2)
print(d2.year, d2.month, d2.day)
