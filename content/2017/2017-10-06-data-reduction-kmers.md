Title: Information content versus data volume and <em>k</em>-mer counting accuracy
Date: 2017-10-06
Author: Daniel S. Standage
Category: blog
Tags: kevlar; variant discovery; error correction

Keeping track of *k*-mers for simple operations has become a fundamental component of many bioinformatics techniques.
Two common operations on *k*-mers include set membership queries ("is *k*-mer *X* present in data set *Y*?") and abundance queries ("how many times does *k*-mer *X* occur in data set *Y*").
Several probabilistic data structures have been developed to support these types of operations in a memory-efficient manner, and this is still [an active area of research](https://doi.org/10.1093/bioinformatics/btx636).

In my recent work with variant discovery, I make extensive use of the Count-min sketch implementation available from the [khmer library](http://dx.doi.org/10.21105/joss.00272).
This data structure is very similar to a Bloom filter, using a fixed amount of memory and multiple hash functions to keep track of *k*-mer abundances.
Because the memory is fixed and collisions are left intentionally unresolved, the accuracy of these data structures declines as they approach full capacity.
The precise accuracy of depends on the number of unique *k*-mers in the data set being analyzed and the amount of space allocated to the data structure.

I was recently reminded of the fact that "data does not equal information" in a way that should have been obvious to me from the beginning.
One of the big challenges with doing variant discovery on human genome sized data sets is the sheer volume of data, where whole genome sequencing to about 30x coverage requires more than 100 Gb of raw compressed data per sample.
Accordingly, I am always looking for things I can do to reduce the data to a more manageable size, both to facilitate my own research progress and to make the methods I'm developing more generally useful.

One of the first ideas I and my colleagues bounced around was to discard all reads that matched the reference genome perfectly before counting *k*-mers.
Preliminary results looked deceptively promising, with around 80% of the reads being discarded from each sample.
This certainly reduced the amount of time required to iterate over the reads in subsequent steps of the workflow.
However, this did very little to reduce the *information content* of each sample.
Recall that the accuracy of the Count-min sketch is a function of the number of distinct *k*-mers and the amount of memory allocated.
Put another way, the only way reduce memory consumption while keeping the accuracy constant is to also reduce the number of distinct *k*-mers being stored.

As it turns out, discarding reads that match the reference genome perfectly does very little to reduce the number of unique *k*-mers in a data set.
*k*-mers associated with sequencing errors typically outnumber true *k*-mers, and this approach does nothing to address these erroneous *k*-mers.
And despite discarding such a large proportion of the reads, the majority of the true *k*-mers were still present in the remaining reads, many of which we can presume had only a single nucleotide substitution error.

For a long time I was resistant to the idea of error correction, because of the resources and the additional processing time that this would require.
But had I been thinking in terms of *information content* instead of *data volume*, this is something I would have investigated much earlier.
Indeed, running the [Lighter](https://doi.org/10.1186/s13059-014-0509-9) error correction tool on one of my data sets resulted in a 60% reduction in the number of unique *k*-mers in each sample.
I was able to cut the memory I had devoted to *k*-mer counting in half and achieve even better accuracy than before.
And it turns out my concerns about resources and processing time were unfounded: with 8 threads Lighter required only 90 minutes of runtime and less than 16 GB of RAM, which isn't asking too much of commodity bioinformatics hardware these days.

Now I need to verify that running error correction doesn't introduce problems later on for variant discovery, but given that error correction tools are usually quite conservative in my experience, I don't anticipate this will be much of a problem.
