__author__ = "William Rowell"
__copyright__ = "Copyright 2020, William Rowell"
__email__ = "wrowell@pacb.com"
__license__ = "MIT"


import os
from snakemake.shell import shell
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get("extra", "")
# Samtools takes additional threads through its option -@
# One thread for samtools merge
# Other threads are *additional* threads passed to the '-@' argument
threads = "" if snakemake.threads <= 1 else " -@ {} ".format(snakemake.threads - 1)

shell(
    """
    (samtools {snakemake.params.outputtype} \
        {threads} {extra} \
        {snakemake.input} > {snakemake.output}) {log}
    """
)

