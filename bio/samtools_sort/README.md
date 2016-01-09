# Wrapper for samtools sort.

## Example:

```
rule samtools_sort:
    input:
        bam="mapped/{sample}.bam"
    output:
        bam="mapped/{sample}.sorted.bam"
    threads: 2
    script:
        "master/bio/samtools_sort"
```
