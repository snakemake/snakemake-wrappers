__author__ = "Jan Forster"
__copyright__ = "Copyright 2020, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"


import os
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


shell(
    "(razers3"
    " -tc {snakemake.threads}"
    " {extra}"
    " -o {snakemake.output[0]}"
    " {snakemake.params.genome}"
    " {snakemake.input.reads})"
    " {log}"
)
