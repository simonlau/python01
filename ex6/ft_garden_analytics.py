#!/usr/bin/env python3
# pyrefly: ignore-errors[missing-override-decorator]

from typing import Final


class Plant:
    class Stats:
        _num_grow: int
        _num_age: int
        _num_show: int

        def __init__(self):
            self._num_grow = 0
            self._num_age = 0
            self._num_show = 0

        def __str__(self):
            return f"Stats: {self._num_grow} grow {self._num_age} age, {self._num_show} show"

        def add_grow(self):
            self._num_grow += 1

        def add_age(self):
            self._num_age += 1

        def add_show(self):
            self._num_show += 1

    _name: Final[str]
    _height: float
    _days: int

    def __init__(self, name: str, height: float, days: int):
        self._name = name
        self._height = height
        self._days = days
        self._stats = Plant.Stats()

    def __str__(self):
        return f"{self._name}: {round(self._height, 1)}cm, {self._days} days old"

    @staticmethod
    def is_year_old(days: int):
        return days > 365

    @classmethod
    def create(cls):
        return cls("Unknown plant", 0.0, 0)

    def get_stats_str(self):
        return self._stats.__str__()

    def show(self):
        self._stats.add_show()
        print(self)

    def grow(self):
        self._stats.add_grow()
        self._days += 1

    def age(self, growth: float):
        self._stats.add_age()
        self._height += growth
        self.grow()

    def set_height(self, height: float):
        if (height > 0):
            self._height = height
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, days: int):
        if (days > 0):
            self._days = days
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_name(self):
        return self._name

    def get_height(self):
        return self._height

    def get_age(self):
        return self._days


class Flower(Plant):
    _color: Final[str]
    _bloom: bool

    def __init__(self, name: str, height: float, days: int, color: str):
        super().__init__(name, height, days)
        self._color = color
        self._bloom = False

    def show(self):
        super().show()
        print(f"Color: {self._color}")
        if self._bloom:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def bloom(self):
        self._bloom = True


class Seed(Flower):
    _seeds: int

    def __init__(self, name: str, height: float, days: int, color: str):
        super().__init__(name, height, days, color)
        self._seeds = 0

    def bloom(self):
        super().bloom()
        self._seeds += 42

    def show(self):
        super().show()
        print(f"Seeds: {self._seeds}")


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._num_shade = 0

        def __str__(self):
            parent = super().__str__()
            return f"{parent}\n{self._num_shade} shade"

        def add_shade(self):
            self._num_shade += 1

    _trunk_diameter: Final[float]

    def __init__(self, name: str, height: float, days: int, trunk_diameter: float):
        super().__init__(name, height, days)
        self._trunk_diameter = trunk_diameter
        self._stats = Tree.TreeStats()

    def produce_shade(self, long: float, wide: float):
        # assert isinstance(self._stats, Tree.TreeStats)
        self._stats.add_shade()  # pyrefly: ignore[missing-attribute]
        print(
            f"Tree {self._name} now producing a shade of {long}cm long and {wide}cm wide")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

    def get_stats_str(self):
        return self._stats.__str__()


class Vegetable(Plant):
    _harvest_season: Final[str]
    _nutritional_value: int

    def __init__(self, name: str, height: float, days: int, harvest_season: str, nutritional_value: int):
        super().__init__(name, height, days)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f"Harvest Season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def grow(self):
        super().grow()
        self._nutritional_value += 1


def show_stats(plant: Plant):
    print(f"[statistics for {plant.get_name()}]")
    print(plant.get_stats_str())


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"is 30 days more than a year? -> {Plant.is_year_old(30)}")
    print(f"is 400 days more than a year? -> {Plant.is_year_old(400)}")
    print("\n")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    show_stats(rose)
    rose.grow()
    rose.bloom()
    rose.show()
    print("\n")
    show_stats(rose)
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    show_stats(tree)
    tree.produce_shade(200.0, 5.0)
    show_stats(tree)
    print("\n")
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    show_stats(sunflower)
    sunflower.age(30.0)
    sunflower.bloom()
    sunflower.show()
    show_stats(sunflower)
    print("\n")
    print("=== Anonymous")
    unknown = Plant.create()
    unknown.show()
    show_stats(unknown)


if __name__ == '__main__':
    main()
