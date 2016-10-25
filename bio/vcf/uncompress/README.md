# Wrapper for bgzip compression and tabix indexing of vcf file.

## Example:

```
rule uncompress_vcf:
    input:
        "{prefix}.vcf.gz"
    output:
        "{prefix}.vcf"
    wrapper:
        "0.9.0/bio/vcf/uncompress"
```
