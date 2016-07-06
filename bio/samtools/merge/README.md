# Wrapper for samtools merge.

## Example:

```
rule samtools_merge:
    input:
        lambda wildcards: expand("mapped/{unit}.bam", unit=config["samples"][wildcards.sample])
    output:
        "merged/{sample}.bam"
    params:
        "" # optional additional parameters as string
    threads: 8
    wrapper:
        "0.2.0/bio/samtools/merge"
```
