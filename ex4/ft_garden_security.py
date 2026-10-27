#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, days: int):
        self._name = name
        self._height = height
        self._days = days

    def __str__(self):
        return f"{self._name}: {round(self._height, 1)}cm, {self._days} days old"

    def show(self):
        print(self)

    def grow(self):
        self._days += 1

    def age(self, growth: float):
        self._height += growth
        self.grow()
        self.show()

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

    def get_height(self):
        return self._height

    def get_age(self):
        return self._days


def main() -> None:
    rose = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("Plant created: ", end='')
    rose.show()

    rose.set_height(25.0)
    rose.set_age(30)

    rose.set_height(-42)
    rose.set_age(-1)

    print("Current state: ", end='')
    rose.show()


if __name__ == '__main__':
    main()
