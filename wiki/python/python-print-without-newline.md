# How to Print without newline in Python

> Sources: GeeksforGeeks, 2025-04-26
> Raw: [2025-04-26-python-print-without-newline.md](../../raw/python/2025-04-26-python-print-without-newline.md)
> Updated: 2026-10-26

## Overview

By default, Python's `print()` appends a newline after each output. To print on the same line, use the `end` parameter (e.g., `end=" "` or `end=""`). Other approaches: `str.join()`, unpacking with `*`, and `sys.stdout.write()`.

## Methods

- **`end` parameter**: `print("geeks", end=" ")` then `print("geeksforgeeks")` → `geeks geeksforgeeks`.
- **`join()`**: `" ".join(["Hello", "World"])` → `Hello World`.
- **Unpacking `*`**: `print(*[1, 2, 3, 4, 5, 6])` → `1 2 3 4 5 6`.
- **`sys.stdout.write()`**: writes text exactly as given, no automatic newline; works only with strings (numbers/lists raise `TypeError`).

## See Also

- [Code Cultivation — Object-Oriented Garden Systems](code-cultivation.md)
- [Python f-Strings](python-f-strings.md)
