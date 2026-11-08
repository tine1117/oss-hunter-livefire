import unittest
import sys
from pathlib import Path

# Add src to sys.path so test can import directly
SRC_DIR = Path(__file__).resolve().parent.parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from duration_utils import parse_duration


class ParseDurationTest(unittest.TestCase):
    def test_days_unit_parsing(self):
        """Verify issue #1: 'd' unit is parsed into 86400 seconds."""
        self.assertEqual(parse_duration("1d"), 86400)
        self.assertEqual(parse_duration("2d4h"), 187200)
        self.assertEqual(parse_duration("7d"), 604800)
        self.assertEqual(parse_duration("0d"), 0)

    def test_hours(self):
        self.assertEqual(parse_duration("1h"), 3600)

    def test_minutes(self):
        self.assertEqual(parse_duration("30m"), 1800)

    def test_seconds(self):
        self.assertEqual(parse_duration("45s"), 45)

    def test_weeks(self):
        self.assertEqual(parse_duration("1w"), 604800)

    def test_combined(self):
        self.assertEqual(parse_duration("1h30m"), 5400)
        self.assertEqual(parse_duration("1w2d3h4m5s"), 604800 + 172800 + 10800 + 240 + 5)

    def test_case_and_strip(self):
        self.assertEqual(parse_duration("  1D2H  "), 86400 + 7200)
        self.assertEqual(parse_duration("5D"), 432000)

    def test_invalid_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("abc")
        with self.assertRaises(ValueError):
            parse_duration("10x")
        with self.assertRaises(ValueError):
            parse_duration("1d_invalid")

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("")
        with self.assertRaises(ValueError):
            parse_duration("   ")


if __name__ == "__main__":
    unittest.main()
