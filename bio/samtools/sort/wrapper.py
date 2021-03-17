__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import os
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

out_name, out_ext = os.path.splitext(snakemake.output[0])

tmp_dir = snakemake.params.get("tmp_dir", "")
if tmp_dir:
    prefix = os.path.join(tmp_dir, os.path.basename(out_name))
else:
    prefix = out_name

# Samtools takes additional threads through its option -@
# One thread for samtools
# Other threads are *additional* threads passed to the argument -@
threads = "" if snakemake.threads <= 1 else " -@ {} ".format(snakemake.threads - 1)

shell(
    "samtools sort {extra} {threads} -o {snakemake.output[0]} "
    "-T {prefix} {snakemake.input[0]} "
    "{log}"
)
