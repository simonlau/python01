#!/usr/bin/env python3
from dataclasses import dataclass
from typing import NewType, TypeGuard

PositiveInt = NewType("PositiveInt", int)
PositiveFloat = NewType("PositiveFloat", float)


def is_positive_int(num: int) -> TypeGuard[PositiveInt]:
    return num > 0


def is_positive_float(num: float) -> TypeGuard[PositiveFloat]:
    return num > 0


@dataclass(slots=True)
class Plant:
    name: str
    height: PositiveFloat
    days: PositiveInt

    def __init__(self, name: str, height: float, days: int):
        if not is_positive_float(height):
            msg = "Height must be a positive float"
            raise ValueError(msg)

        if not is_positive_int(days):
            msg = "Days must be a positive int"
            raise ValueError(msg)

        self.name = name
        self.height = height
        self.days = days

    def __str__(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self.days} days old"

    def show(self) -> None:
        print(self)

    def grow(self) -> None:
        self.days = PositiveInt(self.days + 1)

    def age(self, growth: float) -> None:
        self.height = PositiveFloat(self.height + growth)
        self.grow()


def main() -> None:
    plants: list[Plant] = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant}")


if __name__ == "__main__":
    main()
