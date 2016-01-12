# Wrapper for delly.

## Example:

```
rule delly:
    input:
        ref="genome.fasta",
        samples=expand("mapped/{sample}.bam", sample=config["samples"]),
        indexes=expand("mapped/{sample}.bam.bai", sample=config["samples"])
    output:
        "sv/{type,(DEL|DUP|INV|TRA|INS)}.vcf"
    params:
        ""  # optional parameters for delly (except -t, -g)
    log:
        "logs/delly/{type}.log"
    threads: 3
    wrapper:
        "0.0.10/bio/delly"
```
