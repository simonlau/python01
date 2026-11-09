#!/usr/bin/env python3
from dataclasses import dataclass


@dataclass(slots=True)
class Plant:
    name: str
    height: float
    days: int

    def __str__(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self.days} days old"

    def show(self) -> None:
        print(self)

    def grow(self) -> None:
        self.days += 1

    def age(self, growth: float) -> None:
        self.height += growth
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
