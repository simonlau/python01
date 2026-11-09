#!/usr/bin/env python3
# pyrefly: ignore-errors[missing-override-decorator]

from typing import Final, cast


class Plant:
    # ruff: ignore[undocumented-public-nested-class]
    class Stats:
        _num_grow: int
        _num_age: int
        _num_show: int

        def __init__(self) -> None:
            self._num_grow = 0
            self._num_age = 0
            self._num_show = 0

        def __str__(self) -> str:
            header = "Stats: "
            grow = f"{self._num_grow} grow, "
            age = f"{self._num_age} age, "
            show = f"{self._num_show} show"
            return header + grow + age + show

        def add_grow(self) -> None:
            self._num_grow += 1

        def add_age(self) -> None:
            self._num_age += 1

        def add_show(self) -> None:
            self._num_show += 1

    _name: Final[str]
    _height: float
    _days: int

    def __init__(self, name: str, height: float, days: int):
        self._name = name
        self._height = height
        self._days = days
        self._stats = Plant.Stats()

    def __str__(self) -> str:
        return f"{self._name}: {self._height:.1f}cm, {self._days} days old"

    @staticmethod
    def is_year_old(days: int) -> bool:
        one_year = 365
        return days > one_year

    @classmethod
    def create(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def get_stats_str(self) -> str:
        return str(self._stats)

    def show(self) -> None:
        self._stats.add_show()
        print(self)

    def grow(self) -> None:
        self._stats.add_grow()
        self._days += 1

    def age(self, growth: float) -> None:
        self._stats.add_age()
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

    def get_name(self) -> str:
        return self._name

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


class Seed(Flower):
    _seeds: int

    def __init__(self, name: str, height: float, days: int, color: str):
        super().__init__(name, height, days, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds += 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


class Tree(Plant):
    # ruff: ignore[undocumented-public-nested-class]
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._num_shade = 0

        def __str__(self) -> str:
            parent = super().__str__()
            return f"{parent}\n{self._num_shade} shade"

        def add_shade(self) -> None:
            self._num_shade += 1

    _trunk_diameter: Final[float]

    def __init__(
        self, name: str, height: float, days: int, trunk_diameter: float
    ):
        super().__init__(name, height, days)
        self._trunk_diameter = trunk_diameter
        self._stats = Tree.TreeStats()

    def produce_shade(self, long: float, wide: float) -> None:
        stats = cast("Tree.TreeStats", self._stats)
        stats.add_shade()
        msg = f"Tree {self._name} now producing a shade "
        size = f"of {long}cm long and {wide}cm wide"
        print(msg + size)

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

    def get_stats_str(self) -> str:
        return str(self._stats)


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


def show_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    print(plant.get_stats_str())


def flower_demo() -> None:
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    show_stats(rose)
    rose.grow()
    rose.bloom()
    rose.show()
    print(" ")
    show_stats(rose)


def tree_demo() -> None:
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    show_stats(tree)
    tree.produce_shade(200.0, 5.0)
    show_stats(tree)
    print(" ")


def seed_demo() -> None:
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    show_stats(sunflower)
    sunflower.age(30.0)
    sunflower.bloom()
    sunflower.show()
    show_stats(sunflower)
    print(" ")


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"is 30 days more than a year? -> {Plant.is_year_old(30)}")
    print(f"is 400 days more than a year? -> {Plant.is_year_old(400)}")
    print("\n")

    flower_demo()
    tree_demo()
    seed_demo()

    print("=== Anonymous")
    unknown = Plant.create()
    unknown.show()
    show_stats(unknown)


if __name__ == "__main__":
    main()
