__author__ = "Brett Copeland"
__copyright__ = "Copyright 2021, Brett Copeland"
__email__ = "brcopeland@ucsd.edu"
__license__ = "MIT"


import os

from snakemake.shell import shell

java_memory_size = snakemake.params.get("java_mem_size", "")
if java_memory_size:
    memory_size = "--java-mem-size={}".format(java_memory_size)
else:
    memory_size = ""
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
shell(
    "qualimap {memory_size} rnaseq {extra} "
    "-bam {snakemake.input.bam} -gtf {snakemake.input.gtf} "
    "-outdir {snakemake.output} "
    "{log}"
)
