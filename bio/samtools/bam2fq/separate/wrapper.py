__author__ = "David Laehnemann, Victoria Sack"
__copyright__ = "Copyright 2018, David Laehnemann, Victoria Sack"
__email__ = "david.laehnemann@hhu.de"
__license__ = "MIT"


import os

prefix = os.path.splitext(snakemake.output[0])[0]

# Samtools takes additional threads through its option -@
# One thread is used bu Samtools sort
# One thread is used by Samtools bam2fq
# So snakemake.threads has to take them into account
# before allowing additional threads through samtools sort -@
threads = "" if snakemake.threads <= 2 else " -@ {} ".format(snakemake.threads - 2)

os.system(
    f"samtools sort -n "
    f" {threads} "
    f" -T {prefix} "
    f" {snakemake.params.sort} "
    f" {snakemake.input[0]} | "
    f"samtools bam2fq "
    f" {snakemake.params.bam2fq} "
    f" -1 {snakemake.output[0]} "
    f" -2 {snakemake.output[1]} "
    f" -0 /dev/null "
    f" -s /dev/null "
    f" -F 0x900 "
    f" - "
)
