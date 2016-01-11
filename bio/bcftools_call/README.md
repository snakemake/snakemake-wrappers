# Wrapper for bcftools call.

## Example:

```
rule bcftools_call:
    input:
        ref="genome.fasta",
        samples=expand("mapped/{sample}.sorted.bam", sample=config["samples"]),
        indexes=expand("mapped/{sample}.sorted.bam.bai", sample=config["samples"])
    output:
        "called/{region}.bcf"  # region as expected by samtools mpileup (chr:start-stop)
    params:
        mpileup="",  # optional parameters for samtools mpileup (except -r, -g, -f)
        call=""  # optional parameters for bcftools call (except -v, -o, -m)
    log:
        "logs/bcftools_call/{region}.log"
    wrapper:
        "0.0.8/bio/bcftools_call"
```
