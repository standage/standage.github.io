Title: Shell pipelines in Python
Date: 2015-12-15
Author: Daniel S. Standage
Category: notebook
Tags: shell; python

The UNIX shell is an indispensible tool for project organization and data management in bioinformatics.
I spend *a lot* of time in the shell, and having picked up on a lot of time-saving techniques over the years it might just be my favorite computing environment.

The shell has its limitations, however.
Piping, the very feature that gives the shell its amazing power and flexibility, can also lead to some pretty gruesome syntax.
Debugging shell code is tough, the error handling is rudimentary, and good luck finding a good framework for automated tests.
In short, the shell is great for interactive computing and automating simple tasks, but when it comes to workflows requiring more fine-grained control, a language like Python is often a better choice.

Here I provide a Python translation of several shell commands.

## Simplest case

You don't typically get much bioinformatics work done with a single command without arguments.
Anything substantial will involve data files, parameters, and so on, that are typically specified using arguments on the command line (you haven't hard coded these in your script, have you?!?!).
But just for sake of completeness, it's very straightforward to execute shell commands this way in Python.

```bash
ls
```

The Python equivalent is as follows.

```python
subprocess.check_call('ls')
```

There is even the simpler `call` function...

```python
subprocess.call('ls')
```

...but for most situations I find the `check_call` more useful, since it will halt the Python code immediately if the subprocess returns a non-zero status.

## Command with arguments

```bash
ls -lhp
```

Commands with arguments cannot simply be dropped in to the `check_call` command as-is.
The following code will fail.

```python
subprocess.check_call('ls -lhp')
```

There are two ways you can fix this: the convenient (and wrong and insecure) way...

```python
subprocess.check_call('ls -lhp', shell=True)
```

...and The Right Way.

```python
subprocess.check_call(['ls', '-lhp'])
```

The convenience of the first method comes at the cost of security: the `shell=True` setting introduces vulnerability to [shell injections](https://security.openstack.org/guidelines/dg_use-subprocess-securely.html).
This isn't the type of thing you expect to encounter much in the research setting, but it's an important consideration nonetheless, and exceptions should be made with caution.

This example is pretty silly, since you'll probably never need to call the `ls` command from Python.
Let's do a different example you're much more likely to encounter in bioinformatics.

```bash
blastx -db /opt/ncbi/nr -query tsa.fasta \
       -evalue 1e-4 -num_threads $numthreads \
       -out tsa-vs-nr.blastx
```

The Python equivalent is as follows.

```python
command = ['blastx', '-db', '/opt/ncbi/nr', '-query', 'tsa.fasta',
           '-evalue', '1e-4', '-num_threads', numthreads,
           '-out', 'tsa-vs-nr.blastx']
subprocess.check_call(command)
```

## Redirect stdin and stdout

Many programs and commands allow you to specify input and output files as arguments, as in the `blastx` command above.
However, sometimes your only options are `stdin` and/or `stdout`.

```bash
sed s/^scaffold_/PcanScaf/ < pcan-in.gff3 > pcan-out.gff3
```

Here is the Python equivalent.

```python
with open('pcan-in.gff3', 'r') as instream, open('pcan-out.gff3', 'w') as outstream:
    subprocess.check_call(['sed', 's/^scaffold_/PcanScaf/'], stdin=instream, stdout=outstream)
```

## The main event: pipelines

Handling input and output for single commands is great and all, but the real power of the shell is piping commands together like so.

```bash
grep -v $'\tintron\t' loci.gff3 \
    | pmrna --locus --accession --map=map.txt \
    | canon-gff3 --outfile=locus.mrnas.gff3 
```

Unless we want to introduce security vulnerabilities, we cannot simply run these command with a single `check_call` command.
For this use case, we want to use the `Popen` constructor and the `communicate` method.

```python
grepproc = subprocess.Popen(['grep', '-v', '\tintron\t', 'loci.gff3'],
                             stdout=subprocess.PIPE)
pmrnaproc = subprocess.Popen(['pmrna', '--locus', '--accession', '--map=map.txt'],
                             stdin=grepproc.stdout,
                             stdout=subprocess.PIPE)
canonproc = subprocess.Popen(['canon-gff3', '--outfile=locus.mrnas.gff3'],
                             stdin=pmrnaproc.stdout)
canonproc.communicate()
```

If needed, it is trivial to capture the terminal output like so.

```python
grepproc = subprocess.Popen(['grep', '-v', '\tintron\t', 'loci.gff3'],
                             stdout=subprocess.PIPE)
pmrnaproc = subprocess.Popen(['pmrna', '--locus', '--accession', '--map=map.txt'],
                             stdin=grepproc.stdout,
                             stdout=subprocess.PIPE)
canonproc = subprocess.Popen(['canon-gff3', '--outfile=locus.mrnas.gff3'],
                             stdin=pmrnaproc.stdout,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
stdout, stderr = canonproc.communicate()
for line in stderr.split('\t'):
    # process the terminal warnings
```

## Coda

That's it!

Python's `subprocess` module is pretty powerful, and allows even slicker interactions with the shell, such as printing text to a pipeline of shell commands.
However, writing to and reading from a pipeline simultaneously can get tricky and is prone to deadlocks.
I will not cover this here, but the Internet is full of blog posts and StackOverflow threads discussing the intricacies of the `subprocess` for these more complicated use cases.
