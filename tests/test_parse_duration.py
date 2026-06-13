import unittest
from duration_utils import parse_duration


class TestParseDuration(unittest.TestCase):

    # --- days (the bug fix) ---
    def test_days_single(self):
        self.assertEqual(parse_duration("1d"), 86400)

    def test_days_combined_with_hours(self):
        self.assertEqual(parse_duration("2d4h"), 187200)

    def test_days_zero(self):
        self.assertEqual(parse_duration("0d"), 0)

    # --- other units ---
    def test_weeks(self):
        self.assertEqual(parse_duration("1w"), 604800)

    def test_hours(self):
        self.assertEqual(parse_duration("1h"), 3600)

    def test_minutes(self):
        self.assertEqual(parse_duration("1m"), 60)

    def test_seconds(self):
        self.assertEqual(parse_duration("1s"), 1)

    def test_hours_and_minutes(self):
        self.assertEqual(parse_duration("1h30m"), 5400)

    def test_all_units(self):
        # 1w + 1d + 1h + 1m + 1s
        expected = 604800 + 86400 + 3600 + 60 + 1
        self.assertEqual(parse_duration("1w1d1h1m1s"), expected)

    def test_large_values(self):
        self.assertEqual(parse_duration("7d"), 604800)

    # --- error cases ---
    def test_empty_string_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("")

    def test_invalid_unit_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("5x")


if __name__ == "__main__":
    unittest.main()
