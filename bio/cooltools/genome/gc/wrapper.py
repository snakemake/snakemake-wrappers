__author__ = "Ilya Flyamer"
__copyright__ = "Copyright 2022, Ilya Flyamer"
__email__ = "flyamer@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

## Extract arguments
bins = snakemake.input.get("bins", "")
if not bins:
    raise ValueError("bins are required")
fasta = snakemake.input.get("fasta", "")
if not fasta:
    raise ValueError("fasta is required")
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


shell("(cooltools genome gc {bins} {fasta} {extra} > {snakemake.output}) {log}")
