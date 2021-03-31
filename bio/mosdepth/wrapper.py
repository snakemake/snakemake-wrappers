__author__ = "William Rowell"
__copyright__ = "Copyright 2020, William Rowell"
__email__ = "wrowell@pacb.com"
__license__ = "MIT"

import re
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
by = snakemake.params.get("by", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# mosdepth takes additional threads through its option --threads
# One thread for mosdepth
# Other threads are *additional* decompression threads passed to the '--threads' argument
threads = "" if snakemake.threads <= 1 else "--threads {}".format(snakemake.threads - 1)

if by:
    by = f"--by {by}"

# first output must be *.mosdepth.summary.txt
prefix = re.sub("\.mosdepth\.summary\.txt", "", snakemake.output[0])



shell(
    """
    (mosdepth {threads} \
        {by} {extra} \
        {prefix} \
        {snakemake.input.bam}) {log}
    """
)
