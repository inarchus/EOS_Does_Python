from datetime import datetime, timedelta
import random

def datetime_stuff():

    random_time = datetime(year=2019, month=7, day=24, hour=13, minute=12, second=1)
    current_time = datetime.now()
    print(random_time, current_time)


def stripping_time():
    time_string_1 = '1969.7.16'
    moon_time = datetime.strptime(time_string_1, '%Y.%m.%d')
    print(moon_time)

    time_string_2 = 'Saturday, April 13, 2019 09:55:04'
    the_time = datetime.strptime(time_string_2, '%A, %B %d, %Y %H:%M:%S')
    print(the_time)
    
    time_string_3 = '1969/015-12:30'
    time_3 = datetime.strptime(time_string_3, '%Y/%j-%H:%M')
    print(time_3)
    try:
        time_3a = datetime.strptime(time_string_3, '%Y/%j %H:%M')
        print(time_3a)
    except ValueError:
        print('the time was not assigned')
        
        
def formatting_time():
    the_date = datetime(year=1954, month=12, day=25, hour=12, minute=30, second=13)
    print(the_date.strftime('%H%M%S'), the_date.strftime('%H-%M-%S'))
    print(the_date.strftime('%Y-%m-%d'), the_date.strftime('%Y.%j'))
    print(the_date.strftime('%A, %B %d, %Y'))


def arithmetic_time():
    back_to_the_future = datetime(year=1955, month=11, day=12, hour=22, minute=4, second=0)
    other_time = datetime(year=1985, month=11, day=14, hour=14, minute=0, second=0)
    future_time = datetime(year=2019, month=4, day=13, hour=14, minute=54)
    delta_1 = timedelta(days=13, hours=14, minutes=16, seconds=3)
    
    delta_2 = future_time - back_to_the_future
    print(delta_2)
    print(delta_1, back_to_the_future, other_time)
    
    new_time = future_time + delta_1
    other_new_time = other_time + timedelta(days=1)
    print(new_time, other_new_time)
    
    year = future_time.timetuple().tm_year
    day_of_year = future_time.timetuple().tm_yday
    print(year, day_of_year)

    if back_to_the_future < future_time:
        print('yep, the past is in the past')
    elif back_to_the_future >= other_time:
        print('this shouldn\'t be right')
    
    if delta_2 > timedelta(seconds=0):
        print('yes')
    
    L = list(timedelta(seconds=random.randint(0, 1000)) for _ in range(10))
    print(L)
    L.sort()
    print(L)
    
# formatting_time()
# stripping_time()
arithmetic_time()
