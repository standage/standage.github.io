Title: Streaming data from the SRA with fastq-dump
Date: 2017-01-24
Author: Daniel S. Standage
Category: blog
Tags: sra; streaming; ngs

NCBI's [Sequence Read Archive](https://www.ncbi.nlm.nih.gov/sra) is the go-to repository for published genome-scale sequence data sets.
Although there are a variety of ways to download sequence data from SRA, the `fastq-dump` command from the [SRA Toolkit](https://www.ncbi.nlm.nih.gov/Traces/sra/?view=software) is the most convenient in my opinion.
In fact, with a few settings tweaks `fastq-dump` can stream data directly from the SRA into an analysis pipeline.

1. For a true streaming approach, you'll want to disable local file caching with [vdb-config](https://github.com/ncbi/sra-tools/wiki/Toolkit-Configuration).
   Especially on clusters with tight quotas on home directory storage, the default settings can be very problematic.
2. If you have paired reads, use the `--split-files` flag for proper printing of pairs and the `--stdout` flag (or `-Z` for short) so that the data is printed in *interleaved Fastq* format, rather than in two paired files (as is the default).
3. By default, the read IDs returned by `fastq-dump` don't include any pairing information, which some programs rely on for processing paired-end data.
   Include the options `--defline-seq '@$ac.$si.$sg/$ri' --defline-qual '+'` to append a `/1` or `/2` to the end of each read ID for pairing information, and to throw away all of the superfluous and redundant info in the 3rd line of each Fastq record.

The following example pipes the SRA data set with the accession ERR612477 into a processing pipeline.

```
fastq-dump --split-files --defline-seq '@$ac.$si.$sg/$ri' --defline-qual '+' -Z ERR612477 \
    | trim-low-abund.py --ksize 25 --max-memory-usage 2G --variable-coverage - \
    | my-favorite-mapper-or-assembler > out.dat
```
