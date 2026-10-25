# Python's F-String for String Interpolation and Formatting

> Source: https://realpython.com/python-f-strings/
> Collected: 2026-10-25
> Published: 2026-10-23

[ ![Real Python](/static/real-python-logo.893c30edea53.svg)](/)

- [Start Here](/start-here/)

- [ Learn Python](#)

  ###### Start Learning

  [Your Learning Plan →Your personalized Python learning plan](/account/learning-plan/) [Python Tutorials →In-depth articles and video courses](/search?kind=article&kind=course&order=newest&_from=nav_library) [Learning Paths →Guided study plans for accelerated learning](/learning-paths/)

  ###### Practice

  [Quizzes & Exercises →Check your learning progress](/search?kind=exercise&kind=quiz&_from=nav_library) [Browse Topics →Focus on a specific area or skill level](/tutorials/all/) [Reference →Concise definitions for common Python terms](/ref/)

  ###### Get Help

  [Mentor AI →NewYour personal Python mentor](/mentor/) [Office Hours →Live Q&A calls with Python experts](/office-hours/) [Community Chat →Learn with other Pythonistas](/community/)

  ###### Go Deeper

  [Live Courses →Live, instructor-led Python courses](/live/) [Books →Round out your knowledge and learn offline](/products/books/) [Podcast →Hear what’s new in the world of Python](/podcasts/rpp/)

  [Unlock All Content and Become a Python Expert →Get unlimited access to all Real Python has to offer](/account/join/?from=navbar_learn)

  [Unlock All Content →Become a Python Expert](/account/join/?from=navbar_learn)

- [ More](#)

  [Learner Stories](/learner-stories/) [Python Newsletter](/newsletter/) [Python Job Board](https://www.pythonjobshq.com) [Meet the Team](/team/) [Become a Contributor](/jobs/)

- [ Search](/search "Search")

- [Join](/account/join/)

- [Sign‑In](/account/login/?intent=navbar&next=%2Fpython-f-strings%2F)

— FREE Email Series —

🐍 Python Tricks 💌

![Dictionary merging in Python 3.5+](https://files.realpython.com/media/pytrick-dict-merge.4201a0125a5e.png)

Get Python Tricks »

🔒 No spam. Unsubscribe any time.

[Browse Topics](/tutorials/all/) [Guided Learning Paths](/learning-paths/)  
[ Basics](/search?level=basics&_from=sidebar_level) [ Intermediate](/search?level=intermediate&_from=sidebar_level) [ Advanced](/search?level=advanced&_from=sidebar_level)

---

[ai](/tutorials/ai/) [algorithms](/tutorials/algorithms/) [api](/tutorials/api/) [best-practices](/tutorials/best-practices/) [career](/tutorials/career/) [community](/tutorials/community/) [databases](/tutorials/databases/) [data-science](/tutorials/data-science/) [data-structures](/tutorials/data-structures/) [data-viz](/tutorials/data-viz/) [devops](/tutorials/devops/) [django](/tutorials/django/) [docker](/tutorials/docker/) [editors](/tutorials/editors/) [flask](/tutorials/flask/) [front-end](/tutorials/front-end/) [gamedev](/tutorials/gamedev/) [gui](/tutorials/gui/) [machine-learning](/tutorials/machine-learning/) [news](/tutorials/news/) [numpy](/tutorials/numpy/) [projects](/tutorials/projects/) [python](/tutorials/python/) [stdlib](/tutorials/stdlib/) [testing](/tutorials/testing/) [tools](/tutorials/tools/) [web-dev](/tutorials/web-dev/) [web-scraping](/tutorials/web-scraping/)

[Table of Contents](#toc)

- [Interpolating and Formatting Strings Before Python 3\.6](#interpolating-and-formatting-strings-before-python-36)

  - [The Modulo Operator (%)](#the-modulo-operator)

  - [The str.format() Method](#the-strformat-method)

- [Doing String Interpolation With F-Strings in Python](#doing-string-interpolation-with-f-strings-in-python)

  - [Interpolating Values and Objects in F-Strings](#interpolating-values-and-objects-in-f-strings)

  - [Embedding Expressions in F-Strings](#embedding-expressions-in-f-strings)

- [Formatting Strings With Python’s F-String](#formatting-strings-with-pythons-f-string)

- [Other Relevant Features of F-Strings](#other-relevant-features-of-f-strings)

  - [Using an Object’s String Representations in F-Strings](#using-an-objects-string-representations-in-f-strings)

  - [Self-Documenting Expressions for Debugging](#self-documenting-expressions-for-debugging)

  - [Comparing Performance: F-String vs Traditional Tools](#comparing-performance-f-string-vs-traditional-tools)

- [Upgrading F-Strings: Python 3\.12 and Beyond](#upgrading-f-strings-python-312-and-beyond)

  - [Using Quotation Marks](#using-quotation-marks)

  - [Using Backslashes](#using-backslashes)

  - [Writing Inline Comments](#writing-inline-comments)

  - [Deciphering F-String Error Messages](#deciphering-f-string-error-messages)

- [Using Traditional String Formatting Tools Over F-Strings](#using-traditional-string-formatting-tools-over-f-strings)

  - [Dictionary Interpolation](#dictionary-interpolation)

  - [Lazy Evaluation in Logging](#lazy-evaluation-in-logging)

  - [SQL Database Queries](#sql-database-queries)

  - [Internationalization and Localization](#internationalization-and-localization)

- [Converting Old String Into F-Strings Automatically](#converting-old-string-into-f-strings-automatically)

- [Frequently Asked Questions](#frequently-asked-questions)

Mark as Completed

[](/feedback/survey/article/python-f-strings/liked/?from=article-sidebar "Liked it") [](/feedback/survey/article/python-f-strings/disliked/?from=article-sidebar "Disliked it")

Share

Recommended Course

[](/courses/python-3-f-strings-improved-string-formatting-syntax/)

![F-Strings in Python 3.6](https://files.realpython.com/media/Python-f-Strings-Guide_Watermark.2c8be8b1d392.jpg)

Python 3's F-Strings: An Improved String Formatting Syntax

52m · 12 lessons

![Python's F-String: An Improved String Interpolation and Formatting Tool](https://files.realpython.com/media/UPDATE-f-strings_Watermarked.4d90960e7897.jpg)

# Python's F-String for String Interpolation and Formatting

by [Joanna Jablonski](#author) Updated Oct 23, 2026 Reading time estimate 36m [](#reader-comments) [basics](/tutorials/basics/) [python](/tutorials/python/)

Mark as Completed Share

Table of Contents

- [Interpolating and Formatting Strings Before Python 3\.6](#interpolating-and-formatting-strings-before-python-36)

  - [The Modulo Operator (%)](#the-modulo-operator)

  - [The str.format() Method](#the-strformat-method)

- [Doing String Interpolation With F-Strings in Python](#doing-string-interpolation-with-f-strings-in-python)

  - [Interpolating Values and Objects in F-Strings](#interpolating-values-and-objects-in-f-strings)

  - [Embedding Expressions in F-Strings](#embedding-expressions-in-f-strings)

- [Formatting Strings With Python’s F-String](#formatting-strings-with-pythons-f-string)

- [Other Relevant Features of F-Strings](#other-relevant-features-of-f-strings)

  - [Using an Object’s String Representations in F-Strings](#using-an-objects-string-representations-in-f-strings)

  - [Self-Documenting Expressions for Debugging](#self-documenting-expressions-for-debugging)

  - [Comparing Performance: F-String vs Traditional Tools](#comparing-performance-f-string-vs-traditional-tools)

- [Upgrading F-Strings: Python 3\.12 and Beyond](#upgrading-f-strings-python-312-and-beyond)

  - [Using Quotation Marks](#using-quotation-marks)

  - [Using Backslashes](#using-backslashes)

  - [Writing Inline Comments](#writing-inline-comments)

  - [Deciphering F-String Error Messages](#deciphering-f-string-error-messages)

- [Using Traditional String Formatting Tools Over F-Strings](#using-traditional-string-formatting-tools-over-f-strings)

  - [Dictionary Interpolation](#dictionary-interpolation)

  - [Lazy Evaluation in Logging](#lazy-evaluation-in-logging)

  - [SQL Database Queries](#sql-database-queries)

  - [Internationalization and Localization](#internationalization-and-localization)

- [Converting Old String Into F-Strings Automatically](#converting-old-string-into-f-strings-automatically)

- [Frequently Asked Questions](#frequently-asked-questions)

[Remove ads](/account/join/)

Recommended Course

[Python 3's F-Strings: An Improved String Formatting Syntax](/courses/python-3-f-strings-improved-string-formatting-syntax/) (52m)

Python **f-strings** offer a concise and efficient way to interpolate variables, [objects](/ref/glossary/object/), and [expressions](/ref/glossary/expression/) directly into strings. By prefixing a string with `f` or `F`, you can embed expressions within curly braces (`{}`), which are evaluated at [runtime](/ref/computer-science-glossary/runtime/).

This makes f-strings faster and more readable compared to older approaches like the [modulo (`%`)](https://realpython.com/python-modulo-string-formatting/) operator or the string [`.format()`](https://realpython.com/python-formatted-output/#using-the-format-method-for-string-interpolation) method. Additionally, f-strings support advanced [string formatting](/ref/glossary/string-formatting/) using Python’s string [format mini-language](https://realpython.com/python-format-mini-language/).

**By the end of this tutorial, you’ll understand that:**

- An f-string in Python is a [string literal](/ref/glossary/string-literal/) **prefixed with `f` or `F`**, allowing for the **embedding of expressions** within **curly braces `{}`**.

- To include dynamic content in an f-string, place your expression or [variable](/ref/glossary/variable/) inside the braces to **interpolate** its value into the string.

- An **f-string error** in Python often occurs due to syntax issues, such as **unmatched braces** or **invalid expressions** within the string.

- **Python 3\.12** improved f-strings by allowing **nested expressions** and the use of **backslashes**.

This tutorial will guide you through the features and advantages of f-strings, including interpolation and formatting. By familiarizing yourself with these features, you’ll be able to effectively use f-strings in your Python projects.

**Get Your Code:** [Click here to download the free sample code](https://realpython.com/bonus/python-f-string-code/) that shows you how to do string interpolation and formatting with Python’s f-strings.

 **Take the Quiz:** Test your knowledge with our interactive “Python's F-String for String Interpolation and Formatting” quiz. You’ll receive a score upon completion to help you track your learning progress:

---

[](/quizzes/f-strings/)

![F-Strings in Python 3.6](https://files.realpython.com/media/Python-f-Strings-Guide_Watermark.2c8be8b1d392.jpg)

**Interactive Quiz**

[Python's F-String for String Interpolation and Formatting](/quizzes/f-strings/)

Test your understanding of Python f-strings, including syntax, expression embedding, type conversions, and quoting rules.

**Python for Beginners Live Course:** Want to practice core skills like working with strings alongside an instructor? In Real Python’s [Python for Beginners](https://realpython.com/workshops/python-for-beginners/) live course, you build real programs in a small group, with live feedback when you get stuck. Join the waitlist to hear about the next dates.

## Interpolating and Formatting Strings Before Python 3\.6[](#interpolating-and-formatting-strings-before-python-36 "Permanent link")

Before Python 3\.6, you had two main tools for interpolating values, variables, and expressions inside string literals:

1. The [string interpolation operator](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting) (`%`), or modulo operator

2. The [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format) method

You’ll get a refresher on these two string interpolation tools in the following sections. You’ll also learn about the string formatting capabilities that these tools offer in Python.

[ Remove ads](/account/join/)

### The Modulo Operator (`%`)[](#the-modulo-operator "Permanent link")

The modulo operator (`%`) was the first tool for string interpolation and formatting in Python and has been in the language since the beginning. Here’s what using this operator looks like in practice:

Language: Python

```
>>> name = "Jane"

>>> "Hello, %s!" % name
'Hello, Jane!'
```

In this quick example, you use the `%` operator to interpolate the value of your `name` variable into a string literal. The interpolation operator takes two operands:

- A string literal containing one or more conversion specifiers

- The object or objects that you’re interpolating into the string literal

The **conversion specifiers** work as replacement fields. In the above example, you use the `%s` combination of characters as a conversion specifier. The `%` symbol marks the start of the specifier, while the `s` letter is the **conversion type** and tells the operator that you want to convert the input object into a string.

If you want to insert more than one object into your target string, then you can use a [tuple](https://realpython.com/python-tuple/). Note that the number of objects in the tuple must match the number of format specifiers in the string:

Language: Python

```
>>> name = "Jane"
>>> age = 25

>>> "Hello, %s! You're %s years old." % (name, age)
"Hello, Jane! You're 25 years old."
```

In this example, you use a tuple of values as the right-hand operand to `%`. Note that you’ve used a string and an integer. Because you use the `%s` specifier, Python converts both objects to strings.

You can also use dictionaries as the right-hand operand in your interpolation expressions. To do this, you need to create conversion specifiers that enclose key names in parentheses:

Language: Python

```
>>> "Hello, %(name)s! You're %(age)s years old." % {"name": "Jane", "age": 25}
"Hello, Jane! You're 25 years old."
```

This syntax provides a readable approach to string interpolation with the `%` operator. You can use descriptive key names instead of relying on the positional order of values.

When you use the `%` operator for string interpolation, you can use conversion specifiers. They provide some string formatting capabilities that take advantage of **conversion types**, **conversion flags**, and some characters like the period (`.`) and the asterisk (`*`). Consider the following example:

Language: Python

```
>>> "Balance: $%.2f" % 5425.9292
'Balance: $5425.93'

>>> print("Name: %s\nAge: %5s" % ("John", 35))
Name: John
Age:    35
```

In the first example, you use the `%.2f` conversion specifier to represent currency values. The `f` letter tells the operator to convert to a floating-point number. The `.2` part defines the precision to use when converting the input. In the second example, you use `%5s` to align the age value five positions to the right.

**Note:** Formatting with the modulo operator is inspired by [`printf()`](https://en.wikipedia.org/wiki/Printf) formatting used in [C](https://realpython.com/c-for-python-programmers/) and many other programming languages.

Even though the `%` operator provides a quick way to interpolate and format strings, it has a few issues that lead to common errors. For example, it’s difficult to interpolate tuples in your strings:

Language: Python

```
>>> "The personal info is: %s" % ("John", 35)
Traceback (most recent call last):
    ...
TypeError: not all arguments converted during string formatting
```

In this example, the operator fails to display the tuple of data because it interprets the tuple as two separate values. You can fix this issue by wrapping the data in a single-item tuple:

Language: Python

```
>>> "The personal info is: %s" % (("John", 35),)
"The personal info is: ('John', 35)"
```

This syntax fixes the issue, and now your string successfully shows the tuple of data. However, the syntax is hard to read, understand, and remember, isn’t it?

Another issue with the `%` operator is its limited formatting capabilities and the lack of support for Python’s [string formatting mini-language](https://docs.python.org/3/library/string.html#format-specification-mini-language), which provides a powerful tool to format your strings.

[ Remove ads](/account/join/)

### The `str.format()` Method[](#the-strformat-method "Permanent link")

The `str.format()` method is an improvement compared to the `%` operator because it fixes a couple of issues and supports the string formatting mini-language. With `.format()`, curly braces delimit the replacement fields:

Language: Python

```
>>> name = "Jane"
>>> age = 25

>>> "Hello, {}! You're {} years old.".format(name, age)
"Hello, Jane! You're 25 years old."
```

For the `.format()` method to work, you must provide replacement fields using curly brackets. If you use empty brackets, then the method interpolates its [arguments](/ref/glossary/argument/) into the target string based on position.

You can manually specify the interpolation order by referencing the position of each argument to `.format()` using zero-based indices. For example, the code below switches the arguments to `.format()` in the target string:

Language: Python

```
>>> "Hello, {1}! You're {0} years old.".format(age, name)
"Hello, Jane! You're 25 years old."
```

In this example, you use numeric indices to manually define the order in which you want to interpolate the values that you pass as arguments to `.format()`.

You can also use keyword arguments in the call to the method and enclose the argument names in your replacement fields:

Language: Python

```
>>> "Hello, {name}! You're {age} years old.".format(name="Jane", age=25)
"Hello, Jane! You're 25 years old."
```

This example showcases how `.format()` interpolates keyword arguments by their names into the target string. This construct considerably improves your code’s readability compared to the previous example and to the examples using the `%` operator.

Finally, the `.format()` method allows you to use dictionaries to provide the values that you want to interpolate into your strings:

Language: Python

```
>>> person = {"name": "Jane", "age": 25}

>>> "Hello, {name}! You're {age} years old.".format(**person)
"Hello, Jane! You're 25 years old."
```

In this example, you use a [dictionary](https://realpython.com/python-dicts/) containing the data to interpolate. Then, you use the [dictionary unpacking operator (`**`)](https://realpython.com/iterate-through-dictionary-python/#looping-over-merged-dictionaries-the-unpacking-operator) to provide the arguments to `.format()`.

The `.format()` method supports **format specifiers**. These are strings that you insert into replacement fields to format the values that you want to interpolate. Consider the following examples:

Language: Python

```
>>> "Balance: ${:.2f}".format(5425.9292)
'Balance: $5425.93'

>>> "{:=^30}".format("Centered string")
'=======Centered string========'
```

In the first example, you use the `:.2f` format specifier. This specifier tells `.format()` to *format* the input value as a floating-point number with a precision of two. This way, you can represent currency values.

In the second example, you use the `:=^30` format specifier. In this case, you’re telling `.format()` to format the input value using the `=` symbol as a filler character. The `^` symbol centers the input value by inserting `=` symbols on both sides to reach thirty characters.

Format specifiers provide a remarkable improvement over the limited formatting capabilities of the `%` operator. These specifiers have a straightforward syntax that makes up the string formatting mini-language. Thankfully, f-strings also support the string formatting mini-language, which is another cool feature of theirs. So, you won’t have to use `.format()` if you don’t need to.

In the upcoming sections, you’ll write a few more examples of formatting strings using the mini-language with f-strings.

## Doing String Interpolation With F-Strings in Python[](#doing-string-interpolation-with-f-strings-in-python "Permanent link")

F-strings joined the party in Python 3\.6 with [PEP 498](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498). Also called **formatted string literals**, f-strings are string literals that have an `f` before the opening quotation mark. They can include Python expressions enclosed in curly braces. Python will replace those expressions with their resulting values. So, this behavior turns f-strings into a string interpolation tool.

In the following sections, you’ll learn about f-strings and use them to interpolate values, objects, and expressions in your string literals.

[ Remove ads](/account/join/)

### Interpolating Values and Objects in F-Strings[](#interpolating-values-and-objects-in-f-strings "Permanent link")

F-strings make the string interpolation process intuitive, quick, and concise. The syntax is similar to what you used with `.format()`, but it’s less verbose. You only need to start your string literal with a lowercase or uppercase `f` and then embed your values, objects, or expressions in curly brackets at specific places:

Language: Python

```
>>> name = "Jane"
>>> age = 25

>>> f"Hello, {name}! You're {age} years old."
"Hello, Jane! You're 25 years old."
```

Look how readable and concise your string is now that you’re using the f-string syntax. You don’t need operators or methods anymore. You just embed the desired objects or expressions in your string literal using curly brackets.

It’s important to note that Python evaluates f-strings at runtime. So, in this example, both `name` and `age` are interpolated into the string literal when Python runs the line of code containing the f-string. Python can only interpolate these variables because you defined them *before* the f-string, which means that they must be in [scope](https://realpython.com/python-namespaces-scope/) when Python evaluates the f-string.

### Embedding Expressions in F-Strings[](#embedding-expressions-in-f-strings "Permanent link")

You can embed almost any Python expression in an f-string. This allows you to do some nifty things. You could do something pretty straightforward, like the following:

Language: Python

```
>>> f"{2 * 21}"
'42'
```

When Python runs this f-string, it multiplies `2` by `21` and immediately interpolates the resulting value into the final string.

The example above is quite basic. However, f-strings are more powerful than that. You could also use other Python expressions, including [function](https://realpython.com/defining-your-own-python-function/) and method calls, and even [comprehensions](https://realpython.com/list-comprehension-python/) or other more complex expressions:

Language: Python

```
>>> name = "Jane"
>>> age = 25

>>> f"Hello, {name.upper()}! You're {age} years old."
"Hello, JANE! You're 25 years old."

>>> f"{[2**n for n in range(3, 9)]}"
'[8, 16, 32, 64, 128, 256]'
```

In the first f-string, you embed a call to the `.upper()` string method in the first replacement field. Python runs the method call and inserts the uppercased name into the resulting string. In the second example, you create an f-string that embeds a [list comprehension](https://realpython.com/list-comprehension-python/). The comprehension creates a new list of powers of `2`.

## Formatting Strings With Python’s F-String[](#formatting-strings-with-pythons-f-string "Permanent link")

The expressions that you embed in an f-string are evaluated at runtime. Then, Python formats the result using the [`.__format__()`](https://docs.python.org/3/reference/datamodel.html#object.__format__) special method under the hood. This method supports the string formatting [protocol](https://realpython.com/python-classes/#special-methods-and-protocols). This protocol underpins both the `.format()` method, which you already saw, and the built-in [`format()`](https://docs.python.org/3/library/functions.html#format) function:

Language: Python

```
>>> format(5425.9292, ".2f")
'5425.93'
```

The `format()` function takes a value and a **format specifier** as arguments. Then, it applies the specifier to the value to return a formatted value. The format specifier must follow the rules of the string formatting mini-language.

Just like the `.format()` method, f-strings also support the string formatting mini-language. So, you can use format specifiers in your f-strings too:

Language: Python

```
>>> balance = 5425.9292

>>> f"Balance: ${balance:.2f}"
'Balance: $5425.93'

>>> heading = "Centered string"
>>> f"{heading:=^30}"
'=======Centered string========'
```

Note that the format specifiers in these examples are the same ones that you used in [the section on `.format()`](#the-strformat-method). In this case, the embedded expression comes before the format specifier, which always starts with a colon. This syntax makes the string literals readable and concise.

You can create a wide variety of format specifiers. Some common formats include currencies, dates, and the representation of numeric values. Consider the following examples of string formatting:

Language: Python

```
>>> integer = -1234567
>>> f"Comma as thousand separators: {integer:,}"
'Comma as thousand separators: -1,234,567'

>>> sep = "_"
>>> f"User's thousand separators: {integer:{sep}}"
"User's thousand separators: -1_234_567"

>>> floating_point = 1234567.9876
>>> f"Comma as thousand separators and two decimals: {floating_point:,.2f}"
'Comma as thousand separators and two decimals: 1,234,567.99'

>>> date = (9, 6, 2023)
>>> f"Date: {date[0]:02}-{date[1]:02}-{date[2]}"
'Date: 09-06-2023'

>>> from datetime import datetime
>>> date = datetime(2023, 9, 26)
>>> f"Date: {date:%m/%d/%Y}"
'Date: 09/26/2023'
```

These examples show how flexible the format specifiers can be. You can use them to create almost any string format. Note how in the second example, you’ve used curly brackets to embed variables or expressions in your format specifiers. This possibility allows you to create dynamic specifiers, which is pretty cool. In the last example, you format a [`datetime`](https://realpython.com/python-datetime/) which can be formatted with special [date format specifiers](https://strftime.org/).

[ Remove ads](/account/join/)

## Other Relevant Features of F-Strings[](#other-relevant-features-of-f-strings "Permanent link")

So far, you’ve learned that f-strings provide a quick and readable way to interpolate values, objects, and expressions into string literals. They also support the string formatting mini-language, so you can create format specifiers to format the objects that you want to insert into your strings.

In the following sections, you’ll learn about a few additional features of f-strings that may be relevant and useful in your day-to-day coding.

### Using an Object’s String Representations in F-Strings[](#using-an-objects-string-representations-in-f-strings "Permanent link")

Python’s f-strings support two flags with special meaning in the interpolation process. These flags are closely related to how Python manages the [string representation](https://realpython.com/python-repr-vs-str/#how-can-you-access-an-objects-string-representations) of objects. These flags are:

| Flag | Description |
| --- | --- |
| `!s` | Interpolates the string representation from the `.__str__()` method |
| `!r` | Interpolates the string representation from the `.__repr__()` method |

The `.__str__()` [special method](https://realpython.com/python-classes/#special-methods-and-protocols) generally provides a user-friendly string representation of an object, while the `.__repr__()` method returns a developer-friendly representation. To illustrate how these methods work under the hood, consider the following [class](/ref/glossary/class/):

Language: Python

```
# person.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"I'm {self.name}, and I'm {self.age} years old."

    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}', age={self.age})"
```

This class has two [instance attributes](https://realpython.com/python-classes/#instance-attributes), `.name` and `.age`. The `.__str__()` method returns a string that consists of an informative message for users of your class. This message should be useful for end users rather than developers.

**Note:** To dive deeper into the `__str__()` and `__repr__()` methods, check out [When Should You Use. `.__repr__()` vs `.__str__()` in Python?](https://realpython.com/python-repr-vs-str/)

In contrast, the `.__repr__()` method returns a string that’s a developer-friendly representation of the object. In short, the representation tells the developer how the current [instance](/ref/glossary/instance/) was created. Ideally, the developer should be able to copy this string representation and create an equivalent object.

How does this discussion about string representation affect f-strings? When you create your f-strings, you can choose which string representation to use with the `!r` and `!s` flags:

Language: Python

```
>>> from person import Person

>>> jane = Person("Jane Doe", 25)

>>> f"{jane!s}"
"I'm Jane Doe, and I'm 25 years old."

>>> f"{jane!r}"
"Person(name='Jane Doe', age=25)"
```

In the first f-string, you use the `!s` tag to interpolate the string representation that `.__str__()` returns. In the second f-string, you use the `!r` flag to interpolate the developer-friendly string representation of your current object.

These two flags are pretty relevant for you as a Python developer. Depending on your code’s intended audience, you can decide which one to use. In general, it should be the one that provides more value to your users.

It’s important to note that the `%` operator also supports equivalent conversion types, `s` and `r`, which work the same as the `!s` and `!r` flags in f-strings.

### Self-Documenting Expressions for Debugging[](#self-documenting-expressions-for-debugging "Permanent link")

F-strings have another cool feature that can be useful, especially during your [debugging](https://realpython.com/python-debugging-pdb/) process. The feature helps you self-document some of your expressions. For example, say that you’re dealing with a minor bug or issue in your code, and you want to know the value of a variable at a given moment in the code’s execution.

For this quick check, you can insert a call to [`print()`](https://realpython.com/python-print/) like the following:

Language: Python

```
>>> variable = "Some mysterious value"

>>> print(f"{variable = }")
variable = 'Some mysterious value'
```

You can use a variable name followed by an equal sign (`=`) in an f-string to create a [self-documented expression](https://docs.python.org/3/whatsnew/3.8.html#f-strings-support-for-self-documenting-expressions-and-debugging). When Python runs the f-string, it builds an expression-like string containing the variable’s name, the equal sign, and the variable’s current value. This f-string feature is useful for inserting quick debugging checks in your code.

Note that the whitespaces around the equal sign aren’t required but they are reflected in the output:

Language: Python

```
>>> print(f"{variable=}")
variable='Some mysterious value'

>>> print(f"{variable= }")
variable= 'Some mysterious value'

>>> print(f"{variable =}")
variable ='Some mysterious value'
```

Even though the whitespaces aren’t required, they can improve your code’s readability and the output’s format.

To see how these pieces fit together in a single replacement field, pick a value below and try the self-documenting option, a conversion, and a format specifier, or start from one of the presets:

Interactive diagram — enable JavaScript to view.

Notice that a conversion runs before the format specifier, so `!r` hands the specifier a string rather than the original object.

[ Remove ads](/account/join/)

### Comparing Performance: F-String vs Traditional Tools[](#comparing-performance-f-string-vs-traditional-tools "Permanent link")

F-strings are a bit faster than both the modulo operator (`%`) and the `.format()` method. That’s another cool characteristic. In the script below, you use the [`timeit`](https://realpython.com/python-timer/#python-timer-functions) module to measure the execution time that it takes to build a string using the modulo operator, the `.format()` method, and an f-string:

Language: Python

```
# performance.py

import timeit

name = "Linda Smith"
age = 40
strings = {
    "Modulo operator": "'Name: %s Age: %s' % (name, age)",
    ".format() method": "'Name: {} Age: {}'.format(name, age)",
    "f_string": "f'Name: {name} Age: {age}'",
}

def run_performance_test(strings):
    max_length = len(max(strings, key=len))
    for tool, string in strings.items():
        time = timeit.timeit(
            string,
            number=1000000,
            globals=globals()
        ) * 1000
        print(f"{tool}: {time:>{max_length - len(tool) + 6}.2f} ms")

run_performance_test(strings)
```

In this script, the `run_performance_test()` function takes care of measuring the execution time of the three different string interpolation tools. The `timeit.timeit()` function inside the [`for` loop](https://realpython.com/python-for-loop/) runs each interpolation tool a million times and returns the total execution time.

Then, the function prints the result to the screen. Note how your f-string in the call to `print()` takes advantage of format specifiers to conveniently format the code’s output.

If you [run the script](https://realpython.com/run-python-scripts/) from your command line, then you’ll get an output similar to the following. Of course, the numbers will be different for you:

Language: Shell

```
$ python performance.py
Modulo operator:   90.98 ms
.format() method: 144.69 ms
f_string:          87.08 ms
```

This output shows that f-strings are a bit faster than the `%` operator and the `.format()` method, which is the slowest tool because of all the required function calls. So, f-strings are readable, concise, and also fast.

## Upgrading F-Strings: Python 3\.12 and Beyond[](#upgrading-f-strings-python-312-and-beyond "Permanent link")

Now that you’ve learned why f-strings are great, you’re probably eager to get out there and start using them in your code. However, you need to know that f-strings up to Python [3\.11](https://realpython.com/python311-new-features/) have a few limitations regarding the expressions that you can embed in curly brackets and a few other details.

Fortunately, Python [3\.12](https://realpython.com/python312-f-strings/) lifted those limitations by removing the old f-string parser and providing a new implementation of f-strings based on the [PEG parser](https://realpython.com/python39-new-features/#a-more-powerful-python-parser) of Python [3\.9](https://realpython.com/python39-new-features/). In the following sections, you’ll learn about the limitations and how Python 3\.12 fixed them.

**Note:** Python 3\.14 went one step further and added **template strings**, or **t-strings**. They share the f-string syntax but produce a `Template` object instead of a string, which lets you process the interpolated values before you build the final text.

### Using Quotation Marks[](#using-quotation-marks "Permanent link")

Python supports several different types of quotation marks as delimiters in string [literals](https://en.wikipedia.org/wiki/Literal_\(computer_programming\)). You can use single (`'`) and double quotes (`"`). You can also use triple single (`'''`) and triple double quotes (`"""`). All these string delimiters work for f-strings as well. This feature allows you to insert quotation marks in f-strings. It also lets you introduce string literals in the embedded expressions and even create nested f-strings.

A typical use case of using different quotation marks in an f-string is when you need to use an apostrophe or access a dictionary key in an embedded expression:

Language: Python

```
>>> person = {"name": "Jane", "age": 25}

>>> f"Hello, {person['name']}! You're {person['age']} years old."
"Hello, Jane! You're 25 years old."
```

In this example, you have a dictionary with a person’s data. To define the f-string, you use double quotes. To access the dictionary key, you use single quotes. In the `"You're"` contraction, you use a single quote as an apostrophe.

So, where’s the quote-related limitation of f-strings up to Python 3\.11? The problem is that you can’t reuse quotation marks in an f-string:

Language: Python

```
>>> f"Hello, {person["name"]}!"
  File "<input>", line 1
    f"Hello, {person["name"]}!"
                      ^^^^
SyntaxError: f-string: unmatched '['
```

In this example, when you try to reuse double quotes to access the dictionary key, your f-string fails, and Python raises a [`SyntaxError`](https://realpython.com/invalid-syntax-python/) exception.

Fortunately, the new f-strings in Python 3\.12 solved this issue, allowing you to reuse quotes:

Language: Python

```
>>> # Python 3.12

>>> person = {"name": "Jane", "age": 25}
>>> f"Hello, {person["name"]}!"
'Hello, Jane!'
```

In this example, you reuse the double quotes in your embedded expressions, and the f-string works correctly. The limitation is gone. However, it may not be clear if reusing quotations in this example is cleaner than differentiating nested strings with different quotation marks.

There’s another f-string limitation that’s closely related to quotation marks. You can only nest as many f-strings as there are quote delimiters in Python:

Language: Python

```
>>> f"""{
...     f'''{
...         f"{f'{42}'}"
...     }'''
... }"""
'42'

>>> f"""{
...     f'''{
...         f"{f'{f"{42}"}'}"
...     }'''
... }"""
  File "<stdin>", line 1
    (f"{f'{f"{42}"}'}")
             ^
SyntaxError: f-string: f-string: unterminated string
```

The number of nesting levels in an f-string up to Python 3\.11 is limited by the available string delimiters, which are `"`, `'`, `"""`, and `'''`. So, you only have four delimiters that you can use to differentiate your levels of nesting.

In Python 3\.12, this limitation is removed because you can reuse quotation marks:

Language: Python

```
>>> # Python 3.12

>>> f"{
...     f"{
...         f"{
...             f"{
...                 f"{
...                     f"Deeply nested f-string!"
...                 }"
...             }"
...         }"
...     }"
... }"
'Deeply nested f-string!'
```

Before the new f-string implementation, there was no formal limit on how many levels of nesting you could have. However, the fact that you couldn’t reuse string quotes imposed a natural limit on the allowed levels of nesting in f-string literals. Starting with Python 3\.12, you can reuse quotes, so there are no limits for nesting f-strings.

[ Remove ads](/account/join/)

### Using Backslashes[](#using-backslashes "Permanent link")

Another limitation of f-strings before 3\.12 is that you can’t use backslash characters in embedded expressions. Consider the following example, where you try to [concatenate strings](https://realpython.com/python-string-concatenation/) using the newline (`\n`) [escape sequence](/ref/glossary/escape-sequence/):

Language: Python

```
>>> words = ["Hello", "World!", "I", "am", "a", "Pythonista!"]

>>> f"{'\n'.join(words)}"
  File "<input>", line 1
    f"{'\n'.join(words)}"
                        ^
SyntaxError: f-string expression part cannot include a backslash
```

In this example, you get a `SyntaxError` because f-strings don’t allow backslash characters inside expressions delimited by curly brackets.

Again, the new f-string implementation that comes with Python 3\.12 solves the issue:

Language: Python

```
>>> # Python 3.12

>>> words = ["Hello", "World!", "I", "am", "a", "Pythonista!"]

>>> f"{'\n'.join(words)}"
'Hello\nWorld!\nI\nam\na\nPythonista!'

>>> print(f"{'\n'.join(words)}")
Hello
World!
I
am
a
Pythonista!
```

The new f-string implementation lifted the limitation of using backslash characters in embedded expressions, so you can now use escape sequences in your f-strings.

### Writing Inline Comments[](#writing-inline-comments "Permanent link")

F-strings up to Python 3\.11 don’t allow you to use the `#` symbol in embedded expressions. Because of that, you can’t insert comments in embedded expressions. If you try to do it, then you’ll get a syntax error:

Language: Python

```
>>> employee = {
...     "name": "John Doe",
...     "age": 35,
...     "job": "Python Developer",
... }

>>> f"""Storing employee's data: {
...     employee['name'].upper()  # Always uppercase name before storing
... }"""
  File "<stdin>", line 3
    }"""
        ^
SyntaxError: f-string expression part cannot include '#'
```

When you use `#` to introduce a [comment](/ref/glossary/comment/) in an f-string, you get a `SyntaxError`. Fortunately, the new f-strings in Python 3\.12 also fix this problem:

Language: Python

```
>>> # Python 3.12

>>> employee = {
...     "name": "John Doe",
...     "age": 35,
...     "job": "Python Developer",
... }

>>> f"Storing employee's data: {
...     employee["name"].upper()  # Always uppercase name before storing
... }"
"Storing employee's data: JOHN DOE"
```

Now you can add inline comments if you ever need to clarify something in the embedded expressions of an f-string. Another improvement is that you can add line breaks inside the curly braces, similar to what you can do inside parentheses outside f-strings. You don’t even need to use the triple-quoted multiline strings to do this.

### Deciphering F-String Error Messages[](#deciphering-f-string-error-messages "Permanent link")

Python’s new PEG parser opens the door to many improvements in the language. From the user’s perspective, one of the most valuable improvements is that you now have [better error messages](https://realpython.com/python310-new-features/#better-error-messages). These enhanced error messages weren’t available for f-strings up to Python 3\.11 because they didn’t use the PEG parser. So, the error messages related to f-strings were less specific and clear.

Python 3\.12 came along to fix this issue, too. Take a look at the following example, which compares the error message for an incorrect f-string in both 3\.11 and 3\.12:

Language: Python

```
>>> # Python 3.11
>>> f"{42 + }"
  File "<stdin>", line 1
    (42 + )
          ^
SyntaxError: f-string: invalid syntax

>>> # Python 3.12
>>> f"{42 + }"
  File "<stdin>", line 1
    f"{42 + }"
          ^
SyntaxError: f-string: expecting '=', or '!', or ':', or '}'
```

The error message in the first example is generic and doesn’t point to the exact location of the error within the offending line. Additionally, the expression is surrounded by parentheses, which adds noise to the problem because the original code doesn’t include parentheses.

In Python 3\.12, the error message is more verbose. It signals the exact location of the problem in the affected line. Additionally, the exception message provides some suggestions that might help you fix the issue.

In this specific example, the suggestions aren’t that useful because they focus on an operator that’s possibly wrong. However, having the exact location where the problem happened gives you a strong clue. You have a missing operand in the embedded expression.

[ Remove ads](/account/join/)

## Using Traditional String Formatting Tools Over F-Strings[](#using-traditional-string-formatting-tools-over-f-strings "Permanent link")

Even though f-strings are a pretty cool and popular Python feature, they’re not the one-size-fits-all solution. Sometimes the modulo operator (`%`) or the `.format()` method provides a better solution. Sometimes, they’re your only option. It all depends on your specific use case.

In the following sections, you’ll learn about a few situations where f-strings may not be the best option. To kick things off, you’ll start with a use case that’s closely related to your code’s readability. That’s when you want to interpolate values from a dictionary into a given string.

### Dictionary Interpolation[](#dictionary-interpolation "Permanent link")

Interpolating dictionary values into a string may be a common requirement in your code. Because you now know that f-strings are neat, you may think of using them for this task. You end up with a piece of code that looks like the following:

Language: Python

```
>>> person = {"name": "Jane Doe", "age": 25}

>>> f"Hello, {person['name']}! You're {person['age']} years old."
"Hello, Jane Doe! You're 25 years old."
```

That’s great! The code works just fine. However, it doesn’t look clean because of all those dictionary key lookups embedded in the string. The f-string looks cluttered and may be hard to read. How about using the `.format()` method?

Here’s a new version of your code:

Language: Python

```
>>> "Hello, {name}! You're {age} years old.".format(**person)
"Hello, Jane Doe! You're 25 years old."

>>> "Hello, {name}!".format(**person)
'Hello, Jane Doe!'
```

In this example, you use direct names instead of dictionary lookups in the replacement fields. The only additional requirement is that you need to use the dictionary [unpacking](/ref/glossary/unpacking/) operator (`**`) in the call to `.format()`. Now, the string looks cleaner and is also a bit shorter than the version using an f-string.

As an additional gain, it’s important to note that the number of replacement fields in the string doesn’t have to match the number of keys in the input dictionary. The `.format()` method will ignore unnecessary keys.

You also have the option of using the modulo operator, though:

Language: Python

```
>>> "Hello, %(name)s! You're %(age)s years old." % person
"Hello, Jane Doe! You're 25 years old."

>>> "Hello, %(name)s!" % person
'Hello, Jane Doe!'
```

This time, the string is even shorter. You use direct names in the replacement fields and don’t have to use the dictionary unpacking operator because the modulo operator unpacks the dictionary for you. However, some may say that the replacement fields aren’t that readable and that the modulo operator has limited formatting capabilities.

So, what version do you prefer? Share your thoughts in the comments!

### Lazy Evaluation in Logging[](#lazy-evaluation-in-logging "Permanent link")

Providing [logging](https://realpython.com/python-logging-source-code/) messages is a common example of those use cases where you shouldn’t use f-strings or `.format()`. The `logging` module runs string interpolation [lazily](https://realpython.com/python-logging-source-code/#taking-advantage-of-lazy-formatting) to optimize performance according to the selected logging level.

For example, you may have a hundred debugging messages but only ten warning messages in your code. If you use an f-string or the `.format()` method to construct your logging messages, then Python will interpolate all the strings regardless of the logging level that you’ve chosen.

However, if you use the `%` operator and provide the values to interpolate as arguments to your logging functions, then you’ll optimize the interpolation process. The `logging` module will only interpolate those strings that belong to the current and higher logging levels.

Consider the following example:

Language: Python

```
>>> import logging
>>> msg = "This is a %s message!"

>>> logging.warning(msg, "WARNING")
WARNING:root:This is a WARNING message!

>>> logging.debug(msg, "DEBUGGING")
```

In this example, you use the modulo operator syntax to create the logging message. Then, you pass the value that you want to interpolate as an argument to the logging functions. Because `WARNING` is the default logging level, only the messages at this level and higher will be logged. That’s why the `debug()` function doesn’t generate any output.

In the above call to `debug()`, the string interpolation never happens because you’re using a higher logging level. However, if you use `.format()` like in the code below, then the interpolation will always happen:

Language: Python

```
>>> msg = "This is a {} message!"

>>> logging.debug(msg.format("DEBUGGING"))
```

If you call `debug()` a million times inside a loop, then Python will eagerly evaluate its argument, and the interpolation will happen a million times. This behavior will add performance overhead to your code. That’s why the `logging` module does the interpolation lazily.

The lazy nature of how `logging` does string formatting can make a difference, and it’s only possible using the modulo operator.

[ Remove ads](/account/join/)

### SQL Database Queries[](#sql-database-queries "Permanent link")

Using any string interpolation tool is a bad idea when you’re building SQL queries with dynamic parameters. In this scenario, interpolation tools invite [SQL injection attacks](https://realpython.com/prevent-python-sql-injection/).

To illustrate the problem, say that you’re working with a [PostgresSQL](https://realpython.com/python-sql-libraries/#postgresql) database using the [Psycopg 2](https://pypi.org/project/psycopg2/) adapter, and you want to run a query to get all the users with a given role or set of privileges. You come up with one of the following queries:

Language: Python

```
import psycopg2

connection = psycopg2.connect(
    database="db",
    user="user",
    password="password"
)
cursor = connection.cursor()

role = "admin"

query_modulo = "SELECT * FROM users WHERE role = '%s'" % role
query_format = "SELECT * FROM users WHERE role = '{role}'".format(role=role)
query_f_string = f"SELECT * FROM users WHERE role = '{role}'"

cursor.execute(query_modulo)
cursor.execute(query_format)
cursor.execute(query_f_string)
```

All of these strings directly insert the query parameter into the final query without any validation or security check. If you run any of these queries using the `.execute()` method, then the database won’t be able to perform any security checks on the parameters, which makes your code prone to SQL injection attacks.

**Note:** The code in the above example doesn’t run because of the missing `psycopg2` library and the assumption of a certain database structure and setup. It’s a demonstrative code example only.

To avoid the risk of SQL injection, you can use the `%` operator syntax to build the query template and then provide the query parameter as the second argument to the `.execute()` method in a tuple or list:

Language: Python

```
query_template = "SELECT * FROM users WHERE role = %s"

cursor.execute(query_template, (role,))
```

In this example, you use the `%` operator syntax to create the query template. Then, you provide the parameters as an independent argument to `.execute()`. In this case, the database system will use the specified type and value of `role` when executing the query. This practice offers protection against SQL injection.

**Note:** You should only use the modulo operator syntax in the string literal that represents the query template. You shouldn’t use the operator and the actual sequence of parameters to build the final query. Just let `.execute()` do the hard work and build the final query for you in a safer way.

In short, you must avoid using any string interpolation tool to build dynamic queries beforehand. Instead, use the `%` operator syntax to build the query template and pass the query parameters to `.execute()` in a sequence.

### Internationalization and Localization[](#internationalization-and-localization "Permanent link")

When you want to provide [internationalization and localization](https://en.wikipedia.org/wiki/Internationalization_and_localization) in a Python project, the `.format()` method is the way to go:

Language: Python

```
>>> greeting_template = "{greeting} Pythonista!"

>>> greeting_en = "Good Morning!"
>>> greeting_es = "¡Buenos días!"
>>> greeting_fr = "Bonjour!"

>>> for greeting in (greeting_en, greeting_es, greeting_fr):
...     print(greeting_template.format(greeting=greeting))
...
Good Morning! Pythonista!
¡Buenos días! Pythonista!
Bonjour! Pythonista!
```

You can support multiple languages using string templates. Then, you can handle localized string formatting based on the user’s locale. The `.format()` method will allow you to dynamically interpolate the appropriate strings depending on the user’s language selection.

## Converting Old String Into F-Strings Automatically[](#converting-old-string-into-f-strings-automatically "Permanent link")

If you’re working on porting a legacy codebase to modern Python, and one of your goals is to convert all your strings into f-strings, then you can use the [`flynt`](https://github.com/ikamensh/flynt) project. This tool allows you to convert traditional strings into f-strings quickly.

To use `flynt`, you need to [`pip`](https://realpython.com/what-is-pip/) install it first:

Language: Shell

```
$ python -m pip install flynt
```

This command downloads and installs `flynt` in your current Python environment. Once you have it installed, you can use the command against your code files. For example, say that you have the following Python file:

Language: Python

```
# sample.py

name = "Jane"
age = 25

print("Hello, %s! You're %s years old." % (name, age))
```

If you want to update this file and start using f-strings instead of the `%` operator, then you can just run the following command:

Language: Shell

```
$ flynt sample.py
Running flynt v.1.0.6
Using config file at .../pyproject.toml
Modified 1 of 1 files in 0.00s
```

This command tells `flynt` to update the content of your `sample.py` file by replacing strings that use the `%` operator and the `.format()` method with equivalent f-strings. Note that this command will modify your files in place. So, after running the command, `sample.py` will look something like the following:

Language: Python

```
# sample.py

name = "Jane"
age = 25

print(f"Hello, {name}! You're {age} years old.")
```

That’s cool, isn’t it? You can also run `flynt` against a complete directory containing a large Python codebase. It’ll scan every file and convert the old strings into f-strings. So, the tool is quite useful if you’re modernizing your codebase.

[ Remove ads](/account/join/)

## Frequently Asked Questions[](#frequently-asked-questions "Permanent link")

Now that you have some experience with Python f-strings, you can use the questions and answers below to check your understanding and recap what you’ve learned.

These FAQs are related to the most important concepts you’ve covered in this tutorial. Click the *Show/Hide* toggle beside each question to reveal the answer:

****What is an f-string in Python?****Show/Hide

An f-string, or formatted string literal, is a way to include expressions inside string literals using curly braces `{}`. Introduced in Python 3\.6, f-strings allow for more readable and concise string formatting and interpolation, and provide a more efficient alternative to older methods like the modulo (`%`) operator and `.format()` method.

****How do you write an f-string in Python?****Show/Hide

To write an f-string in Python, you need to add an `f` or `F` prefix before the string literal. Inside this string literal, you can include variables, objects, and expressions in curly braces.

****How do you format numbers in f-strings?****Show/Hide

You can format numbers in f-strings by using format specifiers inside the curly braces. For example, you can use `:.2f` to format a floating-point number with two decimal places.

****Can you embed expressions in f-strings?****Show/Hide

Yes, you can embed almost any Python expression in f-strings, including calculations, list comprehensions, and method calls.

****What are the advantages of f-strings compared to traditional tools?****Show/Hide

F-strings provide a few advantages over the `%` operator and the `.format()` method. They are more readable and concise because you can directly embed variables and expressions within the string. They are also faster and more efficient in programs that deal with a large number of strings.

****What limitations did f-strings have before Python 3\.12?****Show/Hide

Before Python 3\.12, f-strings had several limitations: they didn’t support the use of backslashes in embedded expressions, the reuse of the same type of quotation marks for nested f-strings, or comments within expressions. These limitations were addressed in Python 3\.12, enabling more flexible and complex expressions.

****When should you avoid using f-strings?****Show/Hide

You should avoid using f-strings when you need [lazy evaluation](/ref/computer-science-glossary/lazy-evaluation/), such as in logging, where the string should only be constructed if the log level warrants it. Additionally, avoid using them in SQL queries to prevent SQL injection risks. For internationalization and localization tasks, it’s better to use the `.format()` method.

How did you do? Would you like to take a quick quiz to evaluate your new skills? If so, then click the link below:

 **Take the Quiz:** Test your knowledge with our interactive “Python's F-String for String Interpolation and Formatting” quiz. You’ll receive a score upon completion to help you track your learning progress:

---

[](/quizzes/f-strings/)

![F-Strings in Python 3.6](https://files.realpython.com/media/Python-f-Strings-Guide_Watermark.2c8be8b1d392.jpg)

**Interactive Quiz**

[Python's F-String for String Interpolation and Formatting](/quizzes/f-strings/)

Test your understanding of Python f-strings, including syntax, expression embedding, type conversions, and quoting rules.

Mark as Completed

[](/feedback/survey/article/python-f-strings/liked/?from=article-footer "Liked it") [](/feedback/survey/article/python-f-strings/disliked/?from=article-footer "Disliked it")

Share

Recommended Course

[Python 3's F-Strings: An Improved String Formatting Syntax](/courses/python-3-f-strings-improved-string-formatting-syntax/) (52m)

🐍 Python Tricks 💌

Get a short & sweet **Python Trick** delivered to your inbox every couple of days. No spam ever. Unsubscribe any time. Curated by the Real Python team.

![Dictionary merging in Python 3.5+](https://files.realpython.com/media/pytrick-dict-merge.4201a0125a5e.png)

Send Me Python Tricks »

About **Joanna Jablonski**

Joanna is the Executive Editor of Real Python. She loves natural languages just as much as she loves programming languages!

[» More about Joanna](/team/jjablonski/)

---

*Each tutorial at Real Python is created by a team of developers so that it meets our high quality standards. The team members who worked on this tutorial are:*

[](/team/acutenco/)

Adriana

[](/team/asantos/)

Aldren

[](/team/bweleschuk/)

Brenda

[](/team/bzaczynski/)

Bartosz

[](/team/damos/)

David

[](/team/dbader/)

Dan

[](/team/gahjelle/)

Geir Arne

[](/team/janderson/)

Jim

[](/team/kfinegan/)

Kate

[](/team/lpozoramos/)

Leodanis

[](/team/mbreuss/)

Martin

[](/team/panni/)

Pavel

Master Real-World Python Skills With Unlimited Access to Real Python

![Locked learning resources](/static/videos/lesson-locked.f5105cfd26db.svg)

**Join us and get access to thousands of tutorials, hands-on video courses, and a community of expert Pythonistas:**

[Level Up Your Python Skills »](/account/join/?utm_source=rp_article_footer&utm_content=python-f-strings)

Master Real-World Python Skills  
With Unlimited Access to Real Python

![Locked learning resources](/static/videos/lesson-locked.f5105cfd26db.svg)

**Join us and get access to thousands of tutorials, hands-on video courses, and a community of expert Pythonistas:**

[Level Up Your Python Skills »](/account/join/?utm_source=rp_article_footer&utm_content=python-f-strings)

What Do You Think?

**Rate this article:**

[](/feedback/survey/article/python-f-strings/liked/?from=article-comments "Liked it") [](/feedback/survey/article/python-f-strings/disliked/?from=article-comments "Disliked it")

[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Frealpython.com%2Fpython-f-strings%2F) [Twitter](https://twitter.com/intent/tweet/?text=Interesting%20Python%20article%20on%20%40realpython%3A%20Python%26%23x27%3Bs%20F-String%20for%20String%20Interpolation%20and%20Formatting&url=https%3A%2F%2Frealpython.com%2Fpython-f-strings%2F) [Bluesky](https://bsky.app/intent/compose?text=Interesting%20Python%20article%20on%20%40realpython.com%3A%20Python%26%23x27%3Bs%20F-String%20for%20String%20Interpolation%20and%20Formatting%20https%3A%2F%2Frealpython.com%2Fpython-f-strings%2F) [Facebook](https://facebook.com/sharer/sharer.php?u=https%3A%2F%2Frealpython.com%2Fpython-f-strings%2F) [Email](mailto:?subject=Python%20article%20for%20you&body=Python%26%23x27%3Bs%20F-String%20for%20String%20Interpolation%20and%20Formatting%20on%20Real%20Python%0A%0Ahttps%3A%2F%2Frealpython.com%2Fpython-f-strings%2F%0A)

What’s your \#1 takeaway or favorite thing you learned? How are you going to put your newfound skills to use? Leave a comment below and let us know.

**Commenting Tips:** The most useful comments are those written with the goal of learning from or helping out other students. [Get tips for asking good questions](https://realpython.com/python-beginner-tips/#tip-9-ask-good-questions) and [get answers to common questions in our support portal](https://support.realpython.com).

---

Looking for a real-time conversation? Visit the [Real Python Community Chat](/community/) or join the next [“Office Hours” Live Q&A Session](/office-hours/). Happy Pythoning!

Keep Learning

Related Topics: [basics](/tutorials/basics/) [python](/tutorials/python/)

Related Learning Paths:

- [I/O Operations and String Formatting](/learning-paths/input-output-operations-and-string-formatting/?utm_source=realpython&utm_medium=web&utm_campaign=related-learning-path&utm_content=python-f-strings)

Related Courses:

- [Python 3's F-Strings: An Improved String Formatting Syntax](/courses/python-3-f-strings-improved-string-formatting-syntax/?utm_source=realpython&utm_medium=web&utm_campaign=related-course&utm_content=python-f-strings)

Related Tutorials:

- [Python Exceptions: An Introduction](/python-exceptions/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=python-f-strings)

- [Python's Format Mini-Language for Tidy Strings](/python-format-mini-language/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=python-f-strings)

- [Primer on Python Decorators](/primer-on-python-decorators/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=python-f-strings)

- [Python Classes: The Power of Object-Oriented Programming](/python-classes/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=python-f-strings)

- [Logging in Python](/python-logging/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=python-f-strings)

## Keep reading Real Python by creating a free account or signing in:

[![Keep reading](/static/videos/lesson-locked.f5105cfd26db.svg)](/account/signup/?intent=continue_reading&utm_source=rp&utm_medium=web&utm_campaign=rwn&utm_content=v1&next=%2Fpython-f-strings%2F)

[Continue »](/account/signup/?intent=continue_reading&utm_source=rp&utm_medium=web&utm_campaign=rwn&utm_content=v1&next=%2Fpython-f-strings%2F)

Already have an account? [Sign-In](/account/login/?intent=continue_reading&next=/python-f-strings/)

Almost there! Complete this form and click the button below to gain instant access:

![Python's F-String: An Improved String Interpolation and Formatting Tool](https://files.realpython.com/media/UPDATE-f-strings_Watermarked.4d90960e7897.jpg)

Python's F-String: An Improved String Interpolation and Formatting Tool (Sample Code)

Send Code »

🔒 No spam. We take your privacy seriously.

##### Learn Python

- [Start Here](/start-here/)

- [Your Learning Plan](/account/learning-plan/)

- [Browse Topics](/tutorials/all/)

- [Learning Resources](/search)

- [Python Reference](/ref/)

- [Cheat Sheets](/cheatsheets/)

- [Support Center](https://support.realpython.com)

##### Ways to Learn

- [Mentor AI](/mentor/)

- [Learning Paths](/learning-paths/)

- [Tutorials](/tutorials/)

- [Courses](/courses/)

- [Quizzes](/quizzes/)

- [Coding Exercises](/coding-exercises/)

- [Live Courses](/live/)

- [Books](/books/)

##### Skill Areas

- [Data Science](/start/data-science-analytics/)

- [AI Apps & Agents](/start/ai-apps-agents/)

- [Machine Learning](/start/machine-learning/)

- [Automation](/start/scripting-automation/)

- [Web Development](/start/web-development-apis/)

- [Cybersecurity](/start/cybersecurity/)

##### Community

- [Podcast](/podcasts/rpp/)

- [Newsletter](/newsletter/)

- [Community Chat](/community/)

- [Office Hours](/office-hours/)

- [Learner Stories](/learner-stories/)

##### Membership

- [Plans & Pricing](/account/join/)

- [Team Plans](/account/join-team/)

- [For Business](/account/join-team/inquiry/)

- [For Schools](/account/join-team/education-inquiry/)

- [Reviews](/learner-stories/)

##### Company

- [About Us](/about/)

- [Team](/team/)

- [Mission & Values](/mission/)

- [Editorial Guidelines](/editorial-guidelines/)

- [Sponsorships](/sponsorships/)

- [Careers](https://realpython.workable.com)

- [Press Kit](/media-kit/)

- [Merch](/merch)

[](https://www.youtube.com/realpython "YouTube") [](https://x.com/realpython "X/Twitter") [](https://www.linkedin.com/company/realpython-com "LinkedIn") [](https://www.facebook.com/LearnRealPython "Facebook") [](https://github.com/realpython/ "GitHub")

[Privacy Policy](/privacy-policy/) ⋅ [Terms of Use](/terms/) ⋅ [Security](/security/) ⋅ [Contact](/contact/)

Happy Pythoning!

© 2012–2026 DevCademy Media Inc. DBA Real Python. All rights reserved.  
REALPYTHON™ is a trademark of DevCademy Media Inc. [ ![Real Python - Online Python Training (logo)](/static/real-python-logo-primary.973743b6d39d.svg)](/)