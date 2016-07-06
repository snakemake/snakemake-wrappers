# Wrapper for bgzip compression and tabix indexing of vcf file.

## Example:

```
rule compress_vcf:
    input:
        "{prefix}.vcf"
    output:
        "{prefix}.vcf.gz"
    wrapper:
        "0.3.0/bio/vcf/compress"
```
