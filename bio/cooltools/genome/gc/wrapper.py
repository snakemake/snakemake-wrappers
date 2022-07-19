__author__ = "Ilya Flyamer"
__copyright__ = "Copyright 2022, Ilya Flyamer"
__email__ = "flyamer@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

## Extract arguments
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
shell(
    "(cooltools genome gc"
    " {snakemake.input.bins} {snakemake.input.fasta} {extra} > {snakemake.output})"
    " {log} "
)
