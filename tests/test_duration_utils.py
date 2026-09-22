"""Tests for duration_utils.parse_duration."""

import pytest
from duration_utils import parse_duration


def test_hours_and_minutes():
    assert parse_duration("1h30m") == 5400


def test_weeks():
    assert parse_duration("1w") == 604800


def test_days():
    """Regression: the 'd' unit was missing from _UNITS."""
    assert parse_duration("1d") == 86400


def test_days_combined():
    assert parse_duration("1d12h") == 86400 + 43200


def test_seconds_only():
    assert parse_duration("45s") == 45


def test_empty_raises():
    with pytest.raises(ValueError):
        parse_duration("")


def test_no_tokens_raises():
    with pytest.raises(ValueError):
        parse_duration("abc")
