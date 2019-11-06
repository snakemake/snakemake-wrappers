"""Snakemake wrapper for Transdecoder."""

__author__ = "N Tessa Pierce"
__copyright__ = "Copyright 2010, Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")

# infer seqtype from input files:

outdir = path.dirname(snakemake.output[0])
assert "trinity" in outdir, "output directory name must contain 'trinity'"

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    " TransDecoder.LongOrfs -t {snakemake.input.fasta} --gene_trans_map {snakemake.input.tsv} {log}
shell(
    "Trinity {input_cmd} --CPU {snakemake.threads} "
    " --max_memory {max_memory} --seqType {seqtype} "
    " --output {outdir} {snakemake.params.extra} "
    " {log}"
)
