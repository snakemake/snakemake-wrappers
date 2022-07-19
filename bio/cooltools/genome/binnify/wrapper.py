__author__ = "Ilya Flyamer"
__copyright__ = "Copyright 2022, Ilya Flyamer"
__email__ = "flyamer@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

## Extract arguments
binsize = snakemake.params.get("binsize", snakemake.wildcards.get("binsize", 0))
if not binsize:
    raise ValueError("Please specify resolution either as a wildcard or as a parameter")
if not binsize:
    raise ValueError("binsize is required")
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


shell(
    "(cooltools genome binnify"
    " {snakemake.input.chromsizes} {binsize} "
    " {extra} "
    " > {snakemake.output}) {log}"
)
