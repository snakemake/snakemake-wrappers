__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

genome = ""
input_file = ""

if (os.path.splitext(snakemake.input[0])[-1]) == ".bam":
    input_file = "-ibam " + snakemake.input[0]

if len(snakemake.input) > 1:
    if (os.path.splitext(snakemake.input[0])[-1]) == ".bed":
        input_file = "-i " + snakemake.input.get("bed")
        genome = "-g " + snakemake.input.get("ref")

compress = "| bgzip" if snakemake.output[0].endswith(".gz") else ""

shell(
    "(genomeCoverageBed"
    " {snakemake.params}"
    " {input_file}"
    " {genome}"
    " {compress}"
    " > {snakemake.output[0]}) {log}"
)
