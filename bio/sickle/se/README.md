# Wrapper for `sickle pe`

This is a Snakemake wrapper for the [sickle](https://github.com/najoshi/sickle) tool, subcommand `se`.


## Provided Flags

### Input & Output

  See example below.

### Parameters

  * `qual_type` (maps to `-t`)
  * `other`, where all other optional flags should be put. This is meant to be a free-form string if defined.

Additionally, the `log` attribute of the rule must be set to a valid file path.


## Example

```
rule sickle_pe:
  input:
    "input_R1.fq",
  output:
    "output_R1.fq",
  params:
    qual_type="sanger",
  log:
    "logs/sickle/job.log"
  wrapper:
    "bio/sickle/pe"
```
