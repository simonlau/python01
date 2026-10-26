# Python range() function

> Source: https://www.geeksforgeeks.org/python/python-range-function/
> Collected: 2026-10-26
> Published: 2026-03-10

The range() function in Python is used to generate a sequence of integers within a specified range. It is most commonly used in loops to control how many times a block of code runs.

Note: range() returns a lazy iterable, not a full list. It generates numbers dynamically instead of storing them all in memory. To access elements like a list, convert it using list(range(...)).

Example: This example shows the use of range() to generate numbers starting from 0 up to (but not including) a given value.

Python

```
for i in range(5):
    print(i, end=" ")
```

Output

```
0 1 2 3 4 
```

Explanation: range(5) generates numbers from 0 to 4; i takes one value at a time from the generated sequence.

## Syntax

> range(start, stop, step)

Parameters:

- start (optional): Starting number of the sequence (default is 0)

- stop: Number at which the sequence stops (not included)

- step (optional): Difference between consecutive numbers (default is 1)

Return: A range object representing the sequence

## Examples

Example 1: This example generates numbers starting from a custom value and ending before another value.

Python

```
for n in range(5, 10):
    print(n, end=" ")
```

Output

```
5 6 7 8 9 
```

Explanation: range(5, 10) starts at 5 and stops before 10; numbers increase by the default step of 1.

Example 2: This example generates even numbers by skipping values using a custom step size.

Python

```
for v in range(0, 10, 2):
    print(v, end=" ")
```

Output

```
0 2 4 6 8 
```

Explanation: range(0, 10, 2) increases the value by 2 each time; the step controls how much the number changes per iteration.

Example 3: This example demonstrates how range() can be used to generate numbers in reverse order by providing a negative step value.

Python

```
for i in range(10, 0, -2):
    print(i, end=" ")
```

Output

```
10 8 6 4 2 
```

Explanation: range(10, 0, -2) starts from 10 and decreases by 2 each time; a negative step allows backward iteration through numbers.
