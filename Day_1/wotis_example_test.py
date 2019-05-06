from unittest import TestCase
from Day_1.wotis_example import read_wotis


def baseline_read_wotis(file_name):
    wotis_file = open(file_name)

    for line in wotis_file:
        print(line)

    wotis_file.close()


class WotisTester(TestCase):

    def test_read_wotis_file(self):
        self.assertRaises(OSError, read_wotis, '')
        self.assertRaises(OSError, read_wotis, 'asdfasdfasdf.rpt')

    def test_read_wotis_process(self):
        for i in range(10):
            self.assertListEqual(baseline_read_wotis('Day_1\\test' + str(i + 1) + '.rpt'), read_wotis('Day_1\\test' + str(i + 1) + '.rpt'))
