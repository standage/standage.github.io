Title: A snake in the pipes!
Date: 2018-12-26
Author: Daniel S. Standage
Category: blog
Tags: snakemake; pipes; python
Summary: A few comments on the new "pipe" output flag in Snakemake.


Recently while consulting the [Snakemake documentation](https://snakemake.readthedocs.io) (a common occurrence for me these days) I noticed a [new feature](https://snakemake.readthedocs.io/en/v5.4.0/snakefiles/rules.html#piped-output) I had never encountered before.

> *From Snakemake 5.0 on, it is possible to mark output files as pipes, via the `pipe` flag...If an output file is marked to be a pipe, then Snakemake will first create a [named pipe](https://en.wikipedia.org/wiki/Named_pipe) with the given name and then execute the creating job simultaneously with the consuming job...*

Named pipes are much less commonly used than the pipe (or `|`) character in UNIX land, but they serve the same purpose: rather than writing the output of one command to the terminal or to file on disk, send it to another command. The difference is that named pipes have a user-specified filename on the file system. But if you have `command1` printing to a named pipe and `command2` reading from it, it will act just as if you had executed `command1 | command2`.

Since discovering this new feature, I've tried it in a few workflows. It has proven useful in a couple of scenarios.

- **Streaming non-`stdout` output**: Some programs do not provide the option to write output to `stdout`, which makes it more difficult to execute in a streaming fashion. However, if you mark a rule's output files with `pipe` and then provide these as input to another rule, the data will be passed from rule to rule via the named pipes and will never touch disk.
- **Breaking up complex pipelines**: Snakemake will happily execute shell commands with several subcommands piped together. But when each command has a handful of parameters, configuring this pipeline in a single rule can become cumbersome. I've found in some cases that things are much cleaner and more decipherable when the pipeline is split across multiple rules using `pipe`'d files as data intermediates. I've successfully connected 3 commands using pipe intermediates, so presumable there should be no issues in piping together any arbitrary number of rules with this mechanism.

What do you use the `pipe` flag for?