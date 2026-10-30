"""Snakemake wrapper for Transdecoder LongOrfs"""

__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2019, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from pathlib import Path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

input_fasta = str(snakemake.input.fasta)
if input_fasta.endswith(".gz"):
    input_fa = Path(input_fasta).with_suffix("")
    shell("gunzip -c {input_fasta} > {input_fa}")
else:
    input_fa = input_fasta

gtm = snakemake.input.get("gene_trans_map", "")
if gtm:
    gtm = f"--gene_trans_map {gtm}"

output_dir = Path(snakemake.output[0]).parent
# transdecoder fails if output already exists. No force option available
shell(
    "rm -rf {output_dir} && TransDecoder.LongOrfs -t {input_fa} {gtm} --output_dir {output_dir} {log}"
)
