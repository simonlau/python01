# Python @staticmethod

> Source: https://www.geeksforgeeks.org/python/python-staticmethod/
> Collected: 2026-10-27
> Published: 2026-01-20

A static method in Python is a method defined inside a class that does not depend on any instance or class data. It is used when a function logically belongs to a class but does not need access to self or cls. Static methods help organize related utility functions inside a class without creating objects.

Example:

Python

```
class Calc:
    @staticmethod
    def add(a, b):
        return a + b

res = Calc.add(2, 3)
print(res)
```

Output

```
5
```

Explanation: @staticmethod makes add() independent of class objects. Calc.add(2, 3) directly calls the method using the class name.

## Syntax

> class ClassName:
> @staticmethod
> def method_name(parameters):
>     method_body

Parameters:

- @staticmethod: Declares the method as static

- parameters: Normal function arguments (no self or cls)

Example 1: This example checks whether a number is even using a static method.

Python

```
class Check:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

print(Check.is_even(10))
```

Output

```
True
```

Explanation: is_even() works independently and does not access any class data.

Example 2: This example converts temperature from Celsius to Fahrenheit.

Python

```
class Temp:
    @staticmethod
    def to_fahrenheit(c):
        return (c * 9/5) + 32

print(Temp.to_fahrenheit(25))
```

Output

```
77.0
```

Explanation: to_fahrenheit() is a utility function grouped inside the class.

Example 3: This example checks whether a given age represents an adult.

Python

```
class Person:
    @staticmethod
    def is_adult(age):
        return age >= 18

print(Person.is_adult(16))
print(Person.is_adult(21))
```

Output

```
False
True
```

Explanation: is_adult() does not need object data, so it is defined as static.
