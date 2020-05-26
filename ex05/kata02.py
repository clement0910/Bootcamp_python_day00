import datetime

t = (3, 30, 2019, 9, 25)
d = datetime.datetime(hour=t[0], minute=t[1], year=t[2], month=t[3], day=t[4])
print('{:%m/%d/%Y %H:%M}'.format(d))
