"""
Duration parsing utility.

parse_duration() converts a compact human-readable duration string into a total
number of seconds.

Supported units:
    w = weeks
    d = days
    h = hours
    m = minutes
    s = seconds

Example:
    >>> parse_duration("1d2h30m")
    95400
    >>> parse_duration("2w")
    1209600
    >>> parse_duration("45s")
    45

BUGFIX (issue #1): the "d" (days) unit was silently dropped.
------------------------------------------------------------
The tokenizer regex `(\\d+)([wdhms])` DOES match the "d" unit, so the loop
consumed the token without raising, but the lookup table `_UNITS` did not
contain a "d" key. The guard `if unit in _UNITS` was therefore False for days,
so the day contribution was never added to the running total. Result:
"1d" parsed to 0 and "1d2h" parsed to 7200 (only the hours), i.e. days were
silently discarded instead of being converted.

Fix: register the missing "d" unit (86_400 seconds) in `_UNITS`. The parser
logic itself was already correct; only the unit table was incomplete.
"""

from __future__ import annotations

import re

# Seconds per unit.
# NOTE: "d" (days) MUST be present. Its absence was the root cause of issue #1,
# where day components were silently dropped from the total.
_UNITS = {
    "w": 7 * 24 * 60 * 60,   # weeks   -> 604800 s
    "d": 24 * 60 * 60,       # days    -> 86400 s   <-- fixed (was missing)
    "h": 60 * 60,            # hours   -> 3600 s
    "m": 60,                 # minutes -> 60 s
    "s": 1,                  # seconds -> 1 s
}

_TOKEN_RE = re.compile(r"(\d+)([wdhms])")


def parse_duration(value: str) -> int:
    """Parse a compact duration string (e.g. "1w2d3h4m5s") into total seconds.

    Args:
        value: A string composed of one or more `<int><unit>` tokens, where
            unit is one of w, d, h, m, s. Whitespace between tokens is ignored.

    Returns:
        The total duration in whole seconds.

    Raises:
        ValueError: If the string is empty, contains an unknown unit, or has
            trailing/unparsed characters.
    """
    if not isinstance(value, str):
        raise ValueError(f"duration must be a string, got {type(value).__name__}")

    text = value.strip().lower()
    if not text:
        raise ValueError("duration string is empty")

    total = 0
    consumed = 0

    for match in _TOKEN_RE.finditer(text):
        amount = int(match.group(1))
        unit = match.group(2)

        # `_UNITS` now contains every unit the regex can match (w, d, h, m, s),
        # so this guard is a defensive assertion rather than a silent skip.
        if unit not in _UNITS:
            raise ValueError(f"unknown duration unit: {unit!r}")

        total += amount * _UNITS[unit]
        consumed += len(match.group(0))

    if consumed != len(text):
        raise ValueError(f"could not parse duration string: {value!r}")

    return total


if __name__ == "__main__":
    # Quick self-check covering the regression from issue #1.
    assert parse_duration("1d") == 86_400
    assert parse_duration("2d") == 172_800
    assert parse_duration("1d2h") == 93_600
    assert parse_duration("1w2d3h4m5s") == 788_645
    assert parse_duration("45s") == 45
    print("all duration parser checks passed")
