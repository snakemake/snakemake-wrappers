__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2026, Johannes Köster"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import get_samtools_opts

samtools_opts = get_samtools_opts(snakemake)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=False)

# Parse input
fq_input = snakemake.input.fq
if not isinstance(fq_input, list):
    fq_input = [fq_input]

if len(fq_input) == 2:
    fq_input = "-1 {} -2 {}".format(*fq_input)
else:
    if snakemake.params.get("paired_end", False):
        fq_input = f"-s {fq_input[0]}"
    else:
        fq_input = f"-0 {fq_input[0]}"

shell("samtools import {samtools_opts} {extra} {fq_input} {log}")
