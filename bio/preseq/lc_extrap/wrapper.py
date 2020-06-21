__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

params = ""
sm_input = str(snakemake.input)
print(sm_input)
if (os.path.splitext(sm_input)[-1]) == ".bam":
    if "-bam" not in str(snakemake.params):
        params = "-bam "

shell(
    "(preseq lc_extrap "
    + params
    + "{snakemake.params} {snakemake.input[0]} -output {snakemake.output[0]}) {log}"
)
