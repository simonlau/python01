# Getters and Setters: Manage Attributes in Python

> Sources: Leodanis Pozo Ramos (Real Python), 2026-10-30
> Raw: [python-getter-setter.md](../../raw/python/python-getter-setter.md)
> Updated: 2026-11-09

## Overview

Getter and setter methods allow access and mutation of non-public attributes while maintaining encapsulation. In Python, however, public attributes are preferred, and properties (`@property`) are the Pythonic way to attach behavior to attributes. Getters/setters remain useful for slow operations, extra arguments/flags, inheritance scenarios, raising exceptions, and heterogeneous/migration contexts. Advanced alternatives include descriptors and `.__getattr__()`/`.__setattr__()`.

## Getter and Setter Methods

A getter accesses an attribute; a setter mutates it. Typically attributes are made non-public (single underscore) and managed through methods:

```python
class Label:
    def __init__(self, text, font):
        self._text = text
        self._font = font

    def get_text(self):
        return self._text

    def set_text(self, value):
        self._text = value
```

Use them when internal implementation may change (e.g., transforming text to uppercase) without breaking the API.

## Properties: The Python Way

Properties pack getter/setter/delete logic behind normal attribute syntax, avoiding breaking changes:

```python
from datetime import date


class Employee:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = date.fromisoformat(value)
```

PEP 8 recommends exposing simple public attributes and using properties only when functional behavior is needed. Avoid side effects in properties and keep them fast.

## Advanced Alternatives

### Descriptors

Descriptors implement `.__get__()`, `.__set__()`, and `.__set_name__()` for reusable attributes with attached behavior. Properties are a special case of descriptors.

```python
class Date:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = date.fromisoformat(value)
```

### `.__getattr__()` and `.__setattr__()`

These special methods allow generic transformations on attribute access/mutation:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattr__(self, name):
        return self.__dict__[f"_{name}"]

    def __setattr__(self, name, value):
        self.__dict__[f"_{name}"] = float(value)
```

## When to Prefer Getters/Setters Over Properties

- **Slow operations**: traditional methods make cost explicit.
- **Extra arguments/flags**: setters can accept additional parameters (properties cannot).
- **Inheritance**: properties are inherited as a whole; overriding a getter overrides the whole property. Getters/setters are independent and inherit cleanly.
- **Raising exceptions**: traditional methods make exceptional behavior more explicit.
- **Team integration/migration**: familiar pattern for developers from Java/C++; eases future language migration.

## See Also

- [Encapsulation in Python](python-encapsulation.md)
- [Python Classes: The Power of Object-Oriented Programming](python-classes.md)
- [Python Data Classes](python-data-classes.md)