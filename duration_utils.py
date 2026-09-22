import re
from typing import Dict

# Regular expression to capture a number followed by a unit character.
# Supported units: weeks (w), days (d), hours (h), minutes (m), seconds (s)
_DURATION_RE = re.compile(r"(?P<value>\d+)(?P<unit>[wdhms])")

# Mapping from unit character to its equivalent number of seconds.
# NOTE: The original implementation missed the 'd' (days) unit.
# Adding it here fixes the bug where days were silently ignored.
_UNIT_SECONDS: Dict[str, int] = {
    "w": 7 * 24 * 60 * 60,   # weeks
    "d": 24 * 60 * 60,       # days
    "h": 60 * 60,            # hours
    "m": 60,                 # minutes
    "s": 1,                  # seconds
}


def parse_duration(duration: str) -> int:
    """
    Parse a human‑friendly duration string into a total number of seconds.

    The function accepts a string composed of one or more `<number><unit>` tokens,
    where ``unit`` is one of ``w`` (weeks), ``d`` (days), ``h`` (hours), ``m``
    (minutes) or ``s`` (seconds). Tokens may appear in any order and are summed.

    Parameters
    ----------
    duration: str
        The duration string to parse, e.g. ``"2d4h30m"``.

    Returns
    -------
    int
        Total duration expressed in seconds.

    Raises
    ------
    ValueError
        If the string contains an unknown unit or malformed token.
    """
    if not isinstance(duration, str):
        raise ValueError("duration must be a string")

    total_seconds = 0
    pos = 0  # track parsing position for error reporting

    for match in _DURATION_RE.finditer(duration):
        # Ensure we are consuming the string sequentially; otherwise there are
        # stray characters (e.g., "1h30x").
        if match.start() != pos:
            raise ValueError(f"Invalid duration format at position {pos}: '{duration}'")
        pos = match.end()

        value = int(match.group("value"))
        unit = match.group("unit")

        try:
            multiplier = _UNIT_SECONDS[unit]
        except KeyError as exc:
            # This should never happen because the regex restricts units,
            # but we keep the guard for future changes.
            raise ValueError(f"Unsupported time unit: {unit}") from exc

        total_seconds += value * multiplier

    # If we didn't consume the whole string, there is an invalid trailing part.
    if pos != len(duration):
        raise ValueError(f"Invalid duration format at position {pos}: '{duration}'")

    return total_seconds
