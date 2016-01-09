# Wrapper for bcftools call.

## Example:

```
rule bcftools_call:
    input:
        fasta="genome.fasta",
        bams=expand("mapped/{sample}.sorted.bam", sample=config["samples"]),
        bais=expand("mapped/{sample}.sorted.bam.bai", sample=config["samples"])
    output:
        bam="called/{region}.bcf"  # region as expected by samtools mpileup (chr:start-stop)
    params:
        mpileup="",  # optional parameters for samtools mpileup (except -r, -g, -f)
        call=""  # optional parameters for bcftools call (except -v, -o)
    log:
        "logs/bcftools_call/{region}.log"
    wrapper:
        "master/bio/bcftools_call"
```
