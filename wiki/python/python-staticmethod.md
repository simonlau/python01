# Python @staticmethod

> Sources: GeeksforGeeks, 2026-01-20
> Raw: [2026-01-20-python-staticmethod.md](../../raw/python/2026-01-20-python-staticmethod.md)
> Updated: 2026-10-27

## Overview

`@staticmethod` defines a method inside a class that does not depend on any instance or class data. It is used when a function logically belongs to a class but needs neither `self` nor `cls`. Static methods organize related utility functions inside a class without requiring object creation. They are called directly on the class: `ClassName.method(args)`.

## Syntax

```python
class ClassName:
    @staticmethod
    def method_name(parameters):
        method_body
```

`parameters` are normal function arguments (no `self`/`cls`).

## Examples

- `Calc.add(2, 3)` → `5` (independent of class objects).
- `Check.is_even(10)` → `True`.
- `Temp.to_fahrenheit(25)` → `77.0`.
- `Person.is_adult(16)` → `False`; `Person.is_adult(21)` → `True`.

## See Also

- [Python Classes: The Power of Object-Oriented Programming](python-classes.md)
- [Python __init__ vs __new__](python-init-vs-new.md)
- [Supercharge Your Classes With Python super()](python-super.md)
