import random
from datetime import datetime, timedelta


def orbit_num(aos, factor):
    return int((int(aos.timetuple().tm_yday) * 86400 + aos.timetuple().tm_hour * 3600 + aos.timetuple().tm_min * 60 + aos.timetuple().tm_sec) / (factor*3600))


def generate_example(name):
    stations = ['172', '274', 'TDN', 'HI05', 'HI06', 'TDR', 'SGA', 'SGB']
    code = ['TR1', 'TR2', 'TR3']
    try:
        with open(name, 'w') as wotis_example:
            the_day = datetime(year=2019, month=random.randint(1, 12), day=random.randint(1, 31))
            aos = the_day + timedelta(seconds=random.randint(0, 3600))
            while aos < the_day + timedelta(days=1):
                los = aos + timedelta(seconds=random.randint(300, 600))
                orbit = orbit_num(aos, 3.57)
                difference = "00:" + str((los - aos).seconds // 60).zfill(2) + ":" + str((los - aos).seconds % 60).zfill(2)
                station = random.choice(stations)
                tr_code = random.choice(code)
                values = [str(orbit), aos.strftime('%Y/%j:%H:%M:%S'), los.strftime('%Y/%j:%H:%M:%S'), station, difference, tr_code]
                wotis_example.write('\t'.join(values) + '\n')
                aos = los + timedelta(seconds=random.randint(0, 3600))
    except OSError as err:
        print(err)


if __name__ == '__main__':
    for i in range(10):
        generate_example('AETHERParsedWOTIS' + str(i + 1).zfill(3) + '.rpt')
