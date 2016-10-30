# Wrapper for hisat2

## Example

```
rule hisat2:
    input:
      reads=["reads/{sample}.1.fastq.gz", "reads/{sample}.2.fastq.gz"],
    output:
      "mapped/{sample}.bam"
    log:                                # optional
      "logs/hisat2/{sample}.log"
    params:                             # ref is required, extra is optional
      ref="genome.fa",
      extra="--min-intronlen 1000"
    threads: 8                          # optional, defaults to 1
    wrapper:
      "0.7.0/bio/hisat2"
```

## Notes

  * The `reads` input parameters must point to at least one and at most two
    input files. It can be supplied either as a string (for one input files)
    or as a list (for one or two input files).
  * The `-S` flag must not be used since output is already directly piped to
    `samtools` for compression.
  * The `--threads/-p` flag must not be used since threads is set separately
    via the snakemake `threads` directive.

## Limitations

  * The wrapper does not yet handle SRA input accessions.
  * No reference index files checking is done since the actual number of files
    may differ depending on the reference sequence size. This is also why
    the index is supplied in the `params` directive instead of the `input`
    directive.
