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
        return f"{self.name}: {self.height}cm, {self.days} days old"

    def show(self) -> None:
        print(self)


def main() -> None:
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    main()
