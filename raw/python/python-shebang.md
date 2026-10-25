# Executing Python Scripts With a Shebang

> Source: https://realpython.com/python-shebang/
> Collected: 2026-10-25
> Published: 2025-01-25

In shell scripts, the [shebang](/ref/glossary/shebang/) line (`#!`) specifies the path to the interpreter that should execute the file. You can place it at the top of your Python file to tell the shell how to run your script, allowing you to execute the script directly without typing `python` before the script name. The shebang is essential for Unix-like systems but ignored on Windows unless using specific compatibility layers.

## What’s a Shebang, and When Should You Use It?

In short, a [shebang](https://en.wikipedia.org/wiki/Shebang_\(Unix\)) is a special kind of [comment](https://realpython.com/python-comments-guide/) that you may include in your source code to tell the operating system’s [shell](https://en.wikipedia.org/wiki/Shell_\(computing\)) where to find the interpreter for the rest of the file:

Language: Python

```
#!/usr/bin/python3

print("Hello, World!")
```

If you’re using a shebang, it must appear on the **first line** in your script, and it has to start with a [hash sign (`#`)](https://en.wikipedia.org/wiki/Number_sign) followed by an [exclamation mark (`!`)](https://en.wikipedia.org/wiki/Exclamation_mark), colloquially known as the bang, hence the name *shebang*. The choice of the hash sign to begin this special sequence of characters wasn’t accidental, as many [scripting languages](https://en.wikipedia.org/wiki/Scripting_language) use it for inline comments.

You should make sure you don’t put any other comments before the shebang line if you want it to work correctly, or else it won’t be recognized! After the exclamation mark, specify an **absolute path** to the relevant code interpreter, such as Python. Providing a relative path will have no effect, unfortunately.

**Note:** The shebang is only recognized by shells, such as [Z shell](https://en.wikipedia.org/wiki/Z_shell) or [Bash](https://en.wikipedia.org/wiki/Bash_\(Unix_shell\)), running on [Unix-like](https://en.wikipedia.org/wiki/Unix-like) operating systems, including macOS and Linux distributions. It bears no particular meaning in the [Windows terminal](https://realpython.com/python-coding-setup-windows/#discovering-the-windows-terminal), which treats the shebang as an ordinary comment by ignoring it.

You can get the shebang to work on Windows by installing the [Windows Subsystem for Linux (WSL)](https://realpython.com/effective-python-environment/#windows-subsystem-for-linux) that comes with a Unix shell. Alternatively, Windows lets you make a global [file association](https://learn.microsoft.com/en-us/windows/win32/shell/fa-how-work) between a file extension like `.py` and a program, such as the Python interpreter, to achieve a similar effect.

It’s not uncommon to combine a shebang with the [name-main idiom](https://realpython.com/if-name-main-python/), which prevents the main block of code from running when someone imports the file from another module:

Language: Python

```
#!/usr/bin/python3

if __name__ == "__main__":
    print("Hello, World!")
```

A shebang is only relevant to [runnable scripts](https://realpython.com/run-python-scripts/) that you wish to execute without explicitly specifying the program to run them through. You wouldn’t typically put a shebang in a [Python module](https://realpython.com/python-modules-packages/) that only contains [function](https://realpython.com/defining-your-own-python-function/) and [class definitions](https://realpython.com/python3-object-oriented-programming/#how-do-you-define-a-class-in-python) meant for [importing](https://realpython.com/python-import/) from other modules. Therefore, use the shebang when you don’t want to prefix the command that runs your Python script with `python` or `python3`.

**Note:** In the old days of Python, the shebang line would sometimes appear alongside another specially formatted comment described in [PEP 263](https://peps.python.org/pep-0263/):

Language: Python

```
#!/usr/bin/python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    print("Grüß Gott")
```

The highlighted line used to be necessary to tell the interpreter which [character encoding](https://realpython.com/python-encodings-guide/) it should use to read your source code correctly, as Python defaulted to [ASCII](https://en.wikipedia.org/wiki/ASCII). However, this was only important when you directly embedded non-Latin characters, such as ü or ß, in your code.

This special comment is irrelevant today because modern Python versions use the universal UTF-8 encoding, which can handle such characters with ease. Nevertheless, it’s always preferable to replace tricky characters with their encoded representations using Unicode literals:

Language: Python

```
>>> "Grüß Gott".encode("unicode_escape")
b'Gr\\xfc\\xdf Gott'
```

## How Does a Shebang Work?

Normally, to run a program in the [terminal](https://realpython.com/terminal-commands/), you must provide the full path to a particular **binary executable** or the name of a command present in one of the directories listed on the [`PATH`](https://en.wikipedia.org/wiki/PATH_\(variable\)) environment variable. One or more command-line arguments may follow this path or command:

Language: Shell

```
$ /usr/bin/python3 -c 'print("Hello, World!")'
Hello, World!

$ python3 -c 'print("Hello, World!")'
Hello, World!
```

In practice, most of your Python programs will consist of more than one line of code spread across several modules. There will usually be a single runnable entry point to your program: a script, which you can pass on to the Python interpreter for execution:

Language: Shell

```
$ python3 /path/to/your/script.py
Hello, World!
```

However, your shell can also execute **scripts** or text files that contain source code expressed in a high-level interpreted language like Python, [Perl](https://en.wikipedia.org/wiki/Perl), or [JavaScript](https://realpython.com/python-vs-javascript/). Because executing scripts can potentially have harmful side effects, especially if they come from untrusted sources, files aren’t executable by default. When you try running a Python script without making it executable first, you’ll see this error message in the terminal:

Language: Shell

```
$ ./script.py
bash: ./script.py: Permission denied
```

In general, you can give permission to execute the specified file to its owner, a user belonging to the user group associated with the file, or everyone else. To let anyone execute your script, you can change its file mode bits using the `chmod` command:

Language: Shell

```
$ chmod +x script.py
```

While you should be able to run your script now, it’s still not going to work the way you intended:

Language: Shell

```
$ ./script.py
./script.py: line 1: syntax error near unexpected token `"Hello, World!"'
./script.py: line 1: `print("Hello, World!")'
```

Unless you include a shebang at the beginning of the file, the shell will assume that your script is written in the corresponding shell language. For example, if you’re on the Bash shell, then the shell will expect to find the Bash commands in your file. So, when it stumbles on a call to Python’s `print()` function in your script, it doesn’t understand it. Note that the file’s extension, such as `.py`, is completely irrelevant!

It’s only when you provide the absolute path to your Python interpreter using a shebang in your script that the shell will know where to pass that script:

Language: Shell

```
$ cat script.py
#!/usr/bin/python3
print("Hello, World!")

$ ./script.py
Hello, World!
```

Unfortunately, hard-coding an absolute path in the shebang isn’t super portable across systems, even within the Unix family.

## How Can You Define a Portable Shebang?

Remember that you can’t specify a relative path in a shebang, as it always has to be absolute. Because of this limitation, many developers have adopted a work-around by using the `/usr/bin/env` command, which can figure out the actual path to the Python interpreter:

Language: Python

```
#!/usr/bin/env python3

print("Hello, World!")
```

When invoked without any arguments, the `/usr/bin/env` command will display the [environment variables](https://en.wikipedia.org/wiki/Environment_variable) defined in your shell. Its primary purpose, though, is to run a program in a modified environment, letting you temporarily override certain variables. For example, you can change the language of a given program by setting the `LANG` variable with it:

Language: Shell

```
$ /usr/bin/env LANG=es_ES.UTF_8 git status
En la rama master
Tu rama está actualizada con 'origin/master'.

nada para hacer commit, el árbol de trabajo está limpio
```

The nice thing about `/usr/bin/env` is that you don’t have to change any environment variables whatsoever to run a command:

Language: Shell

```
$ /usr/bin/env python3
Python 3.13.1 (main, Dec  5 2024, 13:58:44) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

As a side effect, it’ll find the first occurrence of the specified executable, such as `python3`, on the `PATH` variable and run it for you. That’s quite useful when you consider that activating a Python virtual environment modifies the `PATH` variable in your current terminal session by prepending the parent folder of the Python executable in the active virtual environment:

Language: Shell

```
$ which python3
/usr/bin/python3

$ python -m venv venv/
$ source venv/bin/activate

(venv) $ which python3
/home/realpython/venv/bin/python3

(venv) $ echo $PATH
/home/realpython/venv/bin
⮑:/home/realpython/.local/bin:/usr/local/sbin:/usr/local/bin
⮑:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
⮑:/snap/bin:/home/realpython/.local/bin:
```

**Note:** Never use the bare `python` command in a shebang because it may map to either `python2` or `python3`, depending on the operating system and its configuration. The only exception would be if you wrote the script in a backward-compatible way and wanted it to run through both Python versions. You can find out more about the [recommended practices](https://peps.python.org/pep-0394/#recommendation) in PEP 394\.

One shortcoming of `/usr/bin/env` is that it doesn’t let you pass any arguments to the underlying command out of the box. So, if you wanted to run `python3 -i` to keep the Python interpreter running in an [interactive mode](https://docs.python.org/3/using/cmdline.html#cmdoption-i) after your script finishes, then it would throw a wrench into the works:

Language: Shell

```
$ ./script.py
/usr/bin/env: ‘python3 -i’: No such file or directory
/usr/bin/env: use -[v]S to pass options in shebang lines
```

Fortunately, there’s a quick fix for that, which the error message hints at. You can use the `/usr/bin/env` command’s `-S` option to split the string that follows into separate arguments passed to the interpreter:

Language: Python

```
#!/usr/bin/env -S python3 -i

print("Hello, World!")
```

After the script runs, you’ll be dropped into the interactive [Python REPL](https://realpython.com/python-repl/) so that you can inspect the state of the variables, which might be helpful in post-mortem debugging.

**Note:** On some systems, the shebang line might be limited to a certain number of characters, so be sure to keep it to a reasonable length.

If you don’t want to set the shebang yourself, then you can rely on tools like [setuptools](https://setuptools.pypa.io/en/latest/) or [Poetry](https://realpython.com/dependency-management-python-poetry/) that’ll do this job for you. They let you configure convenient entry points to your project through regular functions. Alternatively, you might create a special [`__main__.py`](https://docs.python.org/3/library/__main__.html#main-py-in-python-packages) file to turn your Python module into a runnable unit, or you can [build an executable ZIP application](https://realpython.com/python-zipapp/) in Python, avoiding the need for using the shebang.

## What Are Shebang Examples?

Up to this point, you’ve used the shebang to indicate a specific version of the Python interpreter for your scripts. However, in some cases, there might be more than one interpreter capable of understanding and acting on the same code. For example, you can write a script in a way that’s compatible with Python 2 and Python 3 at the same time:

Language: Shell

```
$ /usr/bin/env python2 script.py
Hello, World!

$ /usr/bin/env python3 script.py
Hello, World!
```

The parentheses around the `print` statement in Python 2 end up being ignored, so you can safely use the `python` command without an explicit version in your shebang as long as you stay conservative with your syntax:

Language: Python

```
#!/usr/bin/env python

print("Hello, World!")
```

Heck, you can even run this code through the Perl interpreter, which also happens to have a [`print`](https://perldoc.perl.org/functions/print) function behaving in a fashion that’s similar to its Python counterpart:

Language: Perl

```
#!/usr/bin/env perl

print("Hello, World!")
```

You don’t even need to change the file extension, which the shell doesn’t care about. Just by updating the shebang line, you’ll be able run this script with Perl if you’ve installed its interpreter before:

Language: Shell

```
$ ./script.py
Hello, World!$
```

If you have [Node.js](https://nodejs.org/en/) hanging around on your computer, then you can execute JavaScript right from your terminal. Here’s an analogous `Hello, World!` script written in a language that used to be the domain of web browsers:

Language: JavaScript

```
#!/usr/bin/env node

console.log("Hello, World!")
```

With a [little bit of effort](https://nipafx.dev/scripting-java-shebang/), you can even write scripts using [Java](https://realpython.com/java-vs-python/), which isn’t technically a scripting language. Java requires compiling its high-level code to [bytecode](https://en.wikipedia.org/wiki/Bytecode) for the [Java Virtual Machine (JVM)](https://en.wikipedia.org/wiki/Java_virtual_machine), which is kind of like the Python interpreter but for binary [opcodes](https://en.wikipedia.org/wiki/Opcode).

To make the shebang possible with Java programs, you must follow these steps:

1. Make sure that the file with your Java source code does *not* have the traditional `.java` extension. You can give the file a neutral `.j` extension, for instance.

2. Run your source file through the `java` command instead of `javac`.

3. Explicitly set the Java 11 version with the `--source` switch.

Here’s a complete example of such a Java “script”:

Language: Java

```
#!/usr/bin/env -S java --source 11

public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Running this script takes noticeably longer than the analogous `Hello, World!` programs written in genuine scripting languages. That’s because of the extra compilation step, which takes place on the fly on each invocation.

**Note:** The [Spring Boot](https://spring.io/) framework can cleverly slap a shebang along with a shell script at the beginning of a binary archive with your Java classes to make a [fully executable JAR](https://docs.spring.io/spring-boot/docs/current/maven-plugin/reference/htmlsingle/#goals-repackage-parameters-details-executable) file for Unix-like systems. This makes deployment of such Java web applications a breeze!

## How Can You Use a Shebang With a Custom Interpreter in Python?

Once you’ve downloaded the interpreter, you can [install it with `pip`](https://realpython.com/what-is-pip/) into a new virtual environment:

Language: Shell

```
$ cd interpreter
$ python -m venv venv/
$ source venv/bin/activate
(venv) $ python -m pip install .
```

This should bring the custom `brainf` command into your virtual environment, which means you have an entry point to the installed Python package.

You can run this command without any arguments, in which case it’ll expect you to provide the code written in your domain-specific language through the [standard input (stdin)](https://en.wikipedia.org/wiki/Standard_streams#Standard_input_\(stdin\)), almost like a Python REPL. When you’re done typing your code, you must confirm it with Enter and then terminate the program by hitting Ctrl\+D to send an [end-of-file (EOF)](https://en.wikipedia.org/wiki/End-of-file) character:

Language: Shell

```
(venv) $ brainf
++++++[>++++++++++<-]>+++++.<++++++++++.
A

(venv) $ brainf
++++++[>++++++++++<-]>++++++.<++++++++++.
B
```

This sample piece of code results in printing the ASCII letter `A` followed by a newline character on the screen. Adding one extra plus (`+`) instruction just before the first dot (`.`) in the code above results in printing the letter `B` instead.

Alternatively, you may save your source code in a text file and provide its path as an argument to the `brainf` command:

Language: Shell

```
(venv) $ echo '++++++[>++++++++++<-]>+++++.<++++++++++.' > script.b
(venv) $ brainf script.b
A
```

The `brainf` command behaves pretty much like a Python interpreter at this point. Because of that, it’s also possible to insert an appropriate shebang at the beginning of your script and make it executable:

Language: Shell

```
(venv) $ echo '#!/usr/bin/env brainf
++++++[>++++++++++<-]>+++++.<++++++++++.' > script.b
(venv) $ chmod +x script.b
(venv) $ ./script.b
A
```

If that wasn’t exciting enough, then feel free to explore some of the more advanced sample scripts made by [Daniel B. Cristofani](http://www.hevanet.com/cristofd/), who maintains an impressive [online archive](http://brainfuck.org/) of his esoteric scripts. For example, take a look at this mind-blowing program, which draws the [Sierpiński triangle](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle) using just seven distinct instructions:

Language: Shell

```
(venv) $ cat ./scripts/sierpinski.b
#!/usr/bin/env brainf

++++++++[>+>++++<<-]>++>>+<[-[>>+<<-]+>>]>+[
    -<<<[
        ->[+[-]+>++>>>-<<]<[<]>>++++++[<<+++++>>-]+<<++.[-]<<
    ]>.>+[>>]>+
]

(venv) $ ./scripts/sierpinski.b
                               *
                              * *
                             *   *
                            * * * *
                           *       *
                          * *     * *
                         *   *   *   *
                        * * * * * * * *
                       *               *
                      * *             * *
                     *   *           *   *
                    * * * *         * * * *
                   *       *       *       *
                  * *     * *     * *     * *
                 *   *   *   *   *   *   *   *
                * * * * * * * * * * * * * * * *
               *                               *
              * *                             * *
             *   *                           *   *
            * * * *                         * * * *
           *       *                       *       *
          * *     * *                     * *     * *
         *   *   *   *                   *   *   *   *
        * * * * * * * *                 * * * * * * * *
       *               *               *               *
      * *             * *             * *             * *
     *   *           *   *           *   *           *   *
    * * * *         * * * *         * * * *         * * * *
   *       *       *       *       *       *       *       *
  * *     * *     * *     * *     * *     * *     * *     * *
 *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
```

There are a few interactive scripts as well, which can encode your input text using the [ROT-13](https://en.wikipedia.org/wiki/ROT13) cipher or calculate the factorial of the [Fibonacci sequence](https://realpython.com/fibonacci-sequence-python/). Perhaps the most impressive example you’ll ever find is an animated solution to the [Tower of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi) puzzle, which was made by [Clifford Wolf](https://clifford.at/):

Unsurprisingly, its source code is quite a bit longer than the other examples, weighing almost 55 kilobytes. It also runs very slowly, so the video above is sped up fifteen times and only shows the first few steps of the algorithm.

## What Are Best Practices for the Shebang?

To sum up, here are a few rules that you should follow to successfully use a shebang in your Python scripts:

- Remember that a shebang is only applicable to runnable scripts on Unix-like operating systems.

- When you don’t specify a shebang, your shell will attempt to interpret the script as if it were written in the corresponding shell language.

- Don’t place a shebang in plain Python modules that are only meant to be imported and not executed.

- Make sure that your script is saved in an executable file.

- Consider combining a shebang with the name-main idiom (`if __name__ == "__main__":`).

- Begin your script with a shebang line, and don’t place any other comments before it.

- Start the shebang with a `#!` sequence of characters to distinguish it from a standard comment.

- Use the `/usr/bin/env python3` command to avoid hard-coding an absolute path to any specific Python interpreter.

- Avoid using the bare `python` command unless your script is intentionally backward-compatible with Python 2\. Generally, you should use the more explicit `python3`.

- Enable the `-S` flag if you need to pass extra arguments to the interpreter—for example, `#!/usr/bin/env -S python3 -i`.

- Be cautious about the number of characters that you put into your shebang line.

Finally, ask yourself if you need to add the shebang manually or if it could be generated automatically or replaced with some higher-level abstraction by a utility in your toolchain.

## Conclusion

You know *what* a shebang is, *how* it works, and *when* you might want to include it in your Python scripts. You saw how to define a portable shebang and pass arguments to it. You also looked at some shebang examples and explored how to use a shebang with a custom interpreter written in Python. Finally, you reviewed some of the best practices for using a shebang in your scripts and learned about its shortcomings and alternatives.

**In this tutorial, you’ve learned how to:**

- Decide **when** to include the shebang in Python scripts

- Define the shebang in a **portable** way across systems

- Pass **arguments** to the command defined in a shebang

- Know the shebang’s **limitations** and some of its alternatives

- Execute scripts through a **custom interpreter** written in Python

## Frequently Asked Questions

**What is a shebang, and why is it used in Python scripts?**Show/Hide

A shebang is a special line at the start of a script that tells the operating system which interpreter to use to execute the file. You use it in Python scripts to specify the path to the Python interpreter, enabling the script to be run directly from the command line without needing to explicitly call Python.

**When should I include a shebang in my Python script?**Show/Hide

You should include a shebang in your Python script when you want to execute the script directly from the command line on Unix-like systems without explicitly typing `python` or `python3`. It’s particularly useful for scripts intended to be run as standalone programs.

**Should I include a shebang in Python modules that are meant to be imported?**Show/Hide

No, you typically don’t include a shebang in Python modules that are meant to be imported, as they’re not intended to be executed directly. Shebangs are only relevant for scripts that you execute directly.

**What’s the difference between `#!/usr/bin/python3` and `#!/usr/bin/env python3`?**Show/Hide

`#!/usr/bin/python3` specifies an absolute path to the Python interpreter, which may not be the same on all systems. `#!/usr/bin/env python3` is more portable as it uses the `env` command to locate the Python interpreter based on the user’s `PATH` environment variable, accommodating different installation paths.

**What are the best practices for writing a shebang in Python scripts?**Show/Hide

You should use `#!/usr/bin/env python3` to ensure portability across different systems. Always place the shebang on the first line of the script with no preceding comments. Combine the shebang with the name-main idiom if the script can be both imported and executed directly.
