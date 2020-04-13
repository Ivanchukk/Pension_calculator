import re
import datetime

date = '1988-11-12'
def datev(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    x = '11/05/1988'
    date_now = datetime.datetime.now()
    date_now_year = date_now.year
    y = datetime.datetime.strptime(x, '%d/%m/%Y')
    yy = y.year
    f = date_now_year - yy
    print(f)

datev(date)