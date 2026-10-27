# @classmethod in Python

> Source: https://www.geeksforgeeks.org/python/classmethod-in-python/
> Collected: 2026-10-27
> Published: 2026-06-08

@classmethod is used to create a method that works with the class instead of an object instance. A class method receives the class itself as the first argument using cls. It is commonly used to access class variables, create factory methods and perform operations related to the class.

Example: In this example, a class method is used to access a class variable without creating an object.

Python

```
class Student:
    course = "Python"

    @classmethod
    def show_course(cls):
        print(cls.course)

Student.show_course()
```

Output

```
Python
```

Explanation: @classmethod converts show_course() into a class method, and cls.course accesses the class variable course.

## Syntax

> class ClassName:
>     @classmethod
>     def method_name(cls, args):
>         # method body

Parameters:

- cls: Refers to the class itself.

- args (optional): Additional arguments passed to the method.

Return Value: Returns a class method object.

## Examples

Example 1: In this example, the class method accesses and prints a class variable shared by all objects.

Python

```
class Car:
    brand = "Toyota"

    @classmethod
    def show_brand(cls):
        print(cls.brand)

Car.show_brand()
```

Output

```
Toyota
```

Explanation: cls.brand accesses the class variable brand directly using the class method.

Example 2: In this example, a class method creates an object using a formatted string.

Python

```
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        n, a = data.split("-")
        return cls(n, int(a))

u = User.from_string("Alex-21")

print(u.name)
print(u.age)
```

Output

```
Alex
21
```

Explanation: from_string() uses cls() to create and return a new object from the string data.

Example 3: In this example, classmethod() function is used directly instead of the @classmethod decorator.

Python

```
class Demo:
    name = "GeeksforGeeks"

    def show(cls):
        print(cls.name)

Demo.show = classmethod(Demo.show)
Demo.show()
```

Output

```
GeeksforGeeks
```

Explanation: classmethod(Demo.show) converts the normal method show() into a class method.
