# Wrapper for picard AddOrReplaceReadGroups.

## Example:

```
rule replace_rg:
    input:
        "mapped/{sample}.bam"
    output:
        "fixed-rg/{sample}.bam"
    log:
        "logs/picard/replace_rg/{sample}.log"
    params:
        "RGLB=lib1 RGPL=illumina RGPU={sample} RGSM={sample}"
    wrapper:
        "0.5.0/bio/picard/addorreplacereadgroups"
```
