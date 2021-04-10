import time
from datetime import datetime
import dateparser
import pytz


def get_current_timestamp():
    return int(round(time.time() * 1000))


def convert_cst_in_second_to_utc(time_in_second):
    if time_in_second > 946656000:
        return (time_in_second - 8 * 60 * 60) * 1000
    else:
        return 0


def convert_cst_in_millisecond_to_utc(time_in_ms):
    if time_in_ms > 946656000000:
        return time_in_ms - 8 * 60 * 60 * 1000
    else:
        return 0


def maybe_convert_timestamp_to_datetime(ms, convert):
    if convert:
        return datetime.fromtimestamp(ms/1000)
    return ms

def maybe_convert_to_milliseconds(dt):    
    """Convert input to milliseconds
    If using offset strings add "UTC" to date string e.g. "now UTC", "11 hours ago UTC"
    See dateparse docs for formats http://dateparser.readthedocs.io/en/latest/
    :param dt: 
        datetime in readable format, i.e. "January 01, 2018", "11 hours ago UTC", "now UTC"
        or already in milliseconds
    """

    if isinstance(dt, (int, float)):
        return dt # already in milliseconds
    elif isinstance(dt, str):
        # parse our date string
        dt = dateparser.parse(dt)
    elif not isinstance(dt, datetime):
        raise TypeError("Invalid type {}".format(type(dt)))
        
    # if the date is not timezone aware apply UTC timezone
    if dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None:
        dt = dt.replace(tzinfo=pytz.utc)
    
    # get epoch value in UTC
    epoch = datetime.utcfromtimestamp(0).replace(tzinfo=pytz.utc)
    # return the difference in time
    return int((dt - epoch).total_seconds() * 1000.0)     


def interval_to_milliseconds(interval: str):
    """Convert a Binance interval string to milliseconds
    :param interval: Binance interval string, e.g.: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w
    :type interval: str
    :return:
         int value of interval in milliseconds
         None if interval prefix is not a decimal integer
         None if interval suffix is not one of m, h, d, w
    """
    seconds_per_unit = {
        "m": 60,
        "h": 60 * 60,
        "d": 24 * 60 * 60,
        "w": 7 * 24 * 60 * 60,
    }
    try:
        return int(interval[:-1]) * seconds_per_unit[interval[-1]] * 1000
    except (ValueError, KeyError):
        return None