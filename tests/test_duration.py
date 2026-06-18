import unittest
from duration_utils import parse_duration

class TestParseDuration(unittest.TestCase):
    def test_hours_minutes(self):
        self.assertEqual(parse_duration("1h30m"), 5400)

    def test_weeks(self):
        self.assertEqual(parse_duration("1w"), 604800)

    def test_days(self):
        self.assertEqual(parse_duration("1d"), 86400)
        self.assertEqual(parse_duration("2d"), 172800)
        self.assertEqual(parse_duration("1d12h"), 129600)

    def test_seconds(self):
        self.assertEqual(parse_duration("30s"), 30)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("")

if __name__ == "__main__":
    unittest.main()
