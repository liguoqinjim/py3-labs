import time
import datetime

# print(time.strftime("%Y/%m/%d %H:%M"))
# print(time.replace(minute=last_quarter_minute).strftime("%Y/%m/%d %H:%M"))

rounded_qtr_hour = lambda dt: datetime.datetime(dt.year, dt.month, dt.day, dt.hour,
                                                15 * (dt.minute // 15))
# print(rounded_qtr_hour)
print(datetime.datetime.now())
print(rounded_qtr_hour(datetime.datetime.now()))

# 参考资料
# https://stackoverflow.com/questions/24831018/python-how-can-i-round-a-datetime-object-to-the-most-recent-previous-quarter-h
