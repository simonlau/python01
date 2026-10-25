# Should I put shebang in Python scripts, and what form should it take?

> Source: https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take
> Collected: 2026-10-25
> Published: 2011-08-02

Question by treecoder (score 1299, views 971974)

Tags: python, shell, python-3.x, shebang

## Question

Should I put the shebang in my Python scripts? In what form?

`#!/usr/bin/env python 
`

or

`#!/usr/local/bin/python
`

Are these equally portable? Which form is used most?

Note: the tornado project uses the shebang. On the other hand the Django project doesn't.

---

## Answers (sorted by votes)

### Answer (score 1737) by GlassGhost — 2013-10-10
(accepted answer)

The shebang line in any script determines the script's ability to be executed like a standalone executable without typing `python` beforehand in the terminal or when double clicking it in a file manager (when configured properly). It isn't necessary but generally put there so when someone sees the file opened in an editor, they immediately know what they're looking at. However, which shebang line you use is important.

Correct usage for (defaults to version 3.latest) Python 3 scripts is:

`#!/usr/bin/env python3
`
Correct usage for (defaults to version 2.latest) Python 2 scripts is:

`#!/usr/bin/env python2
`
The following should not be used (except for the rare case that you are writing code which is compatible with both Python 2.x and 3.x):

`#!/usr/bin/env python
`
The reason for these recommendations, given in PEP 394, is that `python` can refer either to `python2` or `python3` on different systems.

Also, do not use:

`#!/usr/local/bin/python
`

"python may be installed at /usr/bin/python or /bin/python in those
cases, the above #! will fail."

―"#!/usr/bin/env python" vs "#!/usr/local/bin/python"

---

### Answer (score 104) by Amber — 2011-08-02

It's really just a matter of taste. Adding the shebang means people can invoke the script directly if they want (assuming it's marked as executable); omitting it just means `python` has to be invoked manually.

The end result of running the program isn't affected either way; it's just options of the means.

---

### Answer (score 53) by jfs — 2015-08-12

Should I put the shebang in my Python scripts?

Put a shebang into a Python script to indicate:

- this module can be run as a script
- whether it can be run only on python2, python3 or is it Python 2/3 compatible
- on POSIX, it is necessary if you want to run the script directly without invoking `python` executable explicitly

Are these equally portable? Which form is used most?

If you write a shebang manually then always use `#!/usr/bin/env python` (or `#!/usr/bin/env python2` / `#!/usr/bin/env python3`, see on that below) unless you have a specific reason not to use it. This form is understood even on Windows (Python launcher).

Note: installed scripts should use a specific python executable e.g., `/usr/bin/python` or `/home/me/.virtualenvs/project/bin/python`. It is bad if some tool breaks if you activate a virtualenv in your shell. Luckily, the correct shebang is created automatically in most cases by `setuptools` or your distribution package tools (on Windows, `setuptools` can generate wrapper `.exe` scripts automatically).

In other words, if the script is in a source checkout then you will probably see `#!/usr/bin/env python`. If it is installed then the shebang is a path to a specific python executable such as `#!/usr/local/bin/python`  (NOTE: you should not write the paths from the latter category manually).

To choose whether you should use `python`, `python2`, or `python3` in the shebang, see PEP 394 - The "python" Command on Unix-Like Systems:

- ... `python` should be used in the shebang line only for scripts that are
source compatible with both Python 2 and 3.

- in preparation for an eventual change in the default version of
Python, Python 2 only scripts should either be updated to be source
compatible with Python 3 or else to use `python2` in the shebang line.

---

### Answer (score 22) by Chris Johnson — 2013-08-10

If you have more than one version of Python and the script needs to run under a specific version, the she-bang can ensure the right one is used when the script is executed directly, for example:

`#!/usr/bin/python2.7
`

Note the script could still be run via a complete Python command line, or via import, in which case the she-bang is ignored.  But for scripts run directly, this is a decent reason to use the she-bang.

`#!/usr/bin/env python` is generally the better approach, but this helps with special cases.

Usually it would be better to establish a Python virtual environment, in which case the generic `#!/usr/bin/env python` would identify the correct instance of Python for the virtualenv.

---

### Answer (score 17) by meson10 — 2011-08-02

The purpose of shebang is for the script to recognize the interpreter type when you want to execute the script from the shell. 
Mostly, and not always, you execute scripts by supplying the interpreter externally.
Example usage: `python-x.x script.py`

This will work even if you don't have a shebang declarator.

Why first one is more "portable" is because, `/usr/bin/env` contains your `PATH` declaration which accounts for all the destinations where your system executables reside.

NOTE: Tornado doesn't strictly use shebangs, and Django strictly doesn't. It varies with how you are executing your application's main function.

ALSO: It doesn't vary with Python.

---

### Answer (score 16) by pepr — 2013-01-30

Sometimes, if the answer is not very clear (I mean you cannot decide if yes or no), then it does not matter too much, and you can ignore the problem until the answer is clear.

The `#!` only purpose is for launching the script. Django loads the sources on its own and uses them. It never needs to decide what interpreter should be used. This way, the `#!` actually makes no sense here.

Generally, if it is a module and cannot be used as a script, there is no need for using the `#!`. On the other hand, a module source often contains `if __name__ == '__main__': ...` with at least some trivial testing of the functionality. Then the `#!` makes sense again.

One good reason for using `#!` is when you use both Python 2 and Python 3 scripts -- they must be interpreted by different versions of Python. This way, you have to remember what `python` must be used when launching the script manually (without the `#!` inside). If you have a mixture of such scripts, it is a good idea to use the `#!` inside, make them executable, and launch them as executables (chmod ...).

When using MS-Windows, the `#!` had no sense -- until recently. Python 3.3 introduces a Windows Python Launcher (py.exe and pyw.exe) that reads the `#!` line, detects the installed versions of Python, and uses the correct or explicitly wanted version of Python. As the extension can be associated with a program, you can get similar behaviour in Windows as with execute flag in Unix-based systems.

---

### Answer (score 14) by Lennart Regebro — 2011-08-02

You should add a shebang if the script is intended to be executable. You should also install the script with an installing software that modifies the shebang to something correct so it will work on the target platform. Examples of this is distutils and Distribute.

---

### Answer (score 11) by Goblinhack — 2019-09-23

If you have different modules installed and need to use a specific 
python install, then shebang appears to be limited at first. However,
you can do tricks like the below to allow the shebang to be invoked
first as a shell script and then choose python. This is very flexible
imo:

```
#!/bin/sh
#
# Choose the python we need. Explanation:
# a) '''\' translates to \ in shell, and starts a python multi-line string
# b) "" strings are treated as string concat by python, shell ignores them
# c) "true" command ignores its arguments
# c) exit before the ending ''' so the shell reads no further
# d) reset set docstrings to ignore the multiline comment code
#
"true" '''\'
PREFERRED_PYTHON=/Library/Frameworks/Python.framework/Versions/2.7/bin/python
ALTERNATIVE_PYTHON=/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
FALLBACK_PYTHON=python3

if [ -x $PREFERRED_PYTHON ]; then
    echo Using preferred python $PREFERRED_PYTHON
    exec $PREFERRED_PYTHON "$0" "$@"
elif [ -x $ALTERNATIVE_PYTHON ]; then
    echo Using alternative python $ALTERNATIVE_PYTHON
    exec $ALTERNATIVE_PYTHON "$0" "$@"
else
    echo Using fallback python $FALLBACK_PYTHON
    exec python3 "$0" "$@"
fi
exit 127
'''

__doc__ = """What this file does"""
print(__doc__)
import platform
print(platform.python_version())

```

Or better yet, perhaps, to facilitate code reuse across multiple python scripts:

```
#!/bin/bash
"true" '''\'; source $(cd $(dirname ${BASH_SOURCE[@]}) &>/dev/null && pwd)/select.sh; exec $CHOSEN_PYTHON "$0" "$@"; exit 127; '''

```

and then select.sh has:

```
PREFERRED_PYTHON=/Library/Frameworks/Python.framework/Versions/2.7/bin/python
ALTERNATIVE_PYTHON=/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
FALLBACK_PYTHON=python3

if [ -x $PREFERRED_PYTHON ]; then
    CHOSEN_PYTHON=$PREFERRED_PYTHON
elif [ -x $ALTERNATIVE_PYTHON ]; then
    CHOSEN_PYTHON=$ALTERNATIVE_PYTHON
else
    CHOSEN_PYTHON=$FALLBACK_PYTHON
fi

```

---

### Answer (score 10) by ETalbot — 2017-06-02

When I installed Python 3.6.1 on Windows 7 recently, it also installed the Python Launcher for Windows, which is supposed to handle the shebang line.  However, I found that the Python Launcher did not do this: the shebang line was ignored and Python 2.7.13 was always used (unless I executed the script using py -3).

To fix this, I had to edit the Windows registry key `HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Python.File\shell\open\command`.  This still had the value

```
"C:\Python27\python.exe" "%1" %*

```

from my earlier Python 2.7 installation.  I modified this registry key value to

```
"C:\Windows\py.exe" "%1" %*

```

and the Python Launcher shebang line processing worked as described above.

---

### Answer (score 9) by SDsolar — 2017-01-22

Answer:  Only if you plan to make it a command-line executable script.

Here is the procedure:

Start off by verifying the proper shebang string to use:

```
which python

```

Take the output from that and add it (with the shebang #!) in the first line.

On my system it responds like so:

```
$which python
/usr/bin/python

```

So your shebang will look like:

```
#!/usr/bin/python

```

After saving, it will still run as before since python will see that first line as a comment.

```
python filename.py

```

To make it a command, copy it to drop the .py extension.  

```
cp filename.py filename

```

Tell the file system that this will be executable:

```
chmod +x filename

```

To test it, use:

```
./filename

```

Best practice is to move it somewhere in your $PATH so all you need to type is the filename itself. 

```
sudo cp filename /usr/sbin

```

That way it will work everywhere (without the ./ before the filename)

---

### Answer (score 5) by F1Linux — 2020-04-11

This is really a question about whether the path to the Python interpreter should be absolute or logical (`/usr/bin/env`) with respect to portability.

My view after thoroughly testing the behavior is that the logical path in the she-bang is the better of the two options.

Being a Linux Engineer, my goal is always to provide the most suitable, optimized hosts for my developer clients, so the issue of Python environments is something I really need a solid answer to. Encountering other answers on this and other Stack Overflow sites which talked about the issue in a general way without supporting proofs, I've performed some really granular testing & analysis on this very question on Unix.SE.

---

### Answer (score 3) by mara004 — 2021-09-18

For files that are intended to be executable from the command-line, I would recommend

```
#! /usr/bin/env python3

```

Otherwise you don't need the shebang (though of course it doesn't harm).

---

### Answer (score 2) by user123664 — 2021-03-30

If you use virtual environments like with pyenv it is better to write `#!/usr/bin/env python`
The pyenv setting will control which version of python and from which file location is started to run your script.

If your code is known to be version specific, it will help others to find why your script does not behave in their environment if you specify the expected version in the shebang.

---

### Answer (score 2) by MukeshKumar — 2021-10-05

If you want to make your file executable you must add shebang line to your scripts.

```
#!/usr/bin/env python3 

```

is better option in the sense that this will not be dependent on specific distro of linux but could be used on almost all linux distro since it hunts for the python3 path from environment variables, which is different for different distros of linux.

whereas

```
#!/usr/local/bin/python3 

```

would be a distro specific path for python3 and would not work if python3 is not found on this path, and could result in confusion and ambiguity for developer when migrating from one distro to another of linux.

---

### Answer (score -3) by frp farhan — 2016-12-21

Use first

```
which python

```

This will give the output as the location where my python interpreter (binary) is present.

This output could be any such as

```
/usr/bin/python

```

or

```
/bin/python

```

Now appropriately select the shebang line and use it.

To generalize we can use:

```
#!/usr/bin/env

```

or 

```
#!/bin/env

```

---
