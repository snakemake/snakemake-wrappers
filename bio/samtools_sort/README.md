# Wrapper for samtools sort.

## Example:

```
rule samtools_sort:
    input:
        "mapped/{sample}.bam"
    output:
        "mapped/{sample}.sorted.bam"
    threads: 2
    script:
        "master/bio/samtools_sort"
```
