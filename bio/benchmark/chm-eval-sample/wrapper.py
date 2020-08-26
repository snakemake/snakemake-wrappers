__author__ = "Johannes Köster"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import os

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

url = "ftp://ftp.sra.ebi.ac.uk/vol1/run/ERR134/ERR1341796/CHM1_CHM13_2.bam"

fmt = "-b"
prefix = snakemake.params.get("first_n", "")
if prefix:
    prefix = "| head -n {} | samtools view -h -b".format(prefix)
    fmt = "-h"

    # Separate into two commands
    os.system(f"samtools view {fmt} {url} {prefix} > {snakemake.output.bam} {log}")
    os.system(f"samtools index {snakemake.output.bam} {log}")
else:
    os.system(
        f"curl -L {url} > {snakemake.output.bam} samtools index {snakemake.output.bam} {log}"
    )
