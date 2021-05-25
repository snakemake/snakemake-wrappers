__author__ = "Brett Copeland"
__copyright__ = "Copyright 2021, Brett Copeland"
__email__ = "brcopeland@ucsd.edu"
__license__ = "MIT"


import os

from snakemake.shell import shell

java_opts = snakemake.params.get("java_opts", "")
if java_opts:
    java_opts_str = f'JAVA_OPTS="{java_opts}"'
else:
    java_opts_str = ""
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
shell(
    "{java_opts_str} qualimap rnaseq {extra} "
    "-bam {snakemake.input.bam} -gtf {snakemake.input.gtf} "
    "-outdir {snakemake.output} "
    "{log}"
)
