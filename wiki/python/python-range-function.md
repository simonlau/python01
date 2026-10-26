# Python range() Function

> Sources: GeeksforGeeks, 2026-03-10
> Raw: [2026-03-10-python-range-function.md](../../raw/python/2026-03-10-python-range-function.md)
> Updated: 2026-10-26

## Overview

`range()` generates a sequence of integers within a specified range, commonly used to control loop iterations. It returns a lazy iterable (not a full list), generating numbers dynamically to save memory. Convert with `list(range(...))` to access elements like a list.

## Syntax

`range(start, stop, step)` — `start` (optional, default 0) is the starting number; `stop` (required) is where the sequence stops (not included); `step` (optional, default 1) is the difference between consecutive numbers. Returns a range object.

## Examples

- `range(5)` → 0 1 2 3 4 (numbers from 0 to 4).
- `range(5, 10)` → 5 6 7 8 9 (starts at 5, stops before 10).
- `range(0, 10, 2)` → 0 2 4 6 8 (even numbers, step 2).
- `range(10, 0, -2)` → 10 8 6 4 2 (reverse, negative step).

## See Also

- [Code Cultivation — Object-Oriented Garden Systems](code-cultivation.md)
- [Python round() Function](python-round-function.md)
