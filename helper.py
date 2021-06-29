from datetime import datetime, timedelta

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

