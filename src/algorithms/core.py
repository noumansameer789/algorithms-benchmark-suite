"""Instrumented sorting and searching algorithms used in the portfolio demo."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass
class Result:
    values: list[float]
    comparisons: int = 0
    writes: int = 0
    swaps: int = 0

    @property
    def steps(self) -> int:
        return self.comparisons + self.writes + self.swaps


def insertion_sort(values: Iterable[float]) -> Result:
    data = list(values)
    result = Result(data)
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0:
            result.comparisons += 1
            if data[j] <= key:
                break
            data[j + 1] = data[j]
            result.writes += 1
            j -= 1
        data[j + 1] = key
        result.writes += 1
    return result


def merge_sort(values: Iterable[float]) -> Result:
    data = list(values)
    result = Result(data)

    def sort(lo: int, hi: int) -> None:
        if hi - lo <= 1:
            return
        mid = (lo + hi) // 2
        sort(lo, mid)
        sort(mid, hi)
        left, right = data[lo:mid], data[mid:hi]
        i = j = 0
        for k in range(lo, hi):
            if i >= len(left):
                data[k] = right[j]
                j += 1
            elif j >= len(right):
                data[k] = left[i]
                i += 1
            else:
                result.comparisons += 1
                if left[i] <= right[j]:
                    data[k] = left[i]
                    i += 1
                else:
                    data[k] = right[j]
                    j += 1
            result.writes += 1

    sort(0, len(data))
    return result


def equal_range(values: Sequence[float], target: float) -> tuple[int, int]:
    """Return the half-open range containing every duplicate of target."""

    def bound(right: bool) -> int:
        lo, hi = 0, len(values)
        while lo < hi:
            mid = (lo + hi) // 2
            if values[mid] < target or (right and values[mid] == target):
                lo = mid + 1
            else:
                hi = mid
        return lo

    return bound(False), bound(True)
