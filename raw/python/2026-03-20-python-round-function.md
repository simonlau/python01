# round() function in Python

> Source: https://www.geeksforgeeks.org/python/round-function-python/
> Collected: 2026-10-26
> Published: 2026-03-20

round() is a built-in Python function used to round numbers to a specified number of decimal places.

- If only the number is provided, it rounds to the nearest integer.

- If the second argument (ndigits) is given, it rounds the number to that many decimal places.

- It follows Python’s rounding rule (ties are rounded to the nearest even number).

- It returns either an int or a float depending on the input.

## Example

Python

```
n = 45.7
print(round(n))
```

Output

```
46
```

Explanation: round(n) rounds 45.7 to the nearest integer, which is 46.

## Syntax

> round(number, ndigits)

Parameters:

- number: The numeric value to round.

- ndigits (optional): Number of decimal places to round to.

Return: Returns a rounded int or float.

## round() Without ndigits

When the second parameter (ndigits) is not provided, round() automatically rounds the number to the nearest integer. If the number is already an integer, it remains unchanged.

For decimal numbers, Python rounds to the closest integer using its standard rounding rule.

Python

```
print(round(15))
print(round(51.6))
print(round(51.5))
print(round(51.4))
```

Output

```
15
52
52
51
```

Explanation:

- round(15) returns 15 because it is already an integer.

- round(51.6) returns 52 since .6 is greater than .5.

- round(51.5) returns 52 because it rounds to the nearest even integer.

- round(51.4) returns 51 since .4 is less than .5.

## round() With ndigits

When the second parameter (ndigits) is provided, round() rounds the number to the specified number of decimal places.

It checks the digit after the required decimal place and rounds accordingly using Python’s standard rounding rule.

Python

```
print(round(2.665, 2))
print(round(2.676, 2))
print(round(2.673, 2))
```

Output

```
2.67
2.68
2.67
```

Explanation:

- round(2.665, 2) rounds to two decimal places and returns 2.67.

- round(2.676, 2) increases the second decimal because the next digit is greater than 5.

- round(2.673, 2) keeps the second decimal unchanged because the next digit is less than 5.

## round() with Negative Numbers

round() works the same way for negative numbers as it does for positive numbers. It rounds to the nearest integer (or specified decimal place) based on closeness. When the value ends in .5, Python applies the “round to nearest even” rule.

Python

```
print(round(-3.2))
print(round(-4.7))
print(round(-2.5))
print(round(-2.675, 2))
print(round(-1234, -2))
```

Output

```
-3
-5
-2
-2.67
-1200
```

Explanation:

- round(-3.2) returns -3 because it is closer to -3 than -4.

- round(-4.7) returns -5 because it is closer to -5.

- round(-2.5) returns -2 due to the nearest even rule.

- round(-2.675, 2) rounds to two decimal places.

- round(-1234, -2) rounds to the nearest hundred (10²).

## Rounding with math Module

The math module provides functions to always round a number down or up, regardless of its decimal value.

- math.floor() rounds down to the nearest integer.

- math.ceil() rounds up to the nearest integer.

Python

```
import math

n = 3.6
print(math.floor(n))
print(math.ceil(n))
```

Output

```
3
4
```

Explanation:

- math.floor(n) returns the largest integer less than or equal to n.

- math.ceil(n) returns the smallest integer greater than or equal to n.

## Rounding with NumPy

The NumPy library provides the np.round() function to round multiple numeric values at once. It is useful when working with arrays, especially in data analysis and scientific computing.

Python

```
import numpy as np
a = np.array([-2.675, -1.23456789, -3.14159265])
print(np.round(a, 3))
```

Output

```
[-2.675 -1.235 -3.142]
```

Explanation: np.round(a, 3) rounds each element in array a to 3 decimal places.

## Rounding Up

When rounding a number to the nearest integer using round(), values with decimal part .5 or greater are rounded upward (based on standard rounding rules).

Python

```
print(round(12))
print(round(12.7))
```

Output

```
12
13
```

Explanation:

- round(12) remains 12 since it is already an integer.

- round(12.7) becomes 13 because .7 is greater than .5.

## Rounding Down

Numbers with a decimal part less than .5 are rounded down to the nearest integer using round().

Python

```
print(round(12))
print(round(12.1))
print(round(12.4))
print(round(12.5))
```

Output

```
12
12
12
12
```

Explanation:

- round(12.1) and round(12.4) round down because the decimal part is less than .5.

- round(12.5) returns 12 due to Python’s “round to nearest even” rule.

## Errors in round()

round() works only with numeric values (int, float). If a non-numeric value is passed, Python raises a TypeError.

Python

```
print(round("a", 2))
```

Output

> ERROR!
> Traceback (most recent call last):
> File "<main.py>", line 1, in <module>
> TypeError: type str doesn't define __round__ method

Explanation: round("a", 2) raises an error because strings do not support the rounding operation.

## Practical Applications

Rounding is commonly used to limit decimal places in calculations, especially when working with fractions that produce long decimal results.

Python

```
b = 1/3
print(b)
print(round(b, 2))
```

Output

```
0.3333333333333333
0.33
```

Explanation: round(b, 2) limits the value of b to two decimal places, making the output cleaner and easier to use in reports or calculations.
