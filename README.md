# Instrumented algorithms benchmark suite

Sorting and searching implementations that count algorithmic work as well as
wall-clock time.

## Reported result from the original experiment

On weather-series inputs increasing from 256 to 2,048 records, bubble sort rose
from 98,997 to 5,214,307 counted steps while merge sort rose from 3,732 to
41,954. Binary search found a hit in 45 steps versus 4,096 for linear search.

## Executable portfolio layer

The repository includes instrumented insertion/merge sort and duplicate-aware
binary bounds. Tests verify ordering, counters and equal ranges.

```bash
python -m unittest discover -s tests -v
```

The original weather data and parallel 100,000-row benchmark are documented but
not represented as rerun results here.
