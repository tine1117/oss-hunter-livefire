import pytest
from duration_utils import parse_duration


def test_standard_units():
    assert parse_duration("1w") == 604800
    assert parse_duration("1d") == 86400
    assert parse_duration("2d4h") == 187200
    assert parse_duration("1h30m") == 5400
    assert parse_duration("45s") == 45


def test_combined_units():
    expected = 604800 + (2 * 86400) + (3 * 3600) + (4 * 60) + 5
    assert parse_duration("1w2d3h4m5s") == expected


def test_invalid_input():
    with pytest.raises(ValueError):
        parse_duration("")
    with pytest.raises(ValueError):
        parse_duration("invalid")
    with pytest.raises(ValueError):
        parse_duration("10x")
