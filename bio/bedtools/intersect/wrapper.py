__author__ = "Jan Forster"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"

from snakemake.shell import shell

## Extract arguments
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Allow compressed output via gzip
if snakemake.output[0].endswith(".gz"):
    compress = "| gzip"
else:
    compress = ""

shell(
    "(bedtools intersect"
    " {extra}"
    " -a {snakemake.input.left}"
    " -b {snakemake.input.right}"
    " {compress}"
    " > {snakemake.output})"
    " {log}"
)
