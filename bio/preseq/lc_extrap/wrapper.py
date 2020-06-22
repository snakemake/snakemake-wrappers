__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

params = ""
if (os.path.splitext(snakemake.input[0])[-1]) == ".bam":
    if "-bam" not in (snakemake.input[0]):
        params = "-bam "

shell(
    "(preseq lc_extrap {params} {snakemake.params} {snakemake.input[0]} -output {snakemake.output[0]}) {log}"
)
