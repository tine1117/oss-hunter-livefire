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

    def test_days_combined(self):
        self.assertEqual(parse_duration("2d4h"), 187200)

    def test_combined(self):
        self.assertEqual(parse_duration("1h30m"), 5400)

    def test_mixed_all_units(self):
        self.assertEqual(
            parse_duration("1w2d3h4m5s"),
            604800 + 2 * 86400 + 3 * 3600 + 4 * 60 + 5
        )

    def test_case_insensitive(self):
        self.assertEqual(parse_duration("1D"), 86400)
        self.assertEqual(parse_duration("2D4H"), 187200)

    def test_whitespace_handling(self):
        self.assertEqual(parse_duration("  1d  "), 86400)

    def test_invalid_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("abc")

    def test_invalid_unit_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("5x")

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("")

    def test_whitespace_only_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("   ")


if __name__ == "__main__":
    unittest.main()
