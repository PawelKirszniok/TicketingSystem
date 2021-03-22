import datetime

def datetime_to_str(date):
    result = f'{date.day}-{date.month}-{date.year}'
    return result

def str_to_datetime(string):
    d, m, y = string.split('-')

    result = datetime.date(int(y), int(m), int(d))
    return result
