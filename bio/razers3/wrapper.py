__author__ = "Jan Forster"
__copyright__ = "Copyright 2020, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"


import os

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


os.system(
    f"(razers3"
    f" -tc {snakemake.threads}"
    f" {extra}"
    f" -o {snakemake.output[0]}"
    f" {snakemake.params.genome}"
    f" {snakemake.input.reads})"
    f" {log}"
)
