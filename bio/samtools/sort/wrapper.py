__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import os.path as p
from snakemake.shell import shell


out_name, out_ext = p.splitext(snakemake.output[0])

tmp_dir = snakemake.params.get("tmp_dir", "")
if tmp_dir:
    prefix = p.join(tmp_dir, p.basename(out_name))
else:
    prefix = out_name

# Samtools takes additional threads through its option -@
# One thread for samtools
# Other threads are *additional* threads passed to the argument -@
threads = "" if snakemake.threads <= 1 else " -@ {} ".format(snakemake.threads - 1)

shell(
    "samtools sort {snakemake.params.extra} {threads} -o {snakemake.output[0]} "
    "-T {prefix} {snakemake.input[0]}"
)
