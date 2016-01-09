# Wrapper for samtools sort.

## Example:

```
rule samtools_sort:
    input:
        "mapped/{sample}.bam"
    output:
        "mapped/{sample}.sorted.bam"
    threads: 2
    wrapper:
        "master/bio/samtools_sort"
```
