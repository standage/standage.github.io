Title: Genomic interval notations: personal preference, or a clear winner?
Date: 2016-02-11
Author: Daniel S. Standage
Category: blog
Tags: annotation; gff3; coordinates; python

Intervals are one of the most common data abstractions used in genome informatics, along with strings and graphs.
DNA has an intricate dynamic three-dimensional structure, but for many bioinformatics problems we can get away with ignoring this level of detail and representing the molecule instead as a static linear sequence of symbols.
Genomic features—such as genes or transposable elements—are then annotated as subsequences of the larger complete sequence, much like an interval on a discrete number line.

The most popular data formats for encoding sequence annotations ([GFF3](http://www.sequenceontology.org/gff3.shtml), [BED](https://genome.ucsc.edu/FAQ/FAQformat.html#format1), [GTF](http://mblab.wustl.edu/GTF22.html)) all use a very similar convention.
The location of a feature is designated by three values: some kind of *label* or *identifier* specifying the precise molecule on which the feature resides (such as *Chr1* or *Scaff17468*), and two integers representing the start and end of the genomic interval.
These values are stored in tab-delimited plain text, along with various other values and metadata.

There are, however, some substantial differences between "the big three" formats.
BED and GTF were designed for very specific use cases (visualization and gene prediction, respectively), whereas GFF3 was designed as a generalized solution for genome annotation.
BED allows for a single level of feature decomposition (a feature can be broken up into blocks), while GTF supports two levels (exons can be grouped by `transcript_id`, and transcripts grouped by `gene_id`), and GFF3 supports an arbitrary number of levels (parent/child relationships defined by `ID` and `Parent` attributes specify a directed acyclic graph of features).

Perhaps the most important difference, though, is the *notation* these formats use to encode genomic intervals: that is, which two integers are used to specify the location of the interval?
GFF3 and GTF both inherited, through their common heritage with older GFF variants, 1-based indexing and closed interval notation.
BED on the other hand uses 0-based indexing and *half-closed* interval notation.
Consider the DNA sequence below.

```
        1    2    3    4    5    6    7      <-- GFF3 style
        |    |    |    |    |    |    |
        G    A    T    T    A    C    A
        |    |    |    |    |    |    |
        0    1    2    3    4    5    6      <-- BED style
```

Using 1-based indexing and closed interval notation *a la* GFF3, the interval containing the subsequence `ATTA` would be represented as `[2, 5]`.
With BED's 0-based indexing and half-closed interval notation, the same subsequence would be represented as `[1, 5)`.

Confused yet?
Don't worry: off-by-one errors with interval arithmetic are very common in bioinformatics, striking newcomers and old-timers alike.

An alternative and useful way to conceptualize the BED-style notation is to shift the indices slightly so that they correspond to the spaces *between* nucleotides, rather than the nucleotides themselves.
Then, the two integers defining an interval are the ones that bound the nucleotides in question.

```
        G    A    T    T    A    C    A
     |    |    |    |    |    |    |    |
     0    1    2    3    4    5    6    7
```

So, the big question is: are there any compelling reasons to choose one notation over the other?
Or is it simply a matter of preference?

Until very recently, I have been of the opinion that it's primarily a matter of preference.
More generally, I have long favored the GFF3 format over any of the alternatives.
Leveraging the [Sequence Ontology](http://www.sequenceontology.org) and supporting parent/child relationships provides a more flexible, comprehensive, and consistent solution for genome annotation than any of GFF3's tab-delimited relatives.
And counting nucleotides starting from 1 has never felt unnatural, at least from the perspective of a biologist.

But I'm now convinced that 0-based half-closed interval notation is indisputably superior to 1-based closed interval notation.
Consider the following.

- One of the most widely cited benefits is that interval length calculations are much simpler: `end - start` rather than `end - start + 1`.
  Interval overlap calculations enjoy the same benefit: `min(a.end, b.end) - max(a.start, b.start)` instead of `min(a.end, b.end) - max(a.start, b.start) + 1`.
  Although the majority of bioinformatics software likely has very little to gain *performance wise* by simplifying calculations at this level, there is a lot to be gained by making *code* cleaner, simpler, and easier to read.
  It's important to optimize code for human comprehension whenever possible, and removing superfluous `+1`s and `-1`s can go a long way in this regard.
- When taking the reverse complement of a sequence, the interval `[start, end)` becomes `[length - end, length - start)`, rather than `[length - end + 1, length - start + 1)`.
  And honestly, the list of cases where proper notation makes these pesky `+1`s and `-1`s disappear keeps going and going, so I'll just leave it at that.
- Another compelling argument is that most programming languages utilize 0-based indexing, so using a 1-based notation for annotations requires care on the part of the programmer to make the ajustments themself when, for example, accessing a DNA subsequence stored as a string.
  The 0-based half-open notation leads to very clean C-style loops (`for(int i = start; i < end; ++)`), and ranges and slices in Python use the same notation.
  Finally, renowned computer scientist Edsger Dijkstra expounded a [simple yet elegant defense](http://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html) of this interval notation, citing empirical evidence that its use leads to fewer programming errors than any alternative notation.
- When splitting a sequence into, for example, 100kb chunks, the 0-based half-closed notation gives much cleaner-looking boundaries: `[100000, 200000), [200000, 300000)` instead of `[100001, 200000], [200001, 300000]` or `[100000, 199999], [200000, 299999]`.

As persuasive as this list is, one still might claim that all of these points (perhaps with the exception of Dijkstra's data-supported claims) still fall within the realm of opinion.
But where the 1-based closed interval indexing really falls apart is in the encoding of **zero-length features**.
GFF3 simply has no unambiguous notation for specifying that, for example, an insertion site resides between the 50th and 51st nucleotide of a sequence.
To be clear, the GFF3 specification explicitly addresses this case.

> For zero-length features, such as insertion sites, start equals end and the implied site is to the right of the indicated base in the direction of the landmark.

But how is one to distinguish zero-length features from one-length features, which must also be encoded as `start = end`?
There is no way to distinguish between these two cases without looking for additional contextual hints, which (as experience shows) come in about as many flavors as there are bioinformaticians.

So although I still prefer GFF3 to the competitors, I now acknowledge its use of 1-based closed intervals as its biggest weakness.

Would it be possible to change GFF3?

I'm afraid that interval notation is too central a feature to change with an incremental update, and would likely require a new major release of the specification.
With lots of legacy code (and modern code!) depending on GFF3, I'm not sure the world is quite ready for GFF4.

----

Hat tip to [this thread](https://github.com/ga4gh/schemas/pull/49#issuecomment-44520397) for the insightful discussion and link to the Dijkstra transcript, and to [this post](https://www.biostars.org/p/176583/#176590) for suggesting that zero-based indices point *between* nucleotides.
