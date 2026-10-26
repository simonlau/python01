# Python round() Function

> Sources: GeeksforGeeks, 2026-03-20
> Raw: [2026-03-20-python-round-function.md](../../raw/python/2026-03-20-python-round-function.md)
> Updated: 2026-10-26

## Overview

`round()` is a built-in Python function that rounds a number to a specified number of decimal places. With only the number, it rounds to the nearest integer. With `ndigits`, it rounds to that many decimal places. Python uses banker’s rounding (ties round to the nearest even number). It returns an `int` when `ndigits` is omitted, otherwise a `float`.

## Syntax

`round(number, ndigits)` — `number` is the value to round; `ndigits` (optional) is the number of decimal places.

## Without ndigits

Rounds to the nearest integer (already-integer inputs stay unchanged):

- `round(15)` → `15`
- `round(51.6)` → `52`
- `round(51.5)` → `52` (nearest even)
- `round(51.4)` → `51`

## With ndigits

Rounds to the given number of decimal places:

- `round(2.665, 2)` → `2.67`
- `round(2.676, 2)` → `2.68`
- `round(2.673, 2)` → `2.67`

## Negative Numbers

Works the same as for positives; ties use nearest-even:

- `round(-3.2)` → `-3`
- `round(-4.7)` → `-5`
- `round(-2.5)` → `-2`
- `round(-2.675, 2)` → `-2.67`
- `round(-1234, -2)` → `-1200` (rounds to nearest hundred)

## Alternatives: math and NumPy

- `math.floor()` rounds down; `math.ceil()` rounds up (e.g., `math.floor(3.6)` → `3`, `math.ceil(3.6)` → `4`).
- `np.round(array, ndigits)` rounds arrays element-wise (e.g., `np.round([-2.675, -1.23456789, -3.14159265], 3)` → `[-2.675, -1.235, -3.142]`).

## Rounding Up / Down

- `round(12.7)` → `13` (decimal ≥ .5 rounds up under standard rules).
- `round(12.1)` and `round(12.4)` → `12` (decimal < .5 rounds down).
- `round(12.5)` → `12` (nearest even).

## Errors

`round()` accepts only numeric values; non-numeric input raises `TypeError` (e.g., `round("a", 2)`).

## Practical Application

Limiting decimal places in calculations: `b = 1/3` → `0.3333333333333333`; `round(b, 2)` → `0.33`.

## See Also

- [Code Cultivation — Object-Oriented Garden Systems](code-cultivation.md)
- [Python Classes: The Power of Object-Oriented Programming](python-classes.md)
