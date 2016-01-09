# Wrapper for samtools index.

## Example:

```
rule samtools_index:
    input:
        bam="mapped/{sample}.sorted.bam"
    output:
        bai="mapped/{sample}.sorted.bam.bai"
    script:
        "master/bio/samtools_index"
```
