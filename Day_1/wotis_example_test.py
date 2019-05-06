from unittest import TestCase
from datetime import datetime
from wotis_example import read_wotis


def baseline_read_wotis(file_name):
    wotis_file = open(file_name)

    total_day = []

    for line in wotis_file:
        split_line = line.strip().split('\t')

        if len(split_line) == 6:
            current = {'orbit': int(split_line[0]), 'aos': datetime.strptime(split_line[1], '%Y/%j:%H:%M:%S'), 'los': datetime.strptime(split_line[2], '%Y/%j:%H:%M:%S'),
                       'station': split_line[3], 'tr_code': split_line[5]}
            total_day.append(current)

    wotis_file.close()
    return current


class WotisTester(TestCase):

    def test_read_wotis_file(self):
        self.assertRaises(OSError, read_wotis, '')
        self.assertRaises(OSError, read_wotis, 'asdfasdfasdf.rpt')

    def test_read_wotis_process(self):
        for i in range(10):
            file = 'WotisExamples/AETHERParsedWOTIS' + str(i + 1).zfill(3) + '.rpt'
            self.assertEqual(baseline_read_wotis(file), read_wotis(file))
