import datetime

now = datetime.datetime.now()
print((now - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M"))
print((now - datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M"))
print((now - datetime.timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M"))
