# Supercharge Your Classes With Python super()

> Sources: Kyle Stratis, 2019-02-12
> Raw: [2019-02-12-python-super.md](../../raw/python/2019-02-12-python-super.md)
> Updated: 2026-10-27

## Overview

`super()` gives a subclass access to methods of its superclass, avoiding code duplication and supporting both single and multiple inheritance. It returns a temporary proxy object of the superclass. Common use: extending functionality of previously built classes.

## Single Inheritance

- `super().__init__(...)` calls the parent's initializer (e.g., `Square` calling `Rectangle.__init__(length, length)`).
- Subclasses inherit methods automatically (e.g., `Cube` uses `Rectangle.area()` via inheritance).
- Extend methods by calling `super().method()` (e.g., `Cube.surface_area()` = `super().area() * 6`).
- If `__init__` doesn't differ, it can be omitted and the parent's is used automatically.

## Deep Dive

- Parameterless `super()` in Python 3 is equivalent to `super(Subclass, self)`.
- Two parameters: subclass and an instance of it. The instance provides a bound method (object context); without it, an unbound function.
- You can start the search at a higher level: `super(Square, self).area()` skips `Square` and starts at `Rectangle`.
- `super()` returns a proxy object, not a method.

## Multiple Inheritance

- A subclass can inherit from multiple (sibling) superclasses.
- **MRO (Method Resolution Order)**: `Class.__mro__` lists the search order; Python uses it to resolve methods.
- Example MROs: `RightPyramid(Triangle, Square)` → RightPyramid, Triangle, Square, Rectangle, object. Reordering to `RightPyramid(Square, Triangle)` → RightPyramid, Square, Rectangle, Triangle, object.
- Cooperative design: rename colliding methods (e.g., `Triangle.area` → `tri_area`), add `super().__init__()` calls up the chain, and pass `**kwargs` through the MRO so each class pops its own arguments.
- Result: `RightPyramid(base=2, slant_height=4)` → `area()` and `area_2()` both return `20.0`.

## Alternatives

- **Composition** instead of multiple inheritance for cleaner code.
- **Mixins**: simple classes providing reusable behavior (e.g., `VolumeMixin` gives `volume = area() * height`); `Cube(VolumeMixin, Square)` yields `surface_area()` 24 and `volume()` 8 for side length 2.

## See Also

- [Python Classes: The Power of Object-Oriented Programming](python-classes.md)
- [Python __init__ vs __new__](python-init-vs-new.md)
- [Code Cultivation — Object-Oriented Garden Systems](code-cultivation.md)
