import unittest

from duration_utils import parse_duration


class ParseDuration(unittest.TestCase):
        def test_weeks(self):
        self.assertEqual(parse_duration("1w"), 604800)

    def test_days(self):
        self.assertEqual(parse_duration("1d"), 86400)

    def test_combined(self):
        self.assertEqual(parse_duration("1h30m"), 5400)

    def test_combined_days_and_hours(self):
        self.assertEqual(parse_duration("2d4h"), 187200)


if __name__ == "__main__":
    unittest.main()
