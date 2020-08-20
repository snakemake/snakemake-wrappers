__author__ = "David Laehnemann, Victoria Sack"
__copyright__ = "Copyright 2018, David Laehnemann, Victoria Sack"
__email__ = "david.laehnemann@hhu.de"
__license__ = "MIT"


import os


prefix = os.path.splitext(snakemake.output[0])[0]

os.system(
    f"samtools bam2fq {snakemake.params} "
    f" -@ {snakemake.threads} "
    f" {snakemake.input[0]}"
    f" >{snakemake.output[0]} "
)
