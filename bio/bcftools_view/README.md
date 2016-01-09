# Wrapper for samtools sort.

## Example:

```
rule bcf_to_vcf:
    input:
        "{prefix}.bcf"
    output:
        "{prefix}.vcf"
    params:
        ""  # add additional bcftools view parameters here (e.g., for filtering)
    script:
        "ce8c887/bio/bcftools_view"
```
