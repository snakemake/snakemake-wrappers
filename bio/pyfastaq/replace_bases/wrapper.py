__author__ = "Michael Hall"
__copyright__ = "Copyright 2019, Michael Hall"
__email__ = "michael@mbh.sh"
__license__ = "MIT"


import os


log = snakemake.log_fmt_shell(stdout=False, stderr=True)

os.system(
    f"fastaq replace_bases"
    " {snakemake.input[0]}"
    " {snakemake.output[0]}"
    " {snakemake.params.old_base}"
    " {snakemake.params.new_base}"
    " {log}"
)
