__author__ = "Jan Forster"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"

from os import path

from snakemake.shell import shell

## Extract arguments
extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "(pre.py"
    " --threads {snakemake.threads}"
    " -r {snakemake.params.genome}"
    " {extra}"
    " {snakemake.input.variants}"
    " {snakemake.output})"
    " {log}"
)
