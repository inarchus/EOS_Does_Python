from datetime import datetime, timedelta


def stripping_time():
    time_string_1 = ''


def formatting_time():
    the_date = datetime(year=1954, month=12, day=25, hour=12, minute=30, second=13)
    print(the_date.strftime('%H%M%S'), the_date.strftime('%H-%M-%S'))
    print(the_date.strftime('%Y-%m-%d'), the_date.strftime('%Y.%j'))

    print(the_date.strftime('%A, %B %d, %Y'))


def arithmetic_time():
    pass



formatting_time()
stripping_time()
