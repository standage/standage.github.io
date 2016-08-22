Title: Reproducible variant calling is possible with randomized algorithms
Date: 2016-08-22
Author: Daniel S. Standage
Category: blog
Tags: random; variant calling

This morning I read [On genomic repeats and reproducibility](http://dx.doi.org/10.1093/bioinformatics/btw139) by Can Firtina and Can Alkan.
The paper discusses two notable observations regarding calling genomic variants.

1. Some sequence read aligners are not deterministic, and shuffling the order of the reads can result in different alignments.
2. Some variant callers are not deterministic, and will report a different set of variants if an analysis is repeated on the same set of alignments (i.e. the same BAM file).

## Non-deterministic read mapping

The first observation wasn't all that surprising to me.
I remember as a graduate student hearing anecdotally that genome assembly algorithms are (or can be) sensitive to read order.
And anything that involves pseudorandom number generators will by definition produce results with technical variation.

The authors analyzed four read alignment tools: Bowtie2, RazerS3, mrFAST, and BWA-MEM.
Based on a sample of 1 million reads, they confirmed that Bowtie2<sup>‡</sup> and mrFAST produce identical alignments when the read order is shuffled.
BWA-MEM, however, reports multimapped reads differently, and the location reported for each multimapped read depends on its order.
Oddly enough, the the authors didn't report RazerS3 results for this analysis, although in the discussion section they describe RazerS3 as a deterministic mapper.

## Non-deterministic variant calling

The second observation was quite intriguing to me.
The authors evaluated four variant callers—HaplotypeCaller, Freebayes, Platypus, and SAMtools—and reported the extent to which differences in read alignments due to read order affect variant calling.
More interestingly, though, was the observation that HaplotypeCaller would produce different results when run multiple times on the same input file.
Apparently, HaplotypeCaller uses a random sampling of the training data for sake of efficiency, and different random samples will result in different variants being filtered out by quality control before final results are reported.

## Discussion and recommendations

In the discussion section, the authors recommend using a deterministic read mapper and variant caller for sake of reproducibility.
However, I want to contend with their claim that *Full reproducibility could only be achieved through using deterministic methods.*
The behavior of random number generators can be controlled by initializing the generator with a "seed" (see [this post from my old blog](https://biowize.wordpress.com/2015/08/05/reproducible-software-behavior-with-random-seeds/)), and I think I'm safe in saying that random seeds are general knowledge.
Somebody with enough technical chops to implement a read aligner will almost certainly be familiar with random seeds.
Therefore, a randomized algorithm can indeed be fully reproducible if the following conditions are met.

- The algorithm allows (but does not necessarily require) the user to specify a seed to initialize the random number generator.
- The algorithm reports the seed used to initialize the random number generator, whether specified by the user or not.
- The random seed(s) used for an analysis are disclosed whenever results are published or shared.

Unfortunately, BWA-MEM does not allow users to specify random seeds, so the authors are correct *in this case* that full reproducibility is not possible with the aligner (I'm not familiar with HaplotypeCaller, so I won't comment on that).
However, the authors themselves admit that in general "randomized algorithms may achieve better accuracy in practice."
So rather than recommending that fellow scientists avoid a tool or class of tools entirely for the sake of reproducibility, I contend that we should recommend that randomized algorithms follow these simple steps to facilitate complete reproducibility.
Perhaps I'll even open a pull request for BWA-MEM myself, although with 30 open pull requests I don't have faith it would be merged any time soon.

----------

<sup>‡</sup>The authors reported anecdotal evidence, almost as an afterthought, that changing read names will affect the results reported by Bowtie2, even if changing the read order does not.
