# coding: utf-8

"""Snakemake-wrapper for pyfaidx"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2025, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake_wrapper_utils.snakemake import get_format
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=False)

bed = snakemake.input.get("bed", "")
if bed:
    extra += f" --bed {bed}"

out = str(snakemake.output[0])
fmt = get_format(out)
if fmt == "fai":
    out = ""
elif fmt == "fasta":
    out = f"--out {out}"
elif fmt == "bed":
    out = f"--out {out} --transform bed"
elif fmt == "chrom":
    out = f"--out {out} --transform chromsizes"
elif fmt == "nuc":
    out = f"--out {out} --transform nucleotide"

shell("faidx {extra} {out} {snakemake.input.fasta} {log}")
