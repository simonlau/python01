# Data Classes in Python

> Sources: Geir Arne Hjelle (Real Python), 2018-05-15
> Raw: [python-data-classes.md](../../raw/python/python-data-classes.md)
> Updated: 2026-11-09

## Overview

A Python data class (introduced in Python 3.7 via `@dataclass`) is a class mainly for storing data, with boilerplate methods like `.__init__()`, `.__repr__()`, and `.__eq__()` generated automatically from annotated fields. Data classes reduce repetition while remaining regular classes: you can add methods, defaults, ordering, immutability, inheritance, and slots. They compare to alternatives like `tuple`, `dict`, `namedtuple`, and `attrs`, with trade-offs around mutability, validation, and tuple compatibility.

## Data Class in a Nutshell

```python
from dataclasses import dataclass


@dataclass
class DataClassCard:
    rank: str
    suit: str
```

Instances get readable representation and equality for free:

```python
>>> queen_of_hearts = DataClassCard('Q', 'Hearts')
>>> queen_of_hearts.rank
'Q'
>>> queen_of_hearts
DataClassCard(rank='Q', suit='Hearts')
>>> queen_of_hearts == DataClassCard('Q', 'Hearts')
True
```

A regular class needs `.__init__`, `.__repr__`, and `.__eq__` written by hand to match this behavior.

## Alternatives

- `tuple`/`dict`: lightweight but error-prone (positional access, inconsistent keys).
- `namedtuple`: tuple subclass with named fields; compares equal to plain tuples and is immutable; defaults are awkward.
- `attrs`: feature-rich (converters/validators) but external dependency.
- Data classes: standard library, mutable by default, generated methods, flexible.

## Basic Data Classes

```python
from dataclasses import dataclass


@dataclass
class Position:
    name: str
    lon: float
    lat: float
```

Create with `make_dataclass('Position', ['name', 'lat', 'lon'])` if desired. Fields require type hints (use `typing.Any` if no explicit type), but types are not enforced at runtime.

### Default Values

```python
@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0
```

### Adding Methods

Data classes are regular classes; add methods normally:

```python
@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other): ...
```

## More Flexible Data Classes

### Advanced Default Values

Avoid mutable default arguments; use `field(default_factory=...)`:

```python
from dataclasses import dataclass, field
from typing import List


@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)
```

`field()` supports `default`, `default_factory`, `init`, `repr`, `compare`, `hash`, and `metadata`. Retrieve field info with `fields()`.

### Representation

Override `.__repr__()`/`.__str__()` for custom output. `.__str__()` falls back to `.__repr__()` if not defined.

### Comparing Cards

Enable ordering with `@dataclass(order=True)`. Fields are compared like tuples; use a `sort_index` field computed in `.__post_init__()` for custom ordering:

```python
@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = RANKS.index(self.rank) * len(SUITS) + SUITS.index(
            self.suit
        )
```

## Immutable Data Classes

Set `frozen=True` to prevent field reassignment:

```python
@dataclass(frozen=True)
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0
```

Assignment raises `FrozenInstanceError`. Note that mutable nested fields (e.g., `list`) can still change; use immutable types (e.g., `tuple`) to avoid this.

## Inheritance

Subclasses inherit and extend fields. If a base field has a default, all new subclass fields must also have defaults (Python argument ordering rule). Redefined fields keep their original position but use the new default.

## Optimizing Data Classes

Use `__slots__` to reduce memory and improve speed:

```python
@dataclass
class SlotPosition:
    __slots__ = ["name", "lon", "lat"]
    name: str
    lon: float
    lat: float
```

Slots classes cannot have default values and restrict attribute creation.

## See Also

- [Python Classes: The Power of Object-Oriented Programming](python-classes.md)
- [Encapsulation in Python](python-encapsulation.md)