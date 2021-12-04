__author__ = "David Laehnemann, Victoria Sack"
__copyright__ = "Copyright 2018, David Laehnemann, Victoria Sack"
__email__ = "david.laehnemann@hhu.de"
__license__ = "MIT"


import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

prefix = os.path.splitext(snakemake.output[0])[0]

shell(
    "samtools bam2fq {snakemake.params} "
    " -@ {snakemake.threads} "
    " {snakemake.input[0]}"
    " > {snakemake.output[0]} "
    "{log}"
)
