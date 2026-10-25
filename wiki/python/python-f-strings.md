# Python's F-String for String Interpolation and Formatting

> Sources: Joanna Jablonski, 2026-10-23
> Raw: [2026-10-23-python-f-strings.md](../../raw/python/2026-10-23-python-f-strings.md)
> Updated: 2026-10-25

## Overview

A tutorial on Python f-strings (formatted string literals), introduced in Python 3.6 via PEP 498. An f-string is prefixed with `f` or `F` and embeds expressions in curly braces `{}` that are evaluated at runtime, making interpolation more readable, concise, and faster than the modulo operator (`%`) or `str.format()`. The article also covers the string formatting mini-language, special flags, performance, Python 3.12 improvements, and cases where traditional tools are preferable.

## Before F-Strings: Traditional Tools

- **Modulo operator (`%`)**: conversion specifiers like `%s`, `%f`, `%d`; supports tuples and dictionaries (`%(name)s`); format specifiers for precision/width (e.g., `%.2f`, `%5s`); inspired by C `printf`. Issues: hard to interpolate tuples, limited formatting, no mini-language.
- **`str.format()`**: replacement fields in `{}`; positional indices or keyword names; dictionary unpacking with `**`; supports format specifiers (e.g., `:.2f`, `:=^30`) and the full mini-language.

## F-String Basics

- Prefix string literal with `f`/`F`; embed variables/objects/expressions in `{}`.
- Evaluated at runtime; embedded names must be in scope.
- Can embed almost any expression: arithmetic, method calls (e.g., `name.upper()`), list comprehensions (e.g., `[2**n for n in range(3, 9)]`).

## Formatting With F-Strings

- Supports the string formatting mini-language; format specifier follows a colon after the expression: `f"{balance:.2f}"`.
- Dynamic specifiers: embed variables in the specifier itself, e.g., `f"{integer:{sep}}"`.
- Examples: thousand separators (`{integer:,}`, `{integer:_}`), two decimals (`{floating_point:,.2f}`), zero-padded dates (`{date[0]:02}`), datetime format (`{date:%m/%d/%Y}`).

## Other Relevant Features

- **String representation flags**: `!s` uses `.__str__()` (user-friendly), `!r` uses `.__repr__()` (developer-friendly).
- **Self-documenting expressions**: `f"{variable = }"` prints `variable = '...'` for debugging; whitespace around `=` is optional but reflected in output.
- **Performance**: f-strings are slightly faster than `%` and `.format()` (benchmark 87.08 ms vs 90.98 ms vs 144.69 ms for 1000000 iterations).

## Python 3.12+ Improvements

The new PEG-based f-string parser (Python 3.12) lifted prior limitations:

- **Quotation marks**: can reuse the same quote type inside expressions (e.g., `f"Hello, {person["name"]}"`); nesting depth no longer limited by available quote delimiters.
- **Backslashes**: allowed in embedded expressions (e.g., `'\n'.join(words)`).
- **Inline comments**: `#` comments allowed inside braces; line breaks inside braces without triple quotes.
- **Better error messages**: precise location and suggestions.

Note: Python 3.14 added **t-strings** (template strings) that produce a `Template` object instead of a string, allowing processing of interpolated values before building final text.

## When to Prefer Traditional Tools

- **Dictionary interpolation**: `.format(**person)` or `% person` can be cleaner than repeated key lookups in f-strings.
- **Lazy evaluation in logging**: `logging` does lazy interpolation only with the `%` operator; using f-strings eagerly evaluates all messages regardless of log level.
- **SQL queries**: never interpolate parameters into queries (SQL injection); use `%s` template with parameters passed to `.execute()`.
- **Internationalization/localization**: `.format()` preferred for template-based localized strings.

## Converting Legacy Code

- Use the `flynt` tool (`pip install flynt`) to automatically convert `%`/`.format()` strings to f-strings in files or directories.

## Frequently Asked Questions

- F-string = formatted string literal, prefixed with `f`/`F`, expressions in `{}`; introduced Python 3.6.
- Format numbers with specifiers like `:.2f`.
- Almost any expression can be embedded.
- Advantages: readability, conciseness, speed.
- Pre-3.12 limitations: no backslashes, no quote reuse, no comments in expressions.
- Avoid f-strings for lazy logging evaluation, SQL queries, and i18n/l10n.

## See Also

- [Python Classes: The Power of Object-Oriented Programming](python-classes.md)
