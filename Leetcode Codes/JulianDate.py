import datetime

def julian_date(date):
    """Return the julian date for given date.
    >>> dt = datetime.datetime.today()
    >>> julian_date(dt)
    21336

    """
    try:
        return str(date.strftime('%y')) + date.strftime('%j')
    except Exception as e:
        return e

date = datetime.datetime.today()
