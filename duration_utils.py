"""Parse human-friendly duration strings like '1h30m' into seconds."""

from __future__ import annotations

import re

# Seconds per unit. Supported: weeks, days, hours, minutes, seconds.
_UNITS = {
    "w": 604800,
    "d": 86400,
    "h": 3600,
    "m": 60,
    "s": 1,
}

_TOKEN = re.compile(r"(d+)([wdhms])")


def parse_duration(text: str) -> int:
    """Return the total number of seconds in a duration string.

    Examples:
        parse_duration("1h30m") -> 5400
        parse_duration("1w")    -> 604800

    Raises ValueError on empty or malformed input.
    """
    text = text.strip().lower()
    if not text:
        raise ValueError("empty duration")

    total = 0
    consumed = 0
    for m in _TOKEN.finditer(text):
        value, unit = int(m.group(1)), m.group(2)
        if unit in _UNITS:
            total += value * _UNITS[unit]
        consumed += len(m.group(0))

    if consumed != len(text):
        raise ValueError(f"invalid duration: {text!r}")
    return total
