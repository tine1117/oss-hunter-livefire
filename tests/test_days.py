from duration_utils import parse_duration
import unittest

class TestDays(unittest.TestCase):
    def test_one_day(self):
        self.assertEqual(parse_duration("1d"), 86400)

    def test_days_with_hours(self):
        self.assertEqual(parse_duration("2d4h"), 187200)

    def test_week_with_day(self):
        self.assertEqual(parse_duration("1w1d"), 691200)

if __name__ == "__main__":
    unittest.main()