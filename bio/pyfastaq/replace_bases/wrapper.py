__author__ = "Michael Hall"
__copyright__ = "Copyright 2019, Michael Hall"
__email__ = "michael@mbh.sh"
__license__ = "MIT"


import os


log = snakemake.log_fmt_shell(stdout=False, stderr=True)

os.system(
    f"fastaq replace_bases"
    f" {snakemake.input[0]}"
    f" {snakemake.output[0]}"
    f" {snakemake.params.old_base}"
    f" {snakemake.params.new_base}"
    f" {log}"
)
