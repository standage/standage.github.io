Title: Group meeting feedback
Date: 2015-11-18
Author: Daniel S. Standage
Category: notebook
Tags: group meeting; iloci
Summary: I gave a group meeting today on my iLocus work, and got some good feedback from the group.

- Taylor
    - we might want to be more careful about terminology clashes
        - we use piLoci and miLoci to refer to protein-coding iLoci and merged iLoci, respectively
        - in molecular genetics the pi- and mi- prefixes are often associated with piwi and microRNAs, respectively
        - it may not be a big deal, but it's something to consider
    - yeast is arguably the best annotated eukaryotic genome, should really investigate its organization
    - effect of TEs?
    - annotated UTR length and delta parameter
        - different deltas for upstream and downstream could be useful in some contexts
        - might think about how/whether UTR length could influence delta gene-by-gene
- Volker
    - did a project a few years ago
        - found pairs of genes with opposite orientation (i.e. `<--  -->`)
        - looked for palidromic motifs in the intergenic space
        - could be potentially interesting to investigate
    - read up on r-scans (maybe [this](http://www.sciencemag.org/content/257/5066/39.abstract) is a good starting point)
    - likes the idea of simulation
        - keep genome *content* constant, but modulate *organization*
        - randomly place giLoci in genomic sequence (don't allow overlaps)
        - compare miLocus/iiLocus summary stats
            - length distributions
            - miLocus gene counts
            - r-scans
