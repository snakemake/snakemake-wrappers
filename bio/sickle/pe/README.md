# Wrapper for `sickle pe`

This is a Snakemake wrapper for the [sickle](https://github.com/najoshi/sickle) tool, subcommand `pe`. The supported
input and output modes are only for separate files. This means the wrapper will not work for interleaved input and/or
output files.


## Provided Flags

### Input

  * `r1` (maps to `-f`)
  * `r2` (maps to `-r`)

### Output

  * `r1` (maps to `-o`)
  * `r2` (maps to `-p`)
  * `rs` (maps to `-s`)

### Parameters

  * `qual_type` (maps to `-t`)
  * `other`, where all other optional flags should be put. This is meant to be a free-form string if defined.

Additionally, the `log` attribute of the rule must be set to a valid file path.


## Example

```
rule sickle_pe:
  input:
    r1="input_R1.fq",
    r2="input_R2.fq"
  output:
    r1="output_R1.fq",
    r2="output_R2.fq",
    rs="output_single.fq",
  params:
    qual_type="sanger",
  log:
    "logs/sickle/job.log"
  wrapper:
    "0.8.0/bio/sickle/pe"
```
