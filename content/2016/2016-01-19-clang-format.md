Title: Formatting C code with clang-format
Date: 2016-01-19
Author: Daniel S. Standage
Category: blog
Tags: programming; c
Summary: Found a nifty tool for enforcing formatting styles for C code.

Code formatting styles: the thing we all love to hate.

![The rules are like guidelines anyway]({filename}/images/pirate-guidelines.gif)

The best formatting style is the style you don't have to think about, the style that helps you focus on the logical flow of your code.
The best formatting style is consistent and organic, providing an intuitive visual representation of program organization.

On the other hand, pedantic enforcement formatting styles can outweigh any benefits you get from it in the first place.

A lot of digital ink has been spilled and flame wars fought over this topic, and I will not belabor the point here.
Suffice it to say that I think that enforcement of code formatting style is, on the whole, a good thing.
Styles focus mostly on readability, which is a HUGE DEAL when it comes to collaborative development and maintenance of code.
Simplifying the *maintenance* of your code will save much more of your time and others' time in the future than almost any technical optimization.
Explicitly enforcing a style convention (like Python's PEP8, and associated tools `pep8` and `autopep8`) minimize conflicts between project contributors, and make it easier to integrate contributions from new contributors.
Exceptions can be considered on a per-case basis, and most enforcement tools provide mechanisms for marking code to ignore, but for the most part the rules are there to be followed for everyone's benefit.

For Python programming, the PEP8 style is the uncontested standard.
There may be others out there, but they're surely obscure and *ad hoc*.
When it comes to C and C++, however, there are many different popular styles.
There are lots of commonalities, but the differences (particularly in the placement of braces) make a huge difference in the appearance of the code.
I prefer the popular Allman style, the K&R style (also popular) is pretty reasonable, but styles like Whitesmith and Pico are just nuts!
See [this page](http://www.terminally-incoherent.com/blog/2009/04/10/the-only-correct-indent-style/) for some examples.

So in some [recent reading](https://matt.sh/howto-c) I came across a tool called `clang-format` that will automatically format C code based on your preferred style.
All of my C code formatting has previously been self-enforced, but after using `pep8` and `autopep8` on my Python code for a few years now I thought it was time to let an automated tool do the work for me.
Here's my config file (`.clang-format`).

```
BasedOnStyle: llvm
IndentWidth: 4
AllowShortFunctionsOnASingleLine: None
KeepEmptyLinesAtTheStartOfBlocks: false
BreakBeforeBraces: Allman
```

And here's the command I use to reformat a file.

```
clang-format -i -style=file src/locuspocus.c
```

Credits.

- [This post](https://matt.sh/howto-c) got me going on this.
- [This thread](http://stackoverflow.com/questions/29477654/how-to-make-clang-format-add-new-line-before-opening-brace-of-a-function) was helpful
- [This page](http://clang.llvm.org/docs/ClangFormatStyleOptions.html) has the official documentation.
- [This answer](http://stackoverflow.com/questions/25880990/clang-format-breaks-lint-annotations) describes a nice trick for disabling style checks for a code block.
