__author__ = "David Laehnemann, Victoria Sack"
__copyright__ = "Copyright 2018, David Laehnemann, Victoria Sack"
__email__ = "david.laehnemann@hhu.de"
__license__ = "MIT"


import os
from snakemake.shell import shell

prefix = os.path.splitext(snakemake.output[0])[0]

shell(
    "samtools sort -n "
    " -@ {snakemake.threads} "
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
