import unittest
from duration_utils import parse_duration

class TestParseDuration(unittest.TestCase):
    def test_days(self):
        self.assertEqual(parse_duration("1d"), 86400)
        self.assertEqual(parse_duration("2d4h"), 187200)

    def test_seconds(self):
        self.assertEqual(parse_duration("45s"), 45)

    def test_weeks(self):
        self.assertEqual(parse_duration("1w"), 604800)

    def test_combined(self):
        self.assertEqual(parse_duration("1h30m"), 5400)
        self.assertEqual(parse_duration("1w2d3h4m5s"), 604800 + 172800 + 10800 + 240 + 5)

    def test_empty(self):
        with self.assertRaises(ValueError):
            parse_duration("")

    def test_invalid(self):
        with self.assertRaises(ValueError):
            parse_duration("invalid")
        with self.assertRaises(ValueError):
            parse_duration("10x")

if __name__ == '__main__':
    unittest.main()
