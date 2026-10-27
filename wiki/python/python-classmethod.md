# @classmethod in Python

> Sources: GeeksforGeeks, 2026-06-08
> Raw: [2026-06-08-python-classmethod.md](../../raw/python/2026-06-08-python-classmethod.md)
> Updated: 2026-10-27

## Overview

`@classmethod` creates a method that works with the class itself rather than an instance. The first parameter is `cls` (the class). Common uses: accessing class variables and creating factory methods (alternative constructors). Can also be applied via `classmethod(func)` directly.

## Syntax

```python
class ClassName:
    @classmethod
    def method_name(cls, args):
        # method body
```

## Examples

- `Student.show_course()` → `Python` (accesses class variable `course`).
- `Car.show_brand()` → `Toyota` (accesses class variable `brand`).
- `User.from_string("Alex-21")` → creates `User("Alex", 21)` via `cls()`.
- `Demo.show = classmethod(Demo.show)` then `Demo.show()` → `GeeksforGeeks`.

## See Also

- [Python Classes: The Power of Object-Oriented Programming](python-classes.md)
- [Python @staticmethod](python-staticmethod.md)
- [Python __init__ vs __new__](python-init-vs-new.md)
- [Supercharge Your Classes With Python super()](python-super.md)
