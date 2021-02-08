import datetime
import time

print(datetime.datetime.today())  # 2020-09-24 11:26:52.000288
print(datetime.date.today())  # 2020-09-24
print(datetime.datetime.now())  # 2020-09-24 11:28:04.630825

# 解析时间字符串
tm = datetime.datetime.strptime("2018-01-16 23:44:55", "%Y-%m-%d %H:%M:%S")
print(tm.year, tm.month, tm.day)  # 2018 1 16

# 时间->string
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
