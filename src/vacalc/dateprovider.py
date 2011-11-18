import os
from datetime import date, datetime

def CurrentDate():
    date_from_environ = os.environ.get('VACALC_DATE', None)
    if date_from_environ:
        year, month, day = (int(item) for item in date_from_environ.split('-'))
        return date(year, month, day)
    return datetime.now()
