import unittest

from duration_utils import parse_duration


class ParseDuration(unittest.TestCase):
    def test_hours(self):
        self.assertEqual(parse_duration("1h"), 3600)

    def test_minutes(self):
        self.assertEqual(parse_duration("30m"), 1800)

    def test_seconds(self):
        self.assertEqual(parse_duration("45s"), 45)

    def test_weeks(self):
        self.assertEqual(parse_duration("1w"), 604800)

    def test_days(self):
        self.assertEqual(parse_duration("1d"), 86400)

    def test_combined(self):
        self.assertEqual(parse_duration("1h30m"), 5400)

    def test_combined_with_days(self):
        self.assertEqual(parse_duration("2d4h"), 187200)

    def test_invalid_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("abc")

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("")


if __name__ == "__main__":
    unittest.main()
