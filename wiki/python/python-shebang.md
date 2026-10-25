# Executing Python Scripts With a Shebang

> Sources: Bartosz Zaczyński, 2025-01-25; Stack Overflow community (treecoder et al.), 2011-08-02
> Raw: [python-shebang.md](../../raw/python/python-shebang.md); [stackoverflow-shebang.md](../../raw/python/stackoverflow-shebang.md)
> Updated: 2026-10-25

## Overview

A tutorial on the shebang line (`#!`) in Python scripts. A shebang tells the operating system’s shell which interpreter to use to execute a file, allowing direct execution without typing `python`/`python3`. It applies to Unix-like systems (macOS, Linux) and is ignored on Windows. The article covers how shebangs work, portable shebangs via `/usr/bin/env`, passing arguments, alternatives, polyglot/custom-interpreter examples, and best practices.

## What and When

- Shebang must be on the **first line** of the script and start with `#!` (hash + exclamation mark), followed by an **absolute path** to the interpreter (e.g., `#!/usr/bin/python3`). Relative paths have no effect.
- Recognized by Unix shells (Bash, Zsh) on Unix-like OSes; ignored on Windows (use WSL or file associations).
- Use for **runnable scripts** executed directly; not for import-only modules.
- Commonly combined with the name-main idiom (`if __name__ == "__main__":`).
- PEP 263 encoding comments (`# -*- coding: utf-8 -*-`) are obsolete now that Python defaults to UTF-8.

## How It Works

- Files are not executable by default; use `chmod +x script.py` to grant execute permission.
- Without a shebang, the shell interprets the file as shell script → syntax errors on Python code; the `.py` extension is irrelevant.
- With a shebang, the shell passes the file to the specified interpreter.

## Portable Shebang

- Avoid hard-coded absolute paths; use `#!/usr/bin/env python3`, which locates the first `python3` on `PATH` (works with virtualenvs).
- Never use bare `python` (may map to Python 2 or 3); use `python3` (see PEP 394).
- Pass arguments with the `-S` flag: `#!/usr/bin/env -S python3 -i`.
- Shebang line length may be limited on some systems.
- Alternatives: setuptools/Poetry entry points, `__main__.py`, executable ZIP apps.

## Examples

- Cross-version: `#!/usr/bin/env python` for Python 2/3-compatible scripts.
- Polyglot scripts: same code run via Perl (`#!/usr/bin/env perl`), Node.js (`#!/usr/bin/env node`), Java (`#!/usr/bin/env -S java --source 11`).
- Custom interpreter: a Python-implemented `brainf` command used as `#!/usr/bin/env brainf`.
- Environment output example: `Python 3.13.1 (main, Dec 5 2024, 13:58:44) [GCC 9.4.0] on linux`.

## Best Practices

- Shebang only for runnable scripts on Unix-like systems.
- No comments before the shebang line.
- Start with `#!`.
- Use `#!/usr/bin/env python3` for portability.
- Avoid bare `python`.
- Use `-S` for interpreter arguments.
- Keep shebang line short.
- Consider generating the shebang via tooling rather than manually.

## Community Perspectives (Stack Overflow)

Additional guidance from a widely referenced Stack Overflow Q&A (971974 views):

- Use `#!/usr/bin/env python3` for Python 3 scripts and `#!/usr/bin/env python2` for Python 2 scripts; avoid bare `#!/usr/bin/env python` except for code compatible with both (PEP 394).
- `#!/usr/local/bin/python` (hard-coded interpreter path) is non-portable and may fail.
- Shebang is only needed for scripts run directly; it is ignored when running via `python script.py` or importing.
- Do not add shebangs to import-only modules (though modules with a `__main__` test block may justify one).
- Installed/distributed scripts should use a specific interpreter path (e.g., `/usr/bin/python`), typically generated automatically by setuptools/distribution tools — not written manually.
- Virtual environments: `#!/usr/bin/env python` can let pyenv/venv control the interpreter.
- Windows: Python 3.3+ provides `py.exe` launcher that reads the shebang; registry association may need updating.
- Community trick: polyglot shell/Python scripts using `#!/bin/sh` with a quoted multi-line string to select among multiple Python installs.
- PEP 394: `python` may map to python2 or python3 depending on the system.

## See Also

- [Code Cultivation — Object-Oriented Garden Systems](code-cultivation.md)
- [Python Classes: The Power of Object-Oriented Programming](python-classes.md)
