# Python __init__ vs __new__

> Sources: GeeksforGeeks, 2025-07-23
> Raw: [2025-07-23-python-init-vs-new.md](../../raw/python/2025-07-23-python-init-vs-new.md)
> Updated: 2026-10-26

## Overview

`__new__` and `__init__` are dunder (magic) methods with distinct roles in object creation. `__new__` is responsible for **creating** the new instance (called first); `__init__` is responsible for **initializing** the instance after creation (called second). `__new__` must return the new instance; `__init__` returns nothing.

## __new__

- Creates the instance; called before `__init__`.
- Typically rarely overridden; commonly used with immutable objects.
- Must return the newly created instance, otherwise creation fails.
- Example: `CustomObject` overrides `__new__` to attach `instance.value` during creation, then returns `instance`.

## __init__

- Initializer/constructor; called automatically when a new instance is created.
- Sets up the object's state/attributes after creation.
- Frequently overridden in most classes.

## Order of Execution

`__new__` runs first (prints/creates), then `__init__` runs (initializes). Example `MyClass(10)` prints "GeeksforGeeks" (from `__new__`) then "10" (from `__init__`).

## Key Differences

| Aspect | `__new__` | `__init__` |
| --- | --- | --- |
| Purpose | Create instance | Initialize instance |
| Called | Before `__init__` | After `__new__` |
| Return | Must return new instance | Returns nothing |
| Usage | Rarely overridden; immutable objects | Frequently overridden |
| Inheritance | Called by class/metaclass | Called on instance |

## See Also

- [Python Classes: The Power of Object-Oriented Programming](python-classes.md)
- [Code Cultivation — Object-Oriented Garden Systems](code-cultivation.md)
