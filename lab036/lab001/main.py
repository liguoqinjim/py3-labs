import datetime


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


SUN, MON, TUE, WED, THU, FRI, SAT = range(7)
d = datetime.date(2021, 8, 25)
next_monday = next_weekday(d, MON)  # 0 = Monday, 1=Tuesday, 2=Wednesday...
print("next_monday1=", next_monday)

# 字符串->datetime

# datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '"%Y-%m-%d %H:%M:%S"')
datetime_object = datetime.datetime.strptime('2021-08-25', '%Y-%m-%d').date()
print(type(d), type(datetime_object))
next_monday = next_weekday(datetime_object, MON)  # 0 = Monday, 1=Tuesday, 2=Wednesday...
print("next_monday2=", next_monday)
