# Instrumented algorithms benchmark suite

> **Provenance and scope.** Coursework portfolio reconstruction, 2026. Included: instrumented insertion/merge sort and duplicate-aware binary bounds with tests. The original weather inputs, bubble-sort instrumentation and assessment report are not included. Original step counts must not be compared with the current counters without matching their definitions.

Sorting and searching implementations that count algorithmic work as well as
wall-clock time.

## Reported result from the original experiment

On weather-series inputs increasing from 256 to 2,048 records, bubble sort rose
from 98,997 to 5,214,307 counted steps while merge sort rose from 3,732 to
41,954.

## Executable portfolio layer

The repository includes instrumented insertion/merge sort and duplicate-aware
binary bounds. Tests verify ordering, counters and equal ranges.

```bash
python -m unittest discover -s tests -v
```

The original weather data and parallel 100,000-row benchmark are documented but
not represented as rerun results here.


## Counter definitions

The earlier “45 steps” binary-search claim has been removed because the original counting convention is unavailable. It was not a supported count of key comparisons. In this implementation `Result.steps = comparisons + writes + swaps` for sorting. `equal_range` performs two binary bounds and does not report a comparison counter. Sorting counts, bound-search iterations and wall-clock time are different measures.

## Licence

Original material is available for portfolio evaluation under the [evaluation-only licence](LICENSE). Third-party data, libraries and original assessment materials retain their own terms.
