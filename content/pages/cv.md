Title: CV
url:
save_as: cv.html
status: hidden

## Education & Training

<table>
  <tr>
    <td>2016 — present</td>
    <td>
      Postdoctoral Scholar<br />
      Lab for Data Intensive Biology<br />
      University of California, Davis
    </td>
  </tr>
    <tr>
      <td>2016</td>
      <td>
        Ph.D. in <strong>Bioinformatics and Computational Biology</strong><br />
        Iowa State University<br />
        In residence at Indiana University July 2012 — May 2016
      </td>
    </tr>
  <tr>
    <td>2010</td>
    <td>
      B.S. in <strong>Bioinformatics</strong> (with minors in <strong>Mathematics</strong> and <strong>Computer Science</strong>)<br />
      Brigham Young University<br />
      Honors thesis: <em>PhyloProf: A Software Package for Predicting Gene Function Using Phylogenetic Profile Analysis</em>
    </td>
  </tr>
</table>


## Research Interests

Variant discovery and analysis  
Genome organization  
Genome annotation and annotation data management  
Comparative genomics  


## Previous Research Experience

**Graduate Research Assistant**  
Computational Genome Science Lab  
Indiana University, 2012 — 2016

**Graduate Research Assistant**  
BCB Graduate Program  
Iowa State University, 2010 — 2012

**Undegraduate Research Technician**  
Plant Genetics Lab  
Brigham Young University, 2009 — 2010

**NSF REU Research Intern**  
Department of Genetics  
University of Georgia, 2008

**Undegraduate Research Assistant**  
Center for Language Studies  
Brigham Young University, 2007 — 2010


## Awards & Honors

**Young and Loomis Travel Award**  
Department of Genetics, Development, and Cell Biology  
Iowa State University

**Top Presenter Award**, Student Research Seminar  
Bioinformatics and Computational Biology Program  
Iowa State University

**Wendell Miller Trust Fellow**  
Graduate College  
Iowa State University

**University Honors**  
*Highest undergraduate distinction*  
Brigham Young University

**Merit-based Scholarship Recipient**  
College of Life Sciences  
Brigham Young University


## Scholarship

### Publications

**Standage DS**, Crusoe MR, Joslin SEK, Kingsley NB, Murray KD, Neches R, Scott C, Shean R, Steinbiss S, Sydney C, Brown CT (2017). khmer release v2.1: software for biological sequence analysis. *The Journal of Open Source Software*, 2(15), 272, [doi:10.21105/joss.00272](http://dx.doi.org/10.21105/joss.00272).

**Standage DS**, Berens AJ, Glastad KM, Severin AJ, Brendel VP, Toth AL (2016) Genome, transcriptome, and methylome sequencing of a primitively eusocial wasp reveal a greatly reduced DNA methylation system in a social insect. *Molecular Ecology*, [doi:10.1111/mec.13578](http://dx.doi.org/10.1111/mec.13578).

Duvick JP, **Standage DS**, Merchant N, Brendel VP (2016) xGDBvm: A Web GUI-driven workflow for annotating eukaryotic genomes in the cloud. *The Plant Cell*, Advance publication, [doi:10.1105/tpc.15.00933](http://dx.doi.org/10.1105/tpc.15.00933).

**Standage DS**, Brendel VP (2012) ParsEval: parallel comparison and analysis of gene structure annotations. *BMC Bioinformatics*, **13**:187, [doi:10.1186/1471-2105-13-187](http://dx.doi.org/10.1186/1471-2105-13-187).

Doyle EL, Booher NJ, **Standage DS**, Voytas DF, Brendel VP, VanDyk JK, Bogdanove AJ (2012) TAL Effector-Nucleotide Targeter (TALE-NT) 2.0: Tools for TAL effector design and target prediction. *Nucleic Acids Research*, **40** (W1): W117-W122, [doi:10.1093/nar/gks608](http://dx.doi.org/10.1093/nar/gks608).

### Selected Oral Presentations

**Standage DS**, Wilson GV. Managing research software projects. Presented at Lawrence Berkeley National Laboratory, September 2017.

**Standage DS**. Testing research software: an academic perspective on compromise. Presented at PyCon, May 2017.

**Standage DS**, Brown CT, Hormozdiari F. Kevlar: reference-free variant discovery in human genomes and beyond. Presented at the Sequencing, Finishing, and Analysis of the Future Meeting, May 2017. *Manuscript in preparation*.

**Standage DS**, Wilson GV. Managing research software projects. Presented at Lawrence Berkeley Laboratory LabTech, October 2016.

**Standage DS**, Toth AL, Brendel VP. iLoci: scalable annotation for provisional genome assemblies. Presented at CSHL Biology and Genomics of Social Insects Meeting, May 2015. *Manuscript in preparation*.

Duvick JP, Denton JF, **Standage DS**, Merchant N, Brendel VP. xGDBvm: a virtual platform for annotating eukaryotic genomes. Invited talk given at PAG XXI, January 2013.

### Selected Posters

**Standage DS**, Brendel VP, Toth AL. Genome sequence and annotation of the primitively social paper wasp *Polistes dominula*. Presented at Notre Dame Arthropod Genomics Conference, June 2013.

Brendel VP, **Standage DS**. mRNAmarkup: quality control and annotation of de novo transcriptome assemblies. Presented at CSHL Genome Informatics meeting, November 2013.


## Selected Research Projects

**Discovery of novel germline variants in whole genome sequence data from autism simplex pedigrees**  
[https://github.com/dib-lab/kevlar](https://github.com/dib-lab/kevlar)  
In this project I am developing a novel method for identifying *de novo* mutations in autism trios and quads.
This method does not rely on read alignments but on *k*-mer abundances to identify potential variants, increasing sensitivity and incorporating multiple variant types in a single workflow.
This project is being actively developed as an open source research software library and is distributed as a Python package.
*Manuscript in preparation.*

**Efficient and tunable processing of sequence data using *k*-mer banding**  
In my variant discovery work we developed a split-and-gather strategy that demonstrates a linear reduction in memory requirements when processing sequence data in batches.
This project explores additional contexts in which subsampling data with *k*-mer banding will provide a substantial decrease in memory requirements but also in runtime.

**Robust evaluation of genome content and organization with iLoci**  
[https://github.com/BrendelGroup/IntervalLoci](https://github.com/BrendelGroup/IntervalLoci)  
In this project I am developing a new framework for genome analyses based on parsing an annotated genome assembly in distinct units (iLoci).
Statistics computed on iLoci reflect various characteristics of genome content and organization in a way that is explicit and meaningful for comparison between related data sets.
This project also introduces a well-defined measure of relative genome compactness and explores trends across a variety of eukaryotic genomes.
*Manuscript in preparation*.

**Paper wasp genome project**  
[http://pdomgenomeproject.github.io](http://pdomgenomeproject.github.io)  
Investigating the molecular mechanisms contributing to social behavior and caste differentiation in the paper wasp *Polistes dominula* was a primary emphasis of my doctoral research, and required a substantial amount of bioinformatics work.
My contributions to this project included quality control of more than a dozen Illumina samples (whole genome shotgun and RNA-seq), *de novo* genome and transcriptome assembly, genome annotation, differential expression analysis, alternative splicing analysis, phylogenetic analysis of conserved single copy orthologs, analysis of taxonomically restricted genes, and assistance with processing and interpreting results of bisulfite sequencing analysis.

**xGDBvm: cloud-based genome browser and annotation platform**  
[http://goblinx.soic.indiana.edu](http://goblinx.soic.indiana.edu)  
For many years my graduate lab has operated [PlantGDB](http://plantgdb.org), a web-based system for comparative plant genomics that provides genome browsers, various search capabilities, and integrated community annotation tools.
I contributed to porting this platform over to the NSF cloud computing provider Atmosphere (now Jetstream), and used this platform for hosting the [*P. dominula* genome database](http://goblinx.soic.indiana.edu/PdomGDB).
Using xGDBvm, our paper wasp project was able to collect hundreds of manually curated annotations from colleagues, collaborators, and biology/bioinformatics students, and feed these back into our annotation workflow.


## Teaching

**Computational Genome Science**  
<small>(Fall 2011, Spring 2013, Spring 2014, Spring 2015)</small>  
I helped design the course in 2011, and was the primary instructor from 2013 to 2015.

**Science of Biology, Honors**  
<small>(Spring 2007, Spring 2008)</small>  
As TA I held independent review sessions and graded reports of student experiments.


## Professional Activities

### Journal Review

**International Journal of Molecular Sciences**  
October 2017

**Science**  
May 2013

**Bioinformatics**  
April 2013, October 2016

**ACM BCB**  
June 2016

### Open Source Research Software

Except where specified, I am lead contributor to the following research software projects.

**kevlar Library**  
[http://kevlar.readthedocs.io](http://kevlar.readthedocs.io)

**khmer Library** (core contributor)  
[http://khmer.readthedocs.io](http://khmer.readthedocs.io)

**tag Library**  
[https://tag.readthedocs.io](https://tag.readthedocs.io)

**AEGeAn Toolkit**  
[http://brendelgroup.github.io/AEGeAn](http://brendelgroup.github.io/AEGeAn)

**GenHub**  
[http://standage.github.io/genhub](http://standage.github.io/genhub)

**GenomeTools Library** (contributor)  
[http://genometools.org/](http://genometools.org/)

### Community Training

**Workshop on Managing Research Software Projects**  
Lead instructor  
Fall 2017, Lawrence Berkeley National Lab

[**Data Intensive Biology Summer Institute**](http://ivory.idyll.org/dibsi/)  
Workshop instructor  
Summer 2017, UC Davis

[**Course on Analyzing NGS Data**](http://bioinformatics.msu.edu/ngs-summer-course-2014)  
Invited instructor  
Summer 2014, Michigan State University

[**Software Carpentry**](http://software-carpentry.org/) & [**Data Carpentry**](http://www.datacarpentry.org/) certified instructor


## Technical Skills

**Software development**  
C, C++, Python, Java

**Scripting, data processing**  
Python, Perl, Bash

**Data analysis, statistical computing**  
Python, R

**Pipelines, workflow management**  
Bash, GNU Make, pydoit

**High-performance computing**  
MPI programming, OpenMP programming, HPC/cluster computing, VM/cloud computing
