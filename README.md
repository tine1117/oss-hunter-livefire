# duration-utils

A tiny, dependency-free parser for human-friendly duration strings.

```python
from duration_utils import parse_duration

parse_duration("1h30m")   # 5400
parse_duration("1w")      # 604800
```

Supported units: `w` (weeks), `d` (days), `h` (hours), `m` (minutes), `s` (seconds).

## Develop

```bash
python -m unittest discover -s tests
```

---

> ⚠️ This repository is a **sandbox / test fixture** used to exercise an automated
> bounty-solving workflow end-to-end. It is not a production project.
