import datetime

datetime_object = datetime.datetime.now()
print(datetime_object, type(datetime_object))
# print(dir(datetime_object))
date_object = datetime.date.today()
print(date_object)

d = datetime.date(2019, 1, 1)
print(d)

timestamp = datetime.date.fromtimestamp(500000)
print(timestamp)

today = datetime.date.today()

print(today.year, today.month, today.day, today.weekday, today.isoweekday)

now = datetime.datetime.now()
print(now)
print(now.strftime("%m/%d/%Y %B %a %A %w %d %I %p %j %z %c %x"))

from datetime import datetime
date_string = "21 June, 2018"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
import pytz

tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

assert 1 == 1