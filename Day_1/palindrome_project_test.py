from unittest import TestCase
from palindrome_project import is_palindrome

def baseline_is_palindrome(s):
    s = s.lower()
    for i in range(len(s)):
        if s[i] != s[len(s) - 1 - i]:
            return False

    return True

class PalindromeTest(TestCase):

    test_cases = ['', 'a', 'racecar', 'three mice', 'ABCdcba', 'MadamInEdenImAdam', 'wasitaratisaw', 'asdfasdfasdfasdf', 'nope, definitely not']

    def test_palindrome(self):
        for case in PalindromeTest.test_cases:
            self.assertEqual(baseline_is_palindrome(case), is_palindrome(case))
