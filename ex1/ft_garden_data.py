#!/usr/bin/env python3

from dataclasses import dataclass


@dataclass(slots=True)
class Plant:
    name: str
    height: float
    days: int

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
