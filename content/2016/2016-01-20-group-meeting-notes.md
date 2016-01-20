Title: Group meeting feedback, 20 Jan 2015
Date: 2016-01-20
Author: Daniel S. Standage
Category: notebook
Tags: group meeting; iloci
Summary: I gave another group meeting today, this time on random arrangements of iLoci. This entry records feedback I received from the group members.

- I went right on to the practical applications and the results, without spending enough time motivating.
    - First, we want a reliable set of benchmarks that we can run a genome annotation through to get a quick first look at a genome.
      Is it normal?
      Are the genes much longer/shorter than related genomes?
      What about the lengths of intergenic regions?
    - Second, we want to really understand how genes are organized in the eukaryotic genome.
        - What do we *really* know about how genes are situated?
        - There are well-known cases of densely packed genes, such as virulence resistance genes and HOX clusters, the latter resulting from gene duplications that have held position over evolutionary time.
        - But how widespread is this throughout the genome?
          To what extent are genes densely packed in the genome?
          What implications does this have for transcription and for molecular evolution?
    - Third, genome assemblies and annotations vary widely in quality.
      iLoci provide a granular representation of the genome, which we can use to select those parts we're confident in.
      Want to train a hidden Markov model for gene finding?
      Want to analyze codon usage?
      Want to calculate dN/dS ratios?
      Don't do it on the whole genome, select the iLoci you're confident in!
        - Independent of how good the annotation is generally, these XXXX gene models are definitely reliable.
- The iLocus shuffling procedure might need to be refined.
    - Currently, the delta extensions are retained when re-positioning the giLoci.
    - This will definitely bias the results away from ziLoci and miLoci.
    - Better to randomly distribute giLoci with delta=0.
