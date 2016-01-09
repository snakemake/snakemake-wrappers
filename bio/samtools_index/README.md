# Wrapper for samtools index.

## Example:

```
rule samtools_index:
    input:
        "mapped/{sample}.sorted.bam"
    output:
        "mapped/{sample}.sorted.bam.bai"
    wrapper:
        "0.0.1/bio/samtools_index"
```
