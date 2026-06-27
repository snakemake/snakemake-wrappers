"""Snakemake wrapper for Transdecoder LongOrfs"""

__author__ = "N. Tessa Pierce, Filipe G. Vieira"
__copyright__ = "Copyright 2019, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

import tempfile
from pathlib import Path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


# Input
ref = snakemake.input.get("ref", "")
if ref:
    ref = f"--genome {ref}"

gtf = snakemake.input.get("gtf", "")
if gtf:
    gtf = f"--gtf {gtf}"

gtm = snakemake.input.get("gene_trans_map", "")
if gtm:
    gtm = f"--gene_trans_map {gtm}"


with tempfile.TemporaryDirectory(delete=False) as tmpdir:
    input_fas = snakemake.input.get("fasta", "")
    if input_fas:
        if input_fas.endswith(".gz"):
            input_fas = Path(tmpdir) / "tmp_input.fas"
            shell("gunzip -c {snakemake.input.fasta} > {input_fas}")
        input_fas = f"--transcripts {input_fas}"

    shell("TransDecoder {input_fas} {ref} {gtf} {gtm} -O {tmpdir} {log}")
