import datetime

def julian_date(date):
    """Return the julian date for given date.
    >>> dt = datetime.datetime.today()
    >>> julian_date(dt)
    '21336'

    """
    try:
        return str(date.strftime('%y')) + date.strftime('%j')
    except Exception as e:
        return e

"""OUTPUT:
PS D:\Python> python -m doctest -v  '.\Leetcode Codes\JulianDate.py'
Trying:
    dt = datetime.datetime.today()
Expecting nothing
ok
Trying:
    julian_date(dt)
Expecting:
    '21336'
ok
1 items had no tests:
    JulianDate
1 items passed all tests:
   2 tests in JulianDate.julian_date
2 tests in 2 items.
2 passed and 0 failed.
Test passed.

"""