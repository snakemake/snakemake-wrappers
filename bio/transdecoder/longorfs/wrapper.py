"""Snakemake wrapper for Transdecoder"""

__author__ = "N Tessa Pierce"
__copyright__ = "Copyright 2019, Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

gtm_cmd = ""
gtm = snakemake.input.get("gene_trans_map", "")
if gtm:
    gtm_cmd = " --gene_trans_map " + gtm

output_dir = path.dirname(str(snakemake.output))

# transdecoder fails if output already exists. No force option available
shell("rm -rf {output_dir}")
shell("TransDecoder.LongOrfs -t {snakemake.input.fasta} {gtm_cmd} {log}")
