__author__ = "David Laehnemann, Victoria Sack"
__copyright__ = "Copyright 2018, David Laehnemann, Victoria Sack"
__email__ = "david.laehnemann@hhu.de"
__license__ = "MIT"


import os
import tempfile
from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_mem

params_collate = snakemake.params.get("collate", "")
params_fastq = snakemake.params.get("fastq", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Samtools takes additional threads through its option -@
# One thread is used by Samtools collate
# One thread is used by Samtools fastq
# So snakemake.threads has to take them into account
# before allowing additional threads through samtools sort -@
threads = 0 if snakemake.threads <= 2 else snakemake.threads - 2

shell(
    "(samtools collate -u -O"
    " --threads {threads}"
    " {params_collate}"
    " {snakemake.input[0]} | "
    "samtools fastq"
    " {params_fastq}"
    " -1 {snakemake.output[0]}"
    " -2 {snakemake.output[1]}"
    " -0 /dev/null"
    " -s /dev/null"
    " -F 0x900"
    " - "
    ") {log}"
)
