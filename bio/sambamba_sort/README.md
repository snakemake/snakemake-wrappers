# Wrapper for sambamba sort.

## Example:

```
rule sambamba_sort:
    input:
        "mapped/{sample}.bam"
    output:
        "mapped/{sample}.sorted.bam"
    params:
        ""  # optional parameters
    threads: 8
    wrapper:
        "0.0.8/bio/sambamba_sort"
```
