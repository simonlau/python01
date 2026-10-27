# Python range() Function

> Sources: GeeksforGeeks, 2026-03-10; Geir Arne Hjelle, 2024-11-24
> Raw: [2026-03-10-python-range-function.md](../../raw/python/2026-03-10-python-range-function.md); [2024-11-24-python-range.md](../../raw/python/2024-11-24-python-range.md)
> Updated: 2026-10-27

## Overview

`range()` generates a sequence of integers within a specified range, commonly used to control loop iterations. It returns a lazy iterable (not a full list), generating numbers dynamically to save memory. Convert with `list(range(...))` to access elements like a list.

## Syntax

`range(start, stop, step)` — `start` (optional, default 0) is the starting number; `stop` (required) is where the sequence stops (not included); `step` (optional, default 1) is the difference between consecutive numbers. Returns a range object.

## Examples

- `range(5)` → 0 1 2 3 4 (numbers from 0 to 4).
- `range(5, 10)` → 5 6 7 8 9 (starts at 5, stops before 10).
- `range(0, 10, 2)` → 0 2 4 6 8 (even numbers, step 2).
- `range(10, 0, -2)` → 10 8 6 4 2 (reverse, negative step).

## Negative Ranges

Ranges can include negative numbers: `range(-10, 0)` → -10..-1; `range(-7, -3)` → -7..-4. Number of elements = stop - start (e.g., (-3) - (-7) = 4).

## Empty Ranges

- `range(0)` or `range(1, 1)` → empty.
- If start >= stop (with positive step), range is empty.
- `len(range(0))` → 0.

## Counting Backward

- Negative step counts down: `range(20, 0, -2)` → 20 18 ... 2; `range(5, -1, -1)` → 5 4 3 2 1 0.
- With negative step, empty if start <= stop.
- `reversed(range(...))` reverses a range (returns a range_iterator).

## Loop Alternatives

- Loop directly over elements instead of indices when possible.
- `enumerate(iterable, start=...)` for index + element (e.g., `enumerate(word, start=1)`).
- `zip(seq1, seq2)` for parallel iteration over multiple sequences.

## Other Features

- **Access**: `range(1, 20, 2)[3]` → 7; negative indices supported.
- **Slices**: `range(1, 20, 2)[1:5]` → `range(3, 11, 2)`.
- **Membership**: `year in range(2000, 2100, 4)` is fast; members are always integers.
- **Length**: `len(range(1, 20, 2))` → 10 (use `len()`, not manual calculation).
- **Reversal**: `range[::-1]` supports all step sizes.
- **Integer-like params**: `range()` accepts objects implementing `.__index__()` (e.g., binary `0b110`, hex `0xeb`, custom `PiDigits`).

## See Also

- [Code Cultivation — Object-Oriented Garden Systems](code-cultivation.md)
- [Python round() Function](python-round-function.md)
