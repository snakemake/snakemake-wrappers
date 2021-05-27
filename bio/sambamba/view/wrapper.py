__author__ = "Jan Forster"
__copyright__ = "Copyright 2021, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"


import os

from snakemake.shell import shell

in_file = snakemake.input[0]
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

if in_file.endswith(".sam") and ("-S" not in extra or "--sam-input" not in extra):
    extra += " --sam-input"

shell(
    "sambamba view {extra} -t {snakemake.threads} "
    "{snakemake.input[0]} > {snakemake.output[0]} "
    "{log}"
)
