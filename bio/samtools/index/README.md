# Wrapper for samtools index.

## Example:

```
rule samtools_index:
    input:
        "mapped/{sample}.sorted.bam"
    output:
        "mapped/{sample}.sorted.bam.bai"
    params:
        "" # optional params string
    wrapper:
        "0.2.0/bio/samtools/index"
```
