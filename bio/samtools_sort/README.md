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
        "0.0.1/bio/samtools_sort"
```
