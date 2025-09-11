from random import randrange
from datetime import timedelta

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.

    sample call:
    from datetime import datetime

    d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')

    print(random_date(d1, d2))
    """
    delta = end - start
    int_delta = delta.days
    random_day = randrange(int_delta)
    return start + timedelta(days=random_day)