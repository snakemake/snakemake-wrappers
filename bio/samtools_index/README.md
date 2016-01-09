# Wrapper for samtools index.

## Example:

```
rule samtools_index:
    input:
        bam="mapped/{sample}.sorted.bam"
    output:
        bai="mapped/{sample}.sorted.bam.bai"
    script:
        "ce8c887/bio/samtools_index"
```
