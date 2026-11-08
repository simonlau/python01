#!/usr/bin/env python3
# pyrefly: ignore-errors[missing-override-decorator]

from typing import Final


class Plant:
    _name: Final[str]
    _height: float
    _days: int

    def __init__(self, name: str, height: float, days: int):
        self._name = name
        self._height = height
        self._days = days

    def __str__(self) -> str:
        height = round(self._height, 1)
        return f"{self._name}: {height}cm, {self._days} days old"

    def show(self) -> None:
        print(self)

    def grow(self) -> None:
        self._days += 1

    def age(self, growth: float) -> None:
        self._height += growth
        self.grow()

    def set_height(self, height: float) -> None:
        if height > 0:
            self._height = height
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, days: int) -> None:
        if days > 0:
            self._days = days
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days


class Flower(Plant):
    _color: Final[str]
    _bloom: bool

    def __init__(self, name: str, height: float, days: int, color: str):
        super().__init__(name, height, days)
        self._color = color
        self._bloom = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloom:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def bloom(self) -> None:
        self._bloom = True


class Tree(Plant):
    _trunk_diameter: Final[float]

    def __init__(
        self, name: str, height: float, days: int, trunk_diameter: float
    ):
        super().__init__(name, height, days)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self, long: float, wide: float) -> None:
        msg = f"Tree {self._name} now producing a shade "
        size = f"of {long}cm long and {wide}cm wide"
        print(msg + size)

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    _harvest_season: Final[str]
    _nutritional_value: int

    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        harvest_season: str,
        nutritional_value: int,
    ):
        super().__init__(name, height, days)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest Season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()

    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    tree.produce_shade(200.0, 5.0)

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()
    for _ in range(20):
        tomato.age(2.1)
    tomato.show()


if __name__ == "__main__":
    main()
