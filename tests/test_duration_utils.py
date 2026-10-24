import unittest

from duration_utils import parse_duration


class ParseDurationTests(unittest.TestCase):
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

    def test_multiple_days_and_hours(self):
        self.assertEqual(parse_duration("2d4h"), 187200)

    def test_all_supported_units(self):
        self.assertEqual(
            parse_duration("1w2d3h4m5s"),
            604800 + 172800 + 10800 + 240 + 5,
        )

    def test_combined(self):
        self.assertEqual(parse_duration("1h30m"), 5400)

    def test_whitespace_and_uppercase_are_normalized(self):
        self.assertEqual(parse_duration(" 2D4H "), 187200)

    def test_zero_duration_is_valid(self):
        self.assertEqual(parse_duration("0d"), 0)

    def test_invalid_text_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("abc")

    def test_unknown_unit_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("1y")

    def test_malformed_mixed_input_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("1d-nope")

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("")


if __name__ == "__main__":
    unittest.main()
