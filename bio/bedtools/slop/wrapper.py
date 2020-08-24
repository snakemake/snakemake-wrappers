__author__ = "Jan Forster"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"

from snakemake.shell import shell

## Extract arguments
extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "(bedtools slop"
    " {extra}"
    " -i {snakemake.input[0]}"
    " -g {snakemake.params.genome}"
    " > {snakemake.output})"
    " {log}"
)
