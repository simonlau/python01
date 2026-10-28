# Final Names, Methods, and Classes in Python

> Sources: mypy 2.4.0 documentation, Unknown
> Raw: [final-names-methods-and-classes.md](../../raw/python/final-names-methods-and-classes.md)
> Updated: 2026-10-28

## Overview

mypy supports three related features for restricting modification and inheritance: **final names** (variables/attributes that must not be reassigned), **final methods** (methods that must not be overridden), and **final classes** (classes that must not be subclassed). These are enforced only by mypy in annotated code, not at runtime. `Final` and `final` come from `typing` (Python 3.8+; use `typing_extensions` for 3.4–3.7).

## Final Names

`typing.Final` indicates that a name or attribute should not be reassigned, redefined, or overridden. It is useful for module/class constants and for protecting attributes from subclass overrides.

```python
from typing import Final

RATE: Final = 3_000

class Base:
    DEFAULT_ID: Final = 0

RATE = 300           # Error: can't assign to final attribute
Base.DEFAULT_ID = 1  # Error: can't override a final attribute
```

`@property` can make an attribute read-only, but unlike `Final` it does not work with module attributes and does not prevent overriding in subclasses.

### Syntax Variants

- `Final[<type>]` with an explicit type: `ID: Final[int] = 1` (mypy infers `int`).
- Omit the type: `ID: Final = 1` (mypy infers `Literal[1]`, not `Final[Any]`).
- In class bodies/stub files, omit the right-hand side: `ID: Final[int]`.
- Instance attributes in `__init__`: `self.id: Final = 1` (assigned once per instance).

### Details

- At most one final declaration per module/class for a given attribute; no separate class- and instance-level constants with the same name.
- Exactly one assignment to a final name.
- A final attribute declared without an initializer in the class body must be initialized in `__init__` (stub files may skip the initializer).
- `Final` must be the outermost type; it cannot be nested (e.g., `list[Final[int]]` is an error) or used for function arguments.
- `Final` and `ClassVar` should not be used together; mypy infers scope from where initialization happens.
- A final attribute cannot be overridden by a subclass, but a final attribute can override a read-only property.
- `Final` prevents re-binding, not mutation. Use immutable ABCs/containers to prevent mutation:

```python
x: Final = ['a', 'b']
x.append('c')          # OK

y: Final[Sequence[str]] = ['a', 'b']
y.append('x')          # Error: Sequence is immutable
z: Final = ('a', 'b')  # Also an option
```

## Final Methods

Use `typing.final` to prevent a method from being overridden in a subclass. It works with instance, class, static methods, and properties.

```python
from typing import final

class Base:
    @final
    def common_name(self) -> None:
        ...

class Derived(Base):
    def common_name(self) -> None:  # Error: cannot override a final method
        ...
```

For overloaded methods, apply `@final` to the implementation (or the first overload in stubs).

## Final Classes

Apply `typing.final` to a class to indicate it should not be subclassed. It is a declaration for mypy and documentation for humans; it does not prevent subclassing at runtime.

```python
from typing import final

@final
class Leaf:
    ...

class MyLeaf(Leaf):  # Error: Leaf can't be subclassed
    ...
```

Useful when a class was not designed for subclassing, subclassing would harm maintainability, or you want freedom to change implementation later. A `@final` abstract class (with abstract methods/properties) causes a mypy error, since those attributes could never be implemented.

## See Also

- [Python Classes: The Power of Object-Oriented Programming](python-classes.md)
- [Code Cultivation — Object-Oriented Garden Systems](code-cultivation.md)