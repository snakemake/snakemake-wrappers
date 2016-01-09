# Wrapper for samtools sort.

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
        "0.0.1/bio/bcftools_view"
```
