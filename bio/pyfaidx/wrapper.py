# coding: utf-8

"""Snakemake-wrapper for pyfaidx"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2025, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell

extra: str = snakemake.params.get("extra", "")
log: str = snakemake.log_fmt_shell(stdout=True, stderr=True, append=False)

bed: str = snakemake.input.get("bed", "")
if bed:
    extra += f" --bed {bed} "

out: str = str(snakemake.output[0])
if out.endswith(".fai"):
    out = ""
elif out.endswith(".fasta"):
    out = f" --out {out} "
elif out.endswith(".bed"):
    out = f" --out {out} --transform bed "
elif out.endswith(".chrom"):
    out = f" --out {out} --transform chromsizes "
elif out.endswith(".nuc"):
    out = f" --out {out} --transform nucleotide "

shell("faidx {extra} {out} {snakemake.input.fasta} {log}")
