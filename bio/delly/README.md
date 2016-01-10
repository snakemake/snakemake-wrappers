# Wrapper for delly.

## Example:

```
rule delly:
    input:
        fasta="genome.fasta",
        bams=expand("mapped/{sample}.bam", sample=config["samples"])
    output:
        vcf="sv/{type,(DEL|DUP|INV|TRA|INS)}.vcf"
    params:
        ""  # optional parameters for delly (except -t, -g)
    log:
        "logs/delly/{type}.log"
    threads: 16
    wrapper:
        "0.0.1/bio/delly"
```
