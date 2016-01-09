# Wrapper for samtools index.

## Example:

```
rule samtools_index:
    input:
        "mapped/{sample}.sorted.bam"
    output:
        "mapped/{sample}.sorted.bam.bai"
    script:
        "master/bio/samtools_index"
```
