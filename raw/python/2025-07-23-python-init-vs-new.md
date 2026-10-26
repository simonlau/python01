# Python __init__ vs __new__

> Source: https://www.geeksforgeeks.org/python/python-init-vs-new/
> Collected: 2026-10-26
> Published: 2025-07-23

In Python, __init__ and __new__ are part of a group of special methods (dunder/magic methods).

## Python __new__

__new__ is responsible for actually creating a new instance of a class. It is called automatically before __init__. It gets called first when a new object is being created.

Example:

Python

```
class CustomObject:
    def __new__(cls, value):
        instance = super().__new__(cls)
        instance.value = value
        return instance

obj1 = CustomObject(10)
obj2 = CustomObject(20)

print(obj1.value)
print(obj2.value)
```

Output

```
10
20
```

Explanation:

- instance = super().__new__(cls): Calls the parent class's __new__ to create an instance.

- instance.value = value: Adds a custom attribute during creation.

- return instance: Returns the newly created instance; object creation fails if not returned.

## Python __init__

__init__ is the initializer/constructor. It is called automatically when a new instance of a class is created. Its primary purpose is to initialize the object's attributes (set up its state) after the object has been created.

Example:

Python

```
class SimpleObject:
    def __init__(self, value):
        self.value = value

obj1 = SimpleObject(10)
obj2 = SimpleObject(20)

print(obj1.value)
print(obj2.value)
```

Output

```
10
20
```

## Demonstration of __new__ and __init__ in Instance Creation

Python

```
class MyClass:
    def __new__(cls, *args, **kwargs):
        print("GeeksforGeeks")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print(f"{value}")
        self.value = value

obj = MyClass(10)
```

Output

```
GeeksforGeeks
10
```

Explanation: __new__ is responsible for creating the instance and is called before __init__. After the instance is created by __new__, __init__ is called to initialize the object's attributes.

## Major Differences between __new__ and __init__

| Aspect | __new__ | __init__ |
| --- | --- | --- |
| Purpose | Responsible for creating a new instance of a class. Called first when a new object is being created. | Responsible for initializing the instance after it has been created. Sets the initial state of the object. |
| When They Are Called | Called before __init__. Used to control the creation of the object. | Called after __new__ and used to initialize the newly created object. |
| Return Value | Must return the newly created instance (object), which is then passed to __init__. | Does not return anything. Only initializes the object after it's created. |
| Common Usage | Typically rarely overridden. Most commonly used when dealing with immutable objects. | Frequently overridden to initialize attributes of an object. Used in most classes. |
| Inheritance Behavior | Called by the class itself or its metaclass. Must return an instance of the class. | Called on the instance of the object. |
