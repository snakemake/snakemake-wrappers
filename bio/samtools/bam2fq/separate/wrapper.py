__author__ = "David Laehnemann, Victoria Sack"
__copyright__ = "Copyright 2018, David Laehnemann, Victoria Sack"
__email__ = "david.laehnemann@hhu.de"
__license__ = "MIT"


import os
from snakemake.shell import shell

prefix = os.path.splitext(snakemake.output[0])[0]

# Samtools takes additional threads through its option -@
# One thread is used bu Samtools sort
# One thread is used by Samtools bam2fq
# So snakemake.threads has to take them into account
# before allowing additional threads through samtools sort -@
threads = "" if snakemake.threads <= 2 else " -@ {} ".format(snakemake.threads - 2)

shell(
    "samtools sort -n "
    " {threads} "
    " -T {prefix} "
    " {snakemake.params.sort} "
    " {snakemake.input[0]} | "
    "samtools bam2fq "
    " {snakemake.params.bam2fq} "
    " -1 {snakemake.output[0]} "
    " -2 {snakemake.output[1]} "
    " -0 /dev/null "
    " -s /dev/null "
    " -F 0x900 "
    " - "
)
