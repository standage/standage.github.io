Title: Software & Databases
navorder: 03

### [kevlar](http://kevlar.readthedocs.io/)

The primary focus of my postdoctoral research is novel germline variant discovery in autism simplex pedigrees.
In support of this work, I am developing reference-free methods for variant discovery that should generalize very easily to other eukaryotes.
The kevlar software has served as my testbed for simulation, method development, and data analysis.
From its inception it has been developed as an open source software project.

### [khmer Library](http://khmer.readthedocs.io/)

Before joining the DIB Lab at UC Davis, I was a user of and (modest) contributor to the khmer library.
Now as a member of the lab, I'm one of the core developers and have taken the lead on implementing several new features.

### [tag Library](https://github.com/standage/tag)

The tag library began as a toy side project for playing with genome annotation data (borrowing concepts heavily from GenomeTools) and figuring out how to publish Python packages.
Since it has blossomed into a useful piece of software...if I might say so myself! :)
It does the hard work of connecting related features in memory (which most BED/GTF/GFF3 parsers leave as an exerise for the user) and embraces a streaming processing paradigm.

### [AEGeAn Toolkit](http://brendelgroup.github.io/AEGeAn)

I am the primary developer of the AEGeAn Toolkit, an integrated toolkit for anlaysis and evaluation of genome annotations.
AEGeAn includes a collection of programs and scripts—most notably `ParsEval` and `LocusPocus`—as well as a C library whose API provides access to all of AEGeAn's core functions and data structures.

### [*P. dominula* Genome Project](http://pdomgenomeproject.github.io/)

Figuring out the best way to distribute the code, data, and full supplemental materials supporting our paper wasp genome project was not easy, but I'm very proud of the standard we were able to achieve with this project.
A description of every precise command used in each analysis, alongside the scripts, code, and ancillary files needed to reproduce the analysis, were posted to GitHub.
Data files that could not easily be uploaded to public databases such as GenBank or the NCBI SRA were deposited in fig**share** for archival.
And we provided the ability to search, visualize, and manually curate the genome with the PdomGDB genome browser.

### [GenHub](http://standage.github.io/genhub)

GenHub is a companion to the AEGeAn Toolkit and the `LocusPocus` program, which implements iLocus parsing functionality.
GenHub's `Fidibus` program provides a more comprehensive pipeline around LocusPocus for data retrieval, pre-processing, post-processing, and computing statistics on iLoci.

### [GenomeTools Library](http://genometools.org/)

I am an avid user of and contributor to the GenomeTools library, a collection of excellent genome informatics tools.
Most of my contributions come in the form of small patches, bug reports, and feature requests, although I have implemented one core data structure.

In many ways GenomeTools served as a model for my development of the AEGeAn Toolkit.
The GenomeTools development community is small but active, and were very accomodating when I first starting using their API, and then later when I began patching and extending it.
I can thank these kind folks for most of what I know about software engineering!
