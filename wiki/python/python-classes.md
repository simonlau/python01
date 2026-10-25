# Python Classes: The Power of Object-Oriented Programming

> Sources: Leodanis Pozo Ramos, 2026-04-01
> Raw: [2026-04-01-python-classes-power-of-oop.md](../../raw/python/2026-04-01-python-classes-power-of-oop.md)
> Updated: 2026-10-25

## Overview

A comprehensive tutorial on Python classes and object-oriented programming. A class is a reusable blueprint defined with the `class` keyword that bundles **attributes** (state/data) and **methods** (behavior); instances are created by calling the class constructor. The article covers naming conventions, class vs instance attributes, `.__dict__`, dynamic attributes, properties and descriptors, `.__slots__`, instance/class/static methods, special methods and protocols, debugging, data classes, enumerations, single/multiple inheritance, MRO, mixins, composition, delegation, dependency injection, abstract base classes, and polymorphism.

## Getting Started

- Syntax: `class ClassName:` with an indented body; attributes and methods live in the class namespace.
- Example `Circle` class with `.__init__(self, radius)` setting `self.radius` and a `calculate_area()` method returning `math.pi * self.radius ** 2`.
- Instantiation: `circle_1 = Circle(42)`; access members via dot notation `obj.attribute` / `obj.method()`; assignment updates state.

## Naming Conventions

- Classes use PascalCase; functions/methods/variables use snake_case.
- No hard private/protected/public distinction; convention: leading underscore marks non-public members (e.g., `_radius`), not part of the public API.
- Double leading underscore triggers name mangling: `__value` becomes `_ClassName__value`, hiding the name from direct outside access (still reachable via mangled name, but discouraged).

## Benefits and When to Avoid

Benefits: model real-world problems, reuse code via hierarchies, encapsulate data+behavior, abstract implementation details, enable polymorphism.

Avoid classes when: storing only data (use data classes, enums, named tuples); providing a single method (use a function); wrapping built-in/third-party functionality; small scripts; performance-critical code with many objects; legacy/functional codebases.

## Attaching Data

- **Class attributes**: defined in class body; shared across all instances. Modifying via an instance creates a new instance attribute instead (shadowing). Use `type(self)` rather than hard-coding the class name when incrementing.
- **Instance attributes**: tied to a concrete instance; usually defined in `.__init__()` using `self`.
- **`.__dict__`**: dictionary of writable members; classes hold class attributes/methods, instances hold instance attributes. Python looks up instance members in instance `.__dict__`, then class `.__dict__`.
- **Dynamic attributes**: can be added at runtime via `setattr()` or direct assignment; useful when attribute set is unknown upfront (e.g., CSV rows).
- **Properties**: `@property` getter + `@attr.setter` for managed attributes with validation without changing the API. Example: `Circle.radius` validates positive `int`/`float`, raising `ValueError` otherwise.
- **Descriptors**: implement `.__get__`/`.__set__` (and `.__set_name__`) to reuse validation logic across classes (e.g., `PositiveNumber` shared by `Circle` and `Square`).
- **`.__slots__`**: tuple of allowed attribute names; prevents `.__dict__` creation, reducing memory (example: `Point(4, 8)` 112 bytes with slots vs 504 bytes without — over 4x). Also prevents adding new attributes dynamically.

## Providing Behavior With Methods

- **Instance methods**: first argument `self` (convention); Python passes the instance automatically when called via an object, or manually via the class.
- **Special methods / protocols**: dunder methods called automatically for specific operations (e.g., `.__str__`, `.__repr__`, `.__iter__`). Protocols: Iterator, Iterable, Descriptor, Context manager.
- **Class methods**: `@classmethod`, first argument `cls`; common for alternative constructors (e.g., `ThreeDPoint.from_sequence`).
- **Static methods**: `@staticmethod`; independent functions bundled in a class for API consistency.
- **Getter/setter vs properties**: Python prefers exposing attributes directly; convert to a property later if function-like behavior is needed (e.g., uppercasing in `Person.name` setter) without breaking the API.

## Complete Example: Employee

Demonstrates combining features: class attribute `company = "Example, Inc."`; instance attributes `name`, `birth_date` (property converting ISO string to `datetime`); instance method `compute_age()`; class method `from_dict()`; `.__str__()`/`.__repr__()`.

## Debugging

Common exceptions: `AttributeError` (missing member), `TypeError` (unsupported operation), `NotImplementedError` (unimplemented abstract method). Common mistakes: forgetting `self`, not instantiating, confusing class/instance attributes, accessing non-public members, overusing inheritance.

## Specialized Standard-Library Classes

- **Data classes** (`@dataclass`): generate `.__init__`, `.__repr__`, `.__eq__`, etc. from annotated fields; can include methods. Example `ThreeDPoint` with `x`, `y`, `z`.
- **Enumerations** (`enum.Enum`): named constants grouped together; members are immutable, iterable, accessible via dot/call/dict notation; `.name`/`.value`; can add methods.

## Inheritance

- Simple inheritance: `class Child(Parent)`; use `super().__init__(...)` to initialize parent state.
- Class hierarchies express is-a relationships; each level adds specialization.
- Extended vs overridden methods: extend by calling `super().method()` then adding; override by replacing entirely.
- Multiple inheritance: `class FlyingCar(Car, Aircraft)`; MRO resolves method lookup (current class → leftmost parents → ... → `object`); inspect via `.__mro__`.
- Mixins: reusable functionality bundles not representing types (e.g., `SerializerMixin` providing `to_json`/`to_pickle`); place before base classes in MRO.
- Benefits: reusability, modularity, maintainability, polymorphism, extensibility. Pitfalls: complexity, diamond problem, fragile base classes.

## Alternatives to Inheritance

- **Composition** (has-a): build objects from components; runtime-flexible; preserves encapsulation (e.g., `IndustrialRobot` with `Body` and `Arm`).
- **Delegation** (can-do): hand tasks to another object; `Stack` delegating to an internal list; can implement via `.__getattr__`.
- **Dependency injection**: pass dependencies in from outside to decouple components.

## Abstract Base Classes and Interfaces

- `abc.ABC` + `@abstractmethod` defines an interface; subclasses cannot be instantiated until all abstract methods are implemented. Example `Shape` requiring `get_area()`/`get_perimeter()`.
- Alternative: `typing.Protocol` for structural subtyping (duck typing).

## Polymorphism

Objects of different classes used interchangeably via a shared interface (duck typing). Example: renaming `Motorcycle.ride()` to `.drive()` so cars and motorcycles share a common method.

## See Also

- [Code Cultivation — Object-Oriented Garden Systems](code-cultivation.md)
- Real Python: [Object-Oriented Programming (OOP) in Python](https://realpython.com/python3-object-oriented-programming/) (referenced by source)
