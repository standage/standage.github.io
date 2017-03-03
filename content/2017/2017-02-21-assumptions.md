Title: asdf
Date: 2017-02-21
Author: Daniel S. Standage
Category: blog
Tags: introspective; assumptions
Status: draft

Last week, I had a breakthrough in my primary research project.
Most of my recent progress has come from finding and squashing bugs in the software I'm writing for the project.
But this one was different.
It came from realizing that one of the foundational assumptions I took for granted was invalid in the context of my project.

The [khmer software library](https://khmer.readthedocs.io), on which this project relies heavily, provides (among other things) memory-efficient data structures that give *approximate* answers to k-mer abundance queries for large DNA sequence data sets.
These data structures make a trade-off between accuracy and space efficiency: reducing the amount of memory used by the data structure makes some computations more tractable, but also results in some erroneously inflated k-mer abundances.
The number of incorrect k-mer abundances and the extent which they are incorrect is captured by the *false positive rate (FPR)*, which depends on the number of collisions in the data structure.
Although most khmer scripts will complain loudly about any expected FPR above 0.2, [the original khmer paper on the topic](http://dx.doi.org/10.1371/journal.pone.0101271) demonstrated that an FPR of up to ≈0.8 had little measurable ill effect on the accuracy of downstream analysis.
My impression from this paper and from conversations with the paper's senior author was that with an FPR around 0.1-0.2, the software would report inflated abundances for a non-trivial portion of k-mers, but that the magnitude of error per k-mer would be pretty small (for example, reporting 1 when true abundance is 0, or reporting 14 when true abundance is 12).

So here I was, processing a large human genome data set and operating with an FPR of about 0.1, when I began seeing hugely inflated k-mer abundances: reporting 15 or 20 or 25 when the true abundance was 1.
At first, I wasn't even sure this wasn't a fluke, and the size of the data set made re-running the analysis (even at the current testing stage) frustratingly slow<sup>1</sup>.
Once I confirmed the errors were deterministic, I started hunting for software bugs.
Several of us in the lab had been actively updating various internals of the khmer software, and I suspected some of these changes might be a factor.
We did catch a few bugs in this hunt (of course, they're everywhere in the software world), but alas even after fixing these some drastically inflated k-mer abundances remained.

The breakthrough came when, after a lot of code review and testing on smaller data sets, I decided to compute exact k-mer abundances for the data set (using [Jellyfish](http://www.genome.umd.edu/jellyfish.html)) and compare these to the approximate k-mer abundances reported by khmer<sup>2</sup>.
I observed highly inflated k-mer abundances at FPRs of 0.2, 0.1, 0.05, and even lower.
It wasn't until I achieved extremely low FPRs (≈0.00001) with a small data set that the problem went completely away.

So, what gives?
Had I been mislead?
Was the original khmer paper linked above incorrect?

In highsight it all makes sense.
The operations described in the paper involve median k-mer abundances aggregated over an entire read, in which context it's extremely unlikely that more than 1 or 2 k-mers will have a drastically inflated abundance, even with high FPRs.
On the other hand, my method considers each individual k-mer independently, in which context highly inflated abundances don't get naturally filtered out, even at lower FPRs.

This simple exercise convinced me that my intuition was misleading me, and I had to revise my assumptions and account for this fact.
And fortunately the solution to the problem of highly inflated k-mer abundances was straightforward once it was acknowledged as a feature and not a bug.

All of this has me thinking more generally about the role assumptions and intuition play in research.
Effective work in a particular area of research requires solid grounding in some fundamental concepts, but some things have to be taken for granted.
There is insufficient time to personally re-develop from scratch the collective theory and findings of an entire field of inquiry, and so

To be effective in a particular area of research, one needs solid grounding with some fundamental concepts and take some things for granted.


----------

<sup>1</sup>By now I've learned the value of rapid iterative testing with small data sets, but only after many painful mistakes over many years.

<sup>2</sup>You can see how it all unfolded [here](https://github.com/dib-lab/khmer/issues/1619).

<sup>3</sup>
