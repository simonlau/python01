# Code Cultivation — Object-Oriented Garden Systems

> Sources: Unknown, Unknown
> Raw: [code-cultivation-object-oriented-garden-systems.md](../../raw/python/code-cultivation-object-oriented-garden-systems.md)
> Updated: 2026-10-25

## Overview

A Python programming project (version 3.2) that builds a comprehensive digital garden ecosystem while teaching advanced Python concepts. The module starts from basic program structure and progresses to object-oriented programming, with each exercise reusing and extending a shared `Plant` class. Code must run on Python 3.10+, pass flake8, use type hints checked by mypy, and follow PascalCase for classes and snake_case for functions and variables. Each exercise lives in its own file and directory.

## Project Setup

- Python version: 3.10 or later.
- Linter: flake8.
- Type checking: mypy (all functions and methods need type hints).
- Naming: classes in PascalCase, functions and variables in snake_case.
- Input validation is not required unless explicitly stated.
- Testing may use `if __name__ == "__main__":` blocks; this pattern is permitted throughout the project.

## Exercise 0: Planting Your First Seed

- File: `ex0/ft_garden_intro.py`. Authorized: `print()`.
- Create a program that runs via `python3 ft_garden_intro.py` using the `if __name__ == "__main__":` pattern.
- Store plant information in simple variables: name, height, and age; display with `print()`.
- Example output: `=== Welcome to My Garden ===`, `Plant: Rose`, `Height: 25cm`, `Age: 30 days`, `=== End of Program ===`.
- The evaluation may ask the student to explain why `if __name__ == "__main__":` matters (imports) and to add a shebang line.

## Exercise 1: Garden Data Organizer

- File: `ex1/ft_garden_data.py`. Authorized: `print()`.
- Create a `Plant` class modeling any plant with attributes name, height, and age.
- Instantiate at least 3 plants and set their attributes; add a `show()` method to display info.
- Example output: `Rose: 25cm, 30 days old`, `Sunflower: 80cm, 45 days old`, `Cactus: 15cm, 120 days old`.

## Exercise 2: Plant Growth Simulator

- File: `ex2/ft_plant_growth.py`. Authorized: `print()`, `range()`, `round()`.
- Reuse the `Plant` class; add `grow()` and `age()` methods that change plant state.
- Simulate a week of growth, then display final height and total week increase.
- Example: Rose starts at `25.0cm, 30 days old`; Day 1 `25.8cm, 31 days old`; ... Day 7 `30.6cm, 37 days old`; growth this week `5.6cm`.

## Exercise 3: Plant Factory

- File: `ex3/ft_plant_factory.py`. Authorized: `print()`, `range()`, `round()`.
- Streamline creation: instantiate and initialize a plant in one step via `__init__`, so it is ready to use immediately.
- Create at least 5 plants with varying characteristics (e.g., Rose 25.0cm/30 days, Oak 200.0cm/365 days, Cactus 5.0cm/90 days, Sunflower 80.0cm/45 days, Fern 15.0cm/120 days).
- Display all created plants using the unchanged `show()` method.

## Exercise 4: Garden Security System

- File: `ex4/ft_garden_security.py`. Authorized: `print()`, `range()`, `round()`.
- Protect data via encapsulation using the protected convention (single underscore, not name mangling).
- Provide `set_height()`, `set_age()`, `get_height()`, `get_age()`.
- Validate that height and age cannot be negative; print an error message and leave data unchanged (or use defaults) on invalid input.
- Example: `Plant created: Rose: 15.0cm, 10 days old`; `Height updated: 25cm`; `Age updated: 30 days`; `Rose: Error, height can't be negative` → `Height update rejected`; `Rose: Error, age can't be negative` → `Age update rejected`; final state `Rose: 25.0cm, 30 days old`.

## Exercise 5: Specialized Plant Types

- File: `ex5/ft_plant_types.py`. Authorized: `super()`, `print()`, `range()`, `round()`.
- Inherit from `Plant` to create `Flower`, `Tree`, and `Vegetable`, avoiding duplicated common code.
- `Flower`: `color` attribute and `bloom()` method.
- `Tree`: `trunk_diameter` attribute and `produce_shade()` method.
- `Vegetable`: `harvest_season` and `nutritional_value` attributes; nutritional value starts at 0 and increases when `age()` and `grow()` are called.
- `show()` override prints standard `Plant` output plus extra characteristics, reusing parent code via `super()`.
- Create at least one instance of each type; make the flower bloom.

## Exercise 6: Garden Analytics

- File: `ex6/ft_garden_analytics.py`. Authorized: `super()`, `print()`, `range()`, `round()`, `staticmethod()`, `classmethod()`.
- Add a static method to `Plant` checking whether a given age (in days) is older than a year.
- Add a class method to create an "anonymous" plant when not all information is available.
- Create `Seed`, inheriting from `Flower`, holding a seed count after blooming; update `show()` accordingly.
- Implement an internal (nested) `PlantStats` class holding counts of `grow()`, `age()`, and `show()` calls; encapsulated, with a display function. `Tree` adds a `produce_shade()` call count.
- Provide a standalone (non-class) function that displays statistics for any plant.
- Example stats output: `Stats: 0 grow, 0 age, 1 show` (and `1 shade` for trees after producing shade).

## See Also

- None yet.
