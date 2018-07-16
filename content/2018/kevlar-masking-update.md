Title: Improvements from applying filters at k-mer counting time in kevlar
Date: 2018-07-16
Author: Daniel S. Standage
Category: blog
Tags: kevlar

One of the fundamental insights of the [kevlar *de novo* variant caller](https://kevlar.readthedocs.io) is the framing of the variant discovery problem as a search for novel k-mers.
In this case, "novel" means abundant in the focal sample and effectively absent from all control samples.
In the early stages of creating kevlar, it quickly became clear that many k-mers satisfying these simple threshold criteria are not associated with a *de novo* variants.
Some come from sample-specific contamination (bacteria, Illumina adapters, etc.), while others derive from alleles present in the reference genome but absent from the controls due to a combination of genetic variation and chance fluctuations in sequencing coverage.
Thus, we introduced filters early on to weed out uninteresting k-mers to focus on those more likely to be associated with *de novo* variants.

Up until very recently, the kevlar workflow applied k-mer filters after the initial pass over the data to find novel k-mers.
Recently I began testing an alternative approach: apply the filters during the initial k-mer counting (enabled by [this code update](https://github.com/dib-lab/kevlar/pull/277)).
Using this strategy, if a k-mer is present in the reference genome or is contaminant in origin, its abundance is not tracked for later reference.
The direct result is that these k-mers are not declared novel in the first pass over the data, and thus the filters do not need to be applied *post facto*.

I've noticed two additional secondary benefits to this approach.
First is a modest improvement in kevlar's memory efficiency.
Since k-mers present in the reference genome and in contaminant databases aren't tracked at all, accurate k-mer counts are possible in a smaller amount of memory.
The second is a substantial improvement (>2x decrease) in runtime during the novel k-mer identification step.
I don't know how much of this is due to better cache locality from the smaller k-mer counters versus fewer lookups overall—I'm guessing the latter is the more influential factor.
In any case, this has been the most computationally expensive part of the kevlar workflow overall, and it's encouraging to see improvements of this magnitude.

Initially I was worried that this approach might require k-mer counts to be recomputed for the final variant likelihood calculations.
However, the likelihood scores are based exclusively on the abundances of the alternate allele k-mers which should not be affected by the filters.
Reference allele k-mers *are* considered when computing the error rate, but this only requires abundance/copy number of these k-mers in the reference assembly, not their per-sample abundance.

In summary, this modest and fairly obvious (in retrospect!) new approach looks like a win-win all around.

- Instead of applying k-mer filters in Python land *post facto*, they are applied *a priori* during k-mer counting using efficient procedures implemented entirely in C++.
- As a result, less memory is needed to get accurate k-mer counts for each sample.
- Also, the task of identifying novel k-mers is sped up substantially, probably due to a decrease in k-mer abundance queries and (to a lesser extent) better cache locality.
