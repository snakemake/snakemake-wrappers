__author__ = "Jan Forster"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"

from snakemake.shell import shell

## Extract arguments
extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "(cat {snakemake.input} | "
    "sort -k1,1 -k2,2n - | "
    "bedtools merge"
    " {extra}"
    " -i -"
    " > {snakemake.output})"
    " {log}"
)
