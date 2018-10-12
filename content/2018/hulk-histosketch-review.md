Title: A brief review of HULK and histosketch
Date: 2018-10-12
Author: Daniel S. Standage
Category: blog
Tags: sketching; metagenomics; journal club

About a month ago, I was intrigued to see a bit of Twitter activity around a new bioRxiv preprint.
The [manuscript](https://www.biorxiv.org/content/early/2018/09/04/408070) describes [HULK](https://github.com/will-rowe/hulk), a new bioinformatics tool that implements some useful comparison metrics and operations for analyzing (meta)genomes.
HULK is based on a new algorithm called histogram sketching (HistoSketch for short), following the trend of related sketching algorithms (HyperLogLog, CountMin, MinHash, etc.) that have steadily captured the collective interest of the genome informatics community over the last several years.

I recently led a journal club to discuss the histogram sketching algorithm and to discuss the claims and results discussed in the HULK paper.
I'm posting some notes from the journal club here mostly for my own sake, but I'd be elated if they happen to be insightful to anyone else who is interested in learning more about the tool or the topic.

**tl;dr**: While a couple of the claims in the manuscript should be qualified, HULK's treatment of *k*-mer abundances and mismatched data set sizes is indeed novel, and incremental sketching + machine learning = awesome!


## Background

The terms *sketch* and *sketching algorithm* seem to be used fairly frequently (at least over the last several years), but surprisingly I was unable to find an authoritative definition for them.
My understanding is that a sketch is a compact approximation of some characteristic of a large data set, just as a pencil sketch approximates a photograph or a painting.
Different kinds of sketches approximate different characteristics of the data set: the HyperLogLog approximates the cardinality (size, or number of distinct elements) of the dataset; the Bloom filter can provide approximate membership queries ("*Is this element in the data set?*"); the CountMin sketch provides approximate frequency queries ("*How many times does this element occur in the data set?*"); and the MinHash sketch selects a representative sample of set elements to...well, represent the data set! The number of shared elements between two MinHash sketches, it turns out, is an excellent proxy for the "distance" or similarity between the data sets.

While all of these sketches have useful bioinformatics applications, I think it's safe to say that MinHash in particular is making big splashes in the genomics community.
MinHash sketches require a negligible amount of storage, can be computed extremely quickly, and permit similarity calculations that can enable or improve metagenome analysis, genome assembly, sample ID, and more.
In addition to the [trend-setting Mash paper](https://doi.org/10.1186/s13059-016-0997-x) and [corresponding tool](https://github.com/marbl/mash), MinHash sketching has been re-implemented in [sourmash](https://github.com/dib-lab/sourmash) and [Finch](https://github.com/onecodex/finch-rs) (and probably others) to facilitate research into additional (meta)genomics applications of this class of algorithms.


## Histogram sketching

The histogram sketching algorithm was first published in the [proceedings of the 2017 IEEE data mining conference](https://doi.org/10.1109/ICDM.2017.64).
Like most sketching algorithms, it was not originally developed with biology applications in mind.
The authors sought a way to efficiently compare and classify *continuous streams* of histogram data, such as from customer visits to a restaurant or other business.
In particular, the authors wanted to account for *concept drift*, in which "the underlying distribution of a streaming histogram changes over time in unforseen ways."

The authors of this work developed HistoSketch to address these needs.
A HistoSketch is similar to MinHash in that it stores a small, fixed number of histogram elements.
A weight is assigned to each histogram element in the sketch using an approach termed *Consistent Weighted Sampling (CWS)*.
The math that defines CWS is a bit above my pay grade, but it endows HistoSketch with some of the properties that sets it apart from alternative sketching algorithms.
In particular, HistoSketch is a *similarity-preserving* data structure while CountMin, for example, is not<sup>‡</sup>.
And while MinHash *is* similarity-preserving, it only accounts for the elements of the data set and not the histogram of the elements' frequencies.
HistoSketch defines a similarity-preserving data structure that is frequency-sensitive, capturing the "best of both worlds" while also elegantly addressing the issue of concept drift that other algorithms do not account for.

## HULK

Which brings us to the main event.
HULK is a new bioinformatics tool that implements histogram sketching in the context of DNA sequence data.
HULK computes a histosketch of the *k*-mer spectrum from a stream of data in Fastq or Fasta format.
The histosketches computed by HULK can be used for similarity calculations based on the weighted variant of the Jaccard distance metric employed by Mash and company.
Additionally, the authors demonstrate that histosketches can be integrated with machine learning models to classify microbiome samples based on the body site from which they were collected.
The experiments described in the manuscript demonstrate that even incomplete/intermediate sketches of a data stream are sufficient to cluster and classify microbiome samples.

HistoSketch and HULK are clearly a promising development in this area, but the million dollar question is what precise advantages they provide over alternative algorithms.
The authors of the HULK preprint claim that histosketch comes with the following advantages.

- speed
- streaming support (incremental sketching)
- robustness for comparing samples of significantly different sizes
- sensitivity to *k*-mer frequencies
- machine learning integration
- elegant handling of "concept drift"

Based on a careful study of the manuscript, a bit of email correspondence with the primary author, a partial code review, and discussion in our journal club, I'd like to provide my assessment of each of these claims.

### Speed

The superior speed of HULK is not something that was emphasized *too much* in the preprint.
It was mentioned in passing in the manuscript, as well as on the README included in the source code distribution.
It's not clear whether HULK's performance is due to characteristics of the histogram sketching algorithm or the language of implementation, Go.

The only hard data offered in the manuscript is a comparison of HULK and [Simka](https://github.com/GATB/simka).
HULK positively spanks Simka with an order-of-magnitude improvement in runtime while acheiving comparable (slightly better) accuracy.
Is this a good speed benchmark? I'm not sure.
I wasn't familiar with Simka prior to reading the HULK preprint, although that may reflect a personal deficiency more than anything else.
However, I do think it would have been appropriate to compare against Mash at the very least, as the trend-setter in sketch-based comparisons of metagenomes.

### Streaming support (incremental sketching)

Much is made of histogram sketching being a streaming algorithm both in the original HistoSketch paper and in the HULK preprint.
At first, this didn't seem like a helpful distinction since there is nothing preventing MinHash or CountMin (for example) from sketching data streams just as easily.
When and how to output the sketch is an implementation decision, not a limitation of the algorithm.

That said, I am unaware of any other sketching tools that output snapshots of a sketch at intermediate intervals while processing the data stream.
This is a Big Deal.
The kind of *incremental sketching* HULK supports opens up a new realm of possibilities for dynamic control of the entire pipeline, from sequencing to sketching to analysis.
And unless I'm mistaken, the HULK preprint was also the first bioinformatics study to investigate the accuracy of sketches computed from partial data streams.

### Robustness for relative data set size

There are known issues when using MinHash to compare data sets of significantly different size.
The HULK preprint references the issue twice: one brief mention in the Introduction section...

> *there remain limitations to standard MinHash techniques; such as the loss of k-mer frequency information and the impact of relative set size on Jaccard similarity estimates.*

...and another in the Discussion section.

> *In particular, it addresses the main limitations of traditional MinHash for certain microbiome analyses.
These being: (i) histogram sketching is not impacted by mismatched set size and (ii), histogram sketching accounts for weighted sets (e.g. k-mer frequency).*

This topic is discussed in depth [in this preprint](https://doi.org/10.1101/184150) and by the Mash authors themselves in [a blog post](https://genomeinformatics.github.io/mash-screen/), both posted about a year ago.
HULK claims to be the first tool to solve this problem for (meta)genome analytics.
I don't think this is true...as an unqualified statement at least.
Mash is capable of performing "containment" queries with `mash screen` as described in the blog post above.
And while Mash doesn't support similarity calculations for metagenomes of mismatched size, sourmash does with its `--scaled` mode.
In both cases, a sampling rate is defined, so a fixed sketch size can no longer be guarantee like it is with HULK.

How exactly *is* HistoSketch robust to differences in relative set sizes? I'm actually not clear on this.
The only discussion of mismatched set sizes I could find in the manuscript are the two shown above.
It's possible there's more information in there for an astute reader who can read between the lines, but I think it would improve the manuscript considerably if the authors clarified this point.

But even giving the authors the benefit of the doubt, I still think it's a bit of a stretch to claim that HULK is the first tool to address mismatched data set sizes.
I *would* fully agree with the sentiment that HistoSketch is the first sketching algorithm that treats comparison of data sets of mismatched size *as a primary algorithm design consideration* rather than a bonus feature or alternative mode.
It's admittedly a subtle point, but an important one in my opinion.

### Sensitivity to *k*-mer frequencies

The HULK authors claim that standard MinHash tools do not take into account *k*-mer frequency information.
I feel like this statement also needs qualification.
It is true that Mash ignores *k*-mer abundance completely, but sourmash has supported a `--track-abundance` mode for some time.
Assuming all sketches in question were computed with `--track-abundance`, the distance calculations with `sourmash compare` integrate the *k*-mer abundance information.

However, even in the case of sourmash, *k*-mer frequencies don't have any influence on which *k*-mers are chosen to occupy the sketch, whereas the *Consistent Weighted Sampling* scheme employed in histosketching is sensitive to *k*-mer frequencies.
Like the previous point, I'd suggest it's more accurate to say that HistoSketch is novel in including this as a primary design consideration rather than an afterthought.

### Machine learning integration

The authors don't claim that this is the only sketching algorithm that can be integrated with machine learning downstream, but HULK is the first to demonstrate it in the context of bioinformatics.
HULK's support for incremental sketching is also relevant here, as successful classification of a data stream (above some confidence threshold) can terminate processing early.

### Elegant handling of *concept drift*

*Concept drift* refers to the phenomenon that occurs when a continuous data stream measures qualitatively different things at different points in time.
By "gradually forgetting" earlier observations, more recent observations can carry more influence and provide a more accurate reflection of what is currently being measured.

I can't say I fully grok the CWS scheme used by HistoSketch, but the CWS-computed weights do provide a simple and elegant mechanism for handling concept drift in a data stream.
With each new observation, the existing weights are scaled so that they are slightly more likely to be replaced by an updated histogram element.
Over time, these slight adjustments accumulate and older observations are replaced with newer observations.

So what is the relevance of this to DNA sequence data? I could imagine a few scenarios where this approach might be useful.

- arrays of sensors continuously collecting sequence data from different locations to profile soil, marine, or human microbiome composition
- stategically placed sensors continuously monitoring for the presence of pathogens
- a strategy for dynamic control of the DNA sequencer that is sensitive to what has been sequenced "recently" (for some value of "recently")

In each case, changes to a sensor's environment over time would muddle its signal without accounting for shifts in what is being observed.

I don't think that DNA sequencing technology has quite "made it" yet to the extent needed to make these types of strategy feasible.
And it's hard to estimate when the tech might be ready.
But I think the HULK authors make a great contribution here in helping us imagine what might be possible.

## Summary

In conclusion, I think HULK and HistoSketch are great contributions to this area of research.
It's notable that HistoSketch accounts for *k*-mer frequency and mismatched data set sizes as primary design considerations.
HULK's demonstration that histosketches are suitable substrates for machine learning approaches is also promising.


I *do* think some of the claims the authors make in the preprint are weakly supported or need to be qualified.
But hey, it's a preprint! Hopefully the HULK authors get some constructive feedback from multiple sources so that their final paper is that much stronger.
In the mean time, I'll be watching [the HULK repo](https://github.com/will-rowe/hulk) closely.

----------

<sup>‡</sup>I'm not exactly sure why CountMin is not similarity-preserving, and the authors offer no explanation.
Perhaps it's related to the fact that CountMin retains all data points and MinHash samples a respresentative subset of data points.
