"""Snakemake wrapper for Prinseq++"""

__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell
from pathlib import Path


log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=False)
extra = snakemake.params.get("extra", "")


ext_fq = [".fq", ".fastq"]
ext_fas = [".fas", ".fna", ".fasta"]


# Input files
input_pe = len(snakemake.input) == 2
file2 = f"-fastq2 {snakemake.input[1]}" if input_pe else ""

# Check input format
in_fmt = Path(snakemake.input[0].removesuffix(".gz")).suffix
if in_fmt in ext_fq:
    pass
elif in_fmt in ext_fas:
    extra += " -FASTA"
else:
    raise ValueError("Invalid input file format")


# Output files
out_fmt = Path(snakemake.output[0]).suffix
for key, value in snakemake.output.items():
    if out_fmt == ".gz":
        extra += f" -out_{key} >(bgzip --threads {snakemake.threads} > {value})"
    else:
        extra += f" -out_{key} {value}"

# Check output format
if out_fmt == ".gz":
    out_fmt = Path(snakemake.output[0].removesuffix(".gz")).suffix
if out_fmt in ext_fq:
    extra += " -out_format 0"
elif out_fmt in ext_fas:
    extra += " -out_format 1"
else:
    raise ValueError("Invalid output file format")


# Run Prinseq++
with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "prinseq++ -threads {snakemake.threads} -fastq {snakemake.input[0]} {file2} {extra} -out_name {tmpdir}/tmp {log}"
    )
