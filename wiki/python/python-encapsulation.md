# Encapsulation in Python

> Sources: William Imoh (roadmap.sh), Unknown
> Raw: [encapsulation-in-python.md](../../raw/python/encapsulation-in-python.md)
> Updated: 2026-10-28

## Overview

Encapsulation is the practice of hiding a class's internal details and exposing only what is necessary, separating the public interface from the implementation. In Python this is achieved through naming conventions (underscore prefixes) and name mangling rather than strict access modifiers. Public, protected, and private attributes control intended visibility, while getter/setter methods and the `@property` decorator provide controlled access with validation. Encapsulation improves security, data protection, and maintainability, and is useful in scenarios such as financial transactions, game state, and API configuration.

## What Is Encapsulation?

Encapsulation groups data members (attributes/variables) and the methods that operate on them into a single unit (a class), then restricts direct access to the object's internal state. The goal is to prevent accidental modification and to let you choose what other code can see or change. Python does not enforce access levels like Java or C++; instead it relies on conventions (`_` and `__` prefixes) to signal intent. Closures achieve a similar hiding of state without a class.

```python
class BankAccount:  # Class with encapsulation
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def get_balance(self):  # Public method
        return self.__balance

account = BankAccount(8000)
print(account.get_balance())  # Access through method
# print(account.__balance)    # Cannot be accessed directly
```

## Access Levels and Naming Conventions

Attributes and methods are categorized as public, protected, or private:

- **Public members**: accessible from anywhere; no leading underscore. All members are public by default.
- **Protected members**: intended for internal use within the class and its subclasses; single leading underscore (`_name`). Python does not block access, but the underscore warns other developers.
- **Private members**: intended for use only within the class itself; double leading underscore (`__name`) triggers name mangling.

```python
class Person:
    def __init__(self):
        self.name = "Cess"           # Public
        self._age = 26               # Protected (single _)
        self.__ssn = "012-34-5678"  # Private (double __)
```

Name mangling rewrites `__name` to `_ClassName__name` (e.g., `__password` becomes `_SecureVault__password`), making direct access harder but not impossible. Accessing mangled names directly is considered bad practice because it breaks encapsulation.

## Implementing Encapsulation

### Public Attributes and Methods

Public attributes store data that external code may read or modify directly. Because there is no restriction, changes can bypass validation.

```python
class Person:
    def __init__(self, field, age):
        self.field = field
        self.age = age

    def increase_age(self, increment):
        """Increases age by the given increment."""
        self.age += increment
        return f"New age: {self.age}"

person1 = Person("Data science", 27)
print(person1.field)          # Data science
person1.age = 30              # Direct modification allowed
```

Use public attributes when external code needs direct read/write access without validation.

### Protected Attributes (Single Underscore)

Protected attributes support internal use within the class and subclasses. They remain accessible from outside, but should not be used there.

```python
class Employee:
    def __init__(self, name, years_of_service):
        self.name = name
        self._years_of_service = years_of_service

    def _calculate_bonus(self):
        return self._years_of_service * 0.1

emp = Employee("Cess", 5)
print(emp._years_of_service)   # 5 (accessible, but warned)
print(emp._calculate_bonus())  # 0.5
```

Subclasses typically initialize protected state by calling `super().__init__()`.

### Private Attributes (Double Underscore)

Private attributes store internal/sensitive data such as passwords or keys. They are accessed only through public methods.

```python
class SecureVault:
    def __init__(self, password):
        self.__password = password

    def verify_password(self, attempt):
        return self.__password == attempt

    def __internal_security_check(self):
        print("Running internal security check...")
        return True

vault = SecureVault(6666)
print(vault.verify_password(6666))  # True
# print(vault.__password)           # AttributeError
# print(vault._SecureVault__password)  # Works, but discouraged
```

### Getter and Setter Methods

Getters (accessors) retrieve attribute values; setters (mutators) modify them with validation. Python's `@property` decorator lets you treat a method like an attribute, adding logic behind the scenes without changing call syntax.

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):          # Getter
        return self._age

    @age.setter
    def age(self, value):   # Setter
        if value > 0:
            self._age = value

person = Person(27)
print(person.age)   # 27
person.age = 50
print(person.age)   # 50
```

## Practical Use Cases

- **Financial calculations/transactions**: keep `__balance` and `__transaction_history` private; expose `deposit()`, `withdraw()`, and a `balance` property with validation.
- **Game object state**: protect `__health`/`__max_health`; expose `take_damage()` and `heal()` to prevent cheating.
- **API configuration objects**: keep `__api_key` private and `_base_url`/`_timeout` protected; expose `make_request()`.

## Common Mistakes to Avoid

- **Overusing private attributes**: don't make simple data private when no protection/validation is needed.
- **Accessing mangled names directly**: bypasses encapsulation and breaks if internals change.
- **Creating getters/setters for everything**: Python favors direct attribute access; use `@property` only when validation or computed values are needed.
- **Mixing internal and external state**: keep internal helpers private so the public interface stays focused and testable.

## Best Practices

- Use the `@property` decorator instead of separate getter/setter methods.
- Follow clear naming conventions (`_` protected, `__` private).
- Document intended access with docstrings, especially for protected/private members.

## See Also

- [Python Classes: The Power of Object-Oriented Programming](python-classes.md)
- [Code Cultivation — Object-Oriented Garden Systems](code-cultivation.md)
- [Supercharge Your Classes With Python super()](python-super.md)