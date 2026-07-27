"""RED tests demonstrating the 'd' (days) unit bug in parse_duration.

These tests MUST fail before the fix is applied.
After fixing, all should pass (GREEN).
"""
import unittest

from duration_utils import parse_duration


class TestDaysUnitBug(unittest.TestCase):
    """parse_duration silently drops the 'd' (days) unit.

    The regex accepts 'd' but _UNITS dict doesn't include it,
    so day tokens are consumed but contribute 0 to the total.
    """

    def test_single_day(self):
        """1d should equal 86400 seconds (1 day), not 0."""
        self.assertEqual(parse_duration("1d"), 86400)

    def test_multiple_days(self):
        """2d should equal 172800 seconds (2 days), not 0."""
        self.assertEqual(parse_duration("2d"), 172800)

    def test_days_with_hours(self):
        """1d12h should equal 129600 (86400 + 43200), not just 43200."""
        self.assertEqual(parse_duration("1d12h"), 129600)

    def test_days_with_minutes(self):
        """1d30m should equal 88200 (86400 + 1800), not just 1800."""
        self.assertEqual(parse_duration("1d30m"), 88200)

    def test_days_with_seconds(self):
        """1d30s should equal 86430 (86400 + 30), not just 30."""
        self.assertEqual(parse_duration("1d30s"), 86430)

    def test_all_units_combined(self):
        """1w2d3h4m5s should equal 788645 (604800+172800+10800+240+5)."""
        self.assertEqual(parse_duration("1w2d3h4m5s"), 788645)


if __name__ == "__main__":
    unittest.main()
