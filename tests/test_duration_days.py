import pytest
from duration_utils import parse_duration

def test_parse_single_day():
    """A single day should be converted to 86 400 seconds."""
    assert parse_duration("1d") == 86_400

def test_parse_multiple_days_and_hours():
    """
    Combination of days and hours must be summed correctly.
    2 days = 172 800 seconds
    4 hours = 14 400 seconds
    Total = 187 200 seconds
    """
    assert parse_duration("2d4h") == 187_200

def test_parse_complex_mixed_units():
    """
    Ensure that days work together with all other supported units.
    """
    expected = (
        1 * 86_400 +   # 1d
        2 * 7 * 24 * 60 * 60 +  # 2w
        3 * 60 * 60 +   # 3h
        4 * 60 +        # 4m
        5               # 5s
    )
    assert parse_duration("1d2w3h4m5s") == expected
