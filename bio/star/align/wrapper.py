__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import os
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


sample = [snakemake.input.sample] if isinstance(snakemake.input.sample, str) else snakemake.input.sample
n = len(sample)
assert n == 1 or n == 2, "input->sample must have 1 (single-end) or 2 (paired-end) elements."

if sample[0].endswith(".gz"):
    readcmd = "--readFilesCommand zcat"
else:
    readcmd = ""


outprefix = os.path.dirname(snakemake.output[0]) + "/"


shell(
    "STAR "
    "{snakemake.params.extra} "
    "--runThreadN {snakemake.threads} "
    "--genomeDir {snakemake.params.index} "
    "--readFilesIn {snakemake.input.sample} "
    "{readcmd} "
    "--outSAMtype BAM Unsorted "
    "--outFileNamePrefix {outprefix} "
    "--outStd Log "
    "{log}")
