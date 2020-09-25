import datetime

d1 = datetime.datetime(2005, 2, 16)
d2 = datetime.datetime(2004, 12, 31)
print((d1 - d2).days)

# Timestamp subtraction must have the same timezones or no timezones
print((d1 - d2).days)
