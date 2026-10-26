# How to Print without newline in Python?

> Source: https://www.geeksforgeeks.org/python/print-without-newline-python/
> Collected: 2026-10-26
> Published: 2025-04-26

In Python, the print() function adds a newline by default after each output. To print without a newline, you can use the end parameter in the print() function and set it to an empty string or a space, depending on your needs. This allows you to print on the same line.

Example:

Python

```
print("geeks", end =" ")
print("geeksforgeeks")
```

Output

```
geeks geeksforgeeks
```

Explanation: In the first print() statement, end=" " is used, which means a space (" ") is printed instead of the default newline after the word "geeks". The second print() statement prints "geeksforgeeks" immediately after "geeks", on the same line.

## Using Python join

You can use the join() method to combine elements of an iterable into a single string and then print it.

python

```
a = ["Hello", "World"]
print(" ".join(a))
```

Output

```
Hello World
```

Explanation: " ".join(a) joins the elements of the list a using a space as the separator, resulting in the string "Hello World".

## Using asterisk ( * ) operator

In Python, you can use the asterisk (*) operator to unpack a list or tuple and print its elements without adding a newline between them.

Python

```
a = [1, 2, 3, 4, 5, 6]
print(*a)
```

Output

```
1 2 3 4 5 6
```

Explanation: The * operator unpacks the list, passing its individual elements as separate arguments to the print() function. This prints the list elements separated by spaces.

## Using Python sys Module

To use the sys module, first, import the module sys using the import keyword. Then, make use of the stdout.write() method available inside the sys module, to print your strings. It only works with string. If you pass a number or a list, you will get a TypeError.

Python

```
import sys

sys.stdout.write("GeeksforGeeks ")
sys.stdout.write("is best website for coding!")
```

Output

```
GeeksforGeeks is best website for coding!
```

Explanation: Unlike the print() function, which automatically adds a newline at the end of the output, sys.stdout.write() writes the specified text to the console exactly as it is, without any extra characters (like a newline).
