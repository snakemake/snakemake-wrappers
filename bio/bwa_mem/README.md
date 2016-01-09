# Wrapper for bwa mem.

## Example:

```
rule bwa_mem:
    input:
        fasta="genome.fasta",
        fastq=["reads/{sample}.1.fastq.gz", "reads/{sample}.2.fastq.gz"]
    output:
        bam="mapped/{sample}.bam"
    log:
        "logs/bwa_mem/{sample}.log"
    params:
        ""  # optional parameters for bwa mem (e.g. read group)
    threads: 8
    script:
        "ce8c887/bio/bwa_mem"
```
