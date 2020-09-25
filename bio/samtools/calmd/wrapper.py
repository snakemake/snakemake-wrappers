__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2020, Filipe G. Vieira"
__license__ = "MIT"


from snakemake.shell import shell

input = list(filter(None, [snakemake.input.get("sam", None), snakemake.input.get("bam", None), snakemake.input.get("cram", None)]))

if len(input) < 1:
    raise ValueError("no valid input file provided")
elif len(input) < 1:
    raise ValueError("too many valid input files provided")

shell("samtools calmd --threads {snakemake.threads} {snakemake.params} {input[0]} {snakemake.input.ref} > {snakemake.output[0]}")
