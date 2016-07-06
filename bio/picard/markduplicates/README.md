# Wrapper for picard MarkDuplicates.

## Example:

```
rule mark_duplicates:
    input:
        "mapped/{sample}.bam"
    output:
        bam="dedup/{sample}.bam",
        metrics="dedup/{sample}.metrics.txt"
    log:
        "logs/picard/dedup/{sample}.log"
    params:
        "REMOVE_DUPLICATES=true"
    wrapper:
        "0.14.0/bio/picard/markduplicates"
```
