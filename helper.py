import datetime
from datetime import datetime, timedelta, date

def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta

def timelist():
    dts = [dt.strftime('%H%M') for dt in 
        datetime_range(datetime(2016, 9, 1, 0), datetime(2016, 9, 1, 9+12), 
        timedelta(minutes=30))]
    return dts

def lastMonth():
    tday = date.today()
    first = tday.replace(day=1)
    lastMonth = first - timedelta(days=1)
    return lastMonth.strftime("%b")

