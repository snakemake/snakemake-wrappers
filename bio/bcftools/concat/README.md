# Wrapper for bcftools concat.

## Example:

```
rule bcftools_concat:
    input:
        expand("called/{region}.bcf", region=chromosomes)
    output:
        "called/all.bcf"
    params:
        ""  # optional parameters for bcftools concat (except -o)
    wrapper:
        "0.1.0/bio/bcftools/concat"
```
