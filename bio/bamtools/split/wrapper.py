__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2021, Patrik Smeds"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

split_type = snakemake.params.get("split_type", "-reference")

if len(snakemake.input) != 1:
    raise ValueError("One bam input file expected, got: " + str(len(snakemake.input)))

shell("bamtools split -in {snakemake.input} " + split_type + " {log}")
