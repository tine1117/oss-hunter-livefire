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

_TOKEN = re.compile(r"(\d+)([wdhms])")


def parse_duration(text: str) -> int:
    """Return the total number of seconds in a duration string.

    Examples:
        parse_duration("1h30m") -> 5400
        parse_duration("1w")    -> 604800
        parse_duration("2d")    -> 172800

    Raises ValueError on empty or unparseable input.
    """
    text = text.strip().lower()
    if not text:
        raise ValueError("duration string must not be empty")

    tokens = _TOKEN.findall(text)
    if not tokens:
        raise ValueError(f"no valid duration tokens in {text!r}")

    total = 0
    for amount, unit in tokens:
        total += int(amount) * _UNITS[unit]
    return total
