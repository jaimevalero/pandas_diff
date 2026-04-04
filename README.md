# pandas_diff

[![CI](https://github.com/jaimevalero/pandas_diff/actions/workflows/python-test.yml/badge.svg)](https://github.com/jaimevalero/pandas_diff/actions/workflows/python-test.yml)
[![PyPI](https://img.shields.io/pypi/v/pandas_diff)](https://pypi.org/project/pandas_diff/)
[![Python](https://img.shields.io/pypi/pyversions/pandas_diff)](https://pypi.org/project/pandas_diff/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Generate event logs of row-level changes between two pandas DataFrames.

Not a statistical comparison tool — pandas_diff tells you **what changed**: which rows were created, deleted, or modified, and exactly which fields changed.

## Installation

```bash
pip install pandas_diff

# With Parquet support
pip install pandas_diff[parquet]
```

## Quick start

```python
import pandas as pd
from pandas_diff import get_diffs

before = pd.DataFrame([
    {"hero": "hulk", "power": "strength"},
    {"hero": "black_widow", "power": "spy"},
    {"hero": "thor", "hammers": 0},
])
after = pd.DataFrame([
    {"hero": "hulk", "power": "smart"},
    {"hero": "captain marvel", "power": "strength"},
    {"hero": "thor", "hammers": 2},
])

df = get_diffs(before, after, keys="hero")
```

| operation | object_keys | object_values  | attribute_changed | old_value | new_value |
|-----------|-------------|----------------|-------------------|-----------|-----------|
| create    | [hero]      | captain marvel |                   |           |           |
| delete    | [hero]      | black_widow    |                   |           |           |
| modify    | [hero]      | hulk           | power             | strength  | smart     |
| modify    | [hero]      | thor           | hammers           | 0         | 2         |

## CLI

```bash
pandas_diff before.csv after.csv --keys id
pandas_diff old.parquet new.parquet --keys name,date --format json
pandas_diff a.csv b.csv --keys id --ignore updated_at -o diff.csv
```

Supported file formats: CSV, JSON (flat records), Parquet.

## Use cases

- **Batch to event-driven migration** — Detect changes between pipeline runs and stream them to Kafka.
- **Audit event logs** — Track how resources change over time.
- **Data conciliation** — Compare a CMDB against the real state of infrastructure.
- **Environment sync** — Propagate changes between production and disaster recovery.

## API

```python
get_diffs(
    before: pd.DataFrame,      # Previous state
    after: pd.DataFrame,        # Current state
    keys: list[str] | str,      # Column(s) identifying each row
    ignore_columns: list[str],  # Columns to skip (optional)
) -> pd.DataFrame
```

Returns a DataFrame with columns: `operation`, `object_keys`, `object_values`, `object_json`, `attribute_changed`, `old_value`, `new_value`.

## License

MIT
