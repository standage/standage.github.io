Title: Filter stderr while piping in UNIX
Date: 2015-12-14
Author: Daniel S. Standage
Category: noteboop
Tags: shell

I've written before about [process substitutions in the shell](https://biowize.wordpress.com/2013/10/11/commands-in-place-of-program-arguments/).
This has become a core technique I use almost on a daily basis in my data work in the shell.
It has many uses, but I want to highlight a particular one here.

## Use case

Imagine you have a shell script with the following commands

```bash
first_command --arg1=foo --arg2=bar --flag3 infile.txt \
    | second_command one two three \
    | third_command --abc xyz \
    > outfile.txt
```

Each of these commands will print to stderr in case of a warning or an error.
However, `second_command` prints an irrelevant warning (`cannot find "foo"`) message over and over again, filling up the terminal with thousands of lines of noise and making it more difficult to find warnings or error messages we might actually care about.
How can we filter the stderr of `second_command` so that the `cannot find "foo"` messages are ignored, but all other messages still show up?

## Solution

Process substitutions can be used not only as pseudo input files using the `<()` syntax, but also as pseudo output files using the `>()` syntax.
If we redirect a program's output to a process, we can then filter the data within that process, like so.

```bash
some_program > >(sort | uniq -c)
```

Extending this to stderr requires only two changes.
First, we replace `>` with `2>` so that we are redirecting the correct output stream.

```bash
some_program 2> >(sort | uniq -c)
```

Secondly, we add `1>&2` to the end of the process so that its stdout is redirected back to stderr, which is where the data was intended to go in the first place (cue Ghostbusters quote about not crossing the streams).

```bash
some_program 2> >(sort | uniq -c 1>&2)
```

Putting this all together and going back to our original use case, we can remove the unwanted `cannot find "foo"` messages from our terminal like so.

```bash
first_command --arg1=foo --arg2=bar --flag3 infile.txt \
    | second_command one two three 2> >(grep 'cannot find "foo"' 1>&2) \
    | third_command --abc xyz \
    > outfile.txt
```

That's it!