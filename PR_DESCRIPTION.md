## Summary

Fixes #1: `parse_duration` silently dropped the `d` (days) unit even though
it's documented in the README and already accepted by the tokenizer regex.

- Added `"d": 86400` to the `_UNITS` seconds-per-unit mapping in
  `duration_utils.py`.
- Added regression tests for the two repro cases from the issue:
  `parse_duration("1d") == 86400` and `parse_duration("2d4h") == 187200`.

## Test plan

- [x] `python -m unittest discover -s tests` — all 9 tests pass (7 existing
      + 2 new), including the pre-existing malformed-input
      (`test_invalid_raises`, `test_empty_raises`) and other-unit tests
      (weeks/hours/minutes/seconds), confirming no regressions.
- [x] Manually verified `parse_duration("1d") == 86400` and
      `parse_duration("2d4h") == 187200` at a REPL.

/bounty $50

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
