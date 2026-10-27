# Supercharge Your Classes With Python super()

> Source: https://realpython.com/python-super/
> Collected: 2026-10-27
> Published: 2019-02-12

While Python isn't purely an object-oriented language, it supports inheritance, which it does with super().

In this tutorial, you'll learn about: the concept of inheritance in Python; multiple inheritance; how the super() function works; how super() works in single inheritance; how super() works in multiple inheritance.

## An Overview of Python's super() Function

super() gives you access to methods in a superclass from the subclass that inherits from it. super() alone returns a temporary object of the superclass that allows you to call that superclass's methods. A common use case is building classes that extend the functionality of previously built classes.

## super() in Single Inheritance

Inheritance: a class derives (inherits) attributes and behaviors from another class. Example Rectangle and Square:

Python

```
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
```

square = Square(4); square.area() -> 16. rectangle = Rectangle(2,4); rectangle.area() -> 8.

Cube extends Square: surface_area = super().area() * 6; volume = super().area() * self.length. cube = Cube(3); cube.surface_area() -> 54; cube.volume() -> 27.

## A super() Deep Dive

super() can take two parameters: subclass and an instance of that subclass. super(Square, self) is equivalent to parameterless super() in Python 3. You can change the starting level: super(Square, self).area() starts searching above Square. The second parameter provides a bound method (object context).

## super() in Multiple Inheritance

Multiple inheritance: a subclass inherits from multiple superclasses (sibling classes).

Example RightPyramid(Triangle, Square). MRO: RightPyramid.__mro__ -> RightPyramid, Triangle, Square, Rectangle, object.

Method Resolution Order determines where Python looks for methods. RightPyramid.__mro__ initially: RightPyramid, Triangle, Square, Rectangle, object. Changing to RightPyramid(Square, Triangle) gives: RightPyramid, Square, Rectangle, Triangle, object. pyramid.area() -> 20.0.

Cooperative design: rename Triangle.area() to tri_area(); add super().__init__() calls; use **kwargs to pass arguments through the MRO. Complete example with Rectangle, Square, Cube, Triangle, RightPyramid using **kwargs. pyramid = RightPyramid(base=2, slant_height=4); pyramid.area() -> 20.0; pyramid.area_2() -> 20.0.

Multiple Inheritance Alternatives: composition; mixins. VolumeMixin provides volume = area() * height. Cube(VolumeMixin, Square): cube = Cube(2); cube.surface_area() -> 24; cube.volume() -> 8.
