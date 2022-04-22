__author__ = "Brett Copeland"
__copyright__ = "Copyright 2021, Brett Copeland"
__email__ = "brcopeland@ucsd.edu"
__license__ = "MIT"

import os
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
convert_out = snakemake.params.get("convert_out")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)


pipes = ""
if convert_out == "PicardCollectRnaSeqMetrics":
    pipes += " | csvcut -t -c 12,1-10 | csvformat -T"


shell(
    "(gtfToGenePred {extra} {snakemake.input} /dev/stdout {pipes} > {snakemake.output}) {log}"
)
