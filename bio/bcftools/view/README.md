# Wrapper for bcftools view.

## Example:

```
rule bcf_to_vcf:
    input:
        "{prefix}.bcf"
    output:
        "{prefix}.vcf"
    params:
        ""  # optional parameters for bcftools view (except -o)
    wrapper:
        "0.2.0/bio/bcftools/view"
```
