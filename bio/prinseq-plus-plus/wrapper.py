"""Snakemake wrapper for Prinseq++"""

__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell
from pathlib import Path


log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=False)
extra = snakemake.params.get("extra", "")


# Input files
input_pe = len(snakemake.input) == 2
file2 = f"-fastq2 {snakemake.input[1]}" if input_pe else ""


# Input format
in_fmt = Path(snakemake.input[0].removesuffix(".gz")).suffix
if in_fmt in [".fq", ".fastq"]:
    pass
elif in_fmt in [".fas", ".fna", ".fasta"]:
    extra += " -FASTA"
else:
    raise ValueError("Invalid input file format")


# Output format
out_fmt = Path(snakemake.output[0]).suffix
out_suffix = ""
if out_fmt == ".gz":
    extra += " -out_gz"
    out_suffix = out_fmt
    out_fmt = Path(snakemake.output[0].removesuffix(".gz")).suffix
if out_fmt in [".fq", ".fastq"]:
    extra += " -out_format 0"
    out_suffix = f".fastq{out_suffix}"
elif out_fmt in [".fas", ".fna", ".fasta"]:
    extra += " -out_format 1"
    out_suffix = f".fasta{out_suffix}"
else:
    raise ValueError("Invalid output file format")


# Run Prinseq++
with tempfile.TemporaryDirectory() as tmpdir:
    out_prefix = "out"

    shell(
        "prinseq++ -threads {snakemake.threads} -fastq {snakemake.input[0]} {file2} {extra} -out_name {tmpdir}/{out_prefix} {log}"
    )

    if out := snakemake.output.get("r1"):
        out_pe = "_R1" if input_pe else ""
        shell("mv {tmpdir}/{out_prefix}_good_out{out_pe}{out_suffix} {out}")
    if out := snakemake.output.get("r2"):
        out_pe = "_R2" if input_pe else ""
        shell("mv {tmpdir}/{out_prefix}_good_out{out_pe}{out_suffix} {out}")
    if out := snakemake.output.get("r1_single"):
        out_pe = "_R1" if input_pe else ""
        shell("mv {tmpdir}/{out_prefix}_single_out{out_pe}{out_suffix} {out}")
    if out := snakemake.output.get("r2_single"):
        out_pe = "_R2" if input_pe else ""
        shell("mv {tmpdir}/{out_prefix}_single_out{out_pe}{out_suffix} {out}")
    if out := snakemake.output.get("r1_bad"):
        out_pe = "_R1" if input_pe else ""
        shell("mv {tmpdir}/{out_prefix}_bad_out{out_pe}{out_suffix} {out}")
    if out := snakemake.output.get("r2_bad"):
        out_pe = "_R2" if input_pe else ""
        shell("mv {tmpdir}/{out_prefix}_bad_out{out_pe}{out_suffix} {out}")
