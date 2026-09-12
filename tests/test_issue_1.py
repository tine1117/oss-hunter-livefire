import unittest
from duration_utils import parse_duration


class TestDaysUnit(unittest.TestCase):
    def test_one_day(self):
        self.assertEqual(parse_duration("1d"), 86400)

    def test_two_days_four_hours(self):
        self.assertEqual(parse_duration("2d4h"), 187200)

    def test_days_with_other_units(self):
        self.assertEqual(parse_duration("1d1h1m1s"), 90061)

    def test_existing_units_still_work(self):
        self.assertEqual(parse_duration("1h30m"), 5400)
        self.assertEqual(parse_duration("1w"), 604800)


if __name__ == "__main__":
    unittest.main()
