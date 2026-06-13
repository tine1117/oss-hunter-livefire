import re

_UNITS = {
    'w': 604800,
    'd': 86400,
    'h': 3600,
    'm': 60,
    's': 1,
}

_TOKEN_RE = re.compile(r'(\d+)([wdhms])')


def parse_duration(s: str) -> int:
    """Parse a human-friendly duration string and return total seconds.

    Supported units: w (weeks), d (days), h (hours), m (minutes), s (seconds).

    Examples::

        parse_duration("1h30m")  # 5400
        parse_duration("1d")     # 86400
        parse_duration("2d4h")   # 187200
    """
    if not s:
        raise ValueError("Empty duration string")

    total = 0
    pos = 0
    for match in _TOKEN_RE.finditer(s):
        if match.start() != pos:
            raise ValueError(f"Unrecognised token at position {pos} in {s!r}")
        value = int(match.group(1))
        unit = match.group(2)
        total += value * _UNITS[unit]
        pos = match.end()

    if pos != len(s):
        raise ValueError(f"Unrecognised token at position {pos} in {s!r}")

    return total
