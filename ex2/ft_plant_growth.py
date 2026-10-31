#!/usr/bin/env python3

from typing import Final


class Plant:
    name: Final[str]
    height: float
    days: int

    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self.height = height
        self.days = days

    def __str__(self) -> str:
        return f"{self.name}: {round(self.height, 1)}cm, {self.days} days old"

    def show(self) -> None:
        print(self)

    def grow(self) -> None:
        self.days += 1

    def age(self, growth: float) -> None:
        self.height += growth
        self.grow()
        self.show()


def main() -> None:
    rose = Plant("Rose", 25, 30)
    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        rose.age(0.8)
    print(f"Growth this week: {round(0.8 * 7, 1)}cm")


if __name__ == "__main__":
    main()
