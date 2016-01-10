# Wrapper for samtools sort.

## Example:

```
rule samtools_sort:
    input:
        "mapped/{sample}.bam"
    output:
        "mapped/{sample}.sorted.bam"
    params:
        "-m 4G"
    threads: 8
    wrapper:
        "0.0.1/bio/samtools_sort"
```
