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
    rose = Plant("Rose", 25, 30)
    print("=== Garden Plant Growth ===")
    rose.show()

    num_days = 7
    growth = 0.8
    for i in range(num_days):
        print(f"=== Day {i + 1} ===")
        rose.age(growth)
        rose.show()
    print(f"Growth this week: {growth * num_days:.1f}cm")


if __name__ == "__main__":
    main()
