import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from duration_utils import parse_duration


class DaysRegressionTest(unittest.TestCase):
    def test_single_day(self):
        self.assertEqual(parse_duration("1d"), 86400)

    def test_day_plus_hours(self):
        self.assertEqual(parse_duration("2d4h"), 187200)

    def test_full_mixed(self):
        self.assertEqual(parse_duration("1w1d2h3m4s"), 604800 + 86400 + 7200 + 180 + 4)


if __name__ == "__main__":
    unittest.main()
