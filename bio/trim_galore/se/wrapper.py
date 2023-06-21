"""Snakemake wrapper for trimming unpaired reads using trim_galore."""

__author__ = "Kerrin Mendler"
__copyright__ = "Copyright 2018, Kerrin Mendler"
__email__ = "mendlerke@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import os
import tempfile


log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Don't run with `--fastqc` flag
if "--fastqc" in snakemake.params.get("extra", ""):
    raise ValueError(
        "The trim_galore Snakemake wrapper cannot "
        "be run with the `--fastqc` flag. Please "
        "remove the flag from extra params. "
        "You can use the fastqc Snakemake wrapper on "
        "the input and output files instead."
    )
# Check that input files were supplied
n = len(snakemake.input)
assert n == 1, "Input must contain 1 files. Given: %r." % n

# Check that two output files were supplied
m = len(snakemake.output)
assert m == 2, "Output must contain 2 files. Given: %r." % m

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "(trim_galore"
        " {snakemake.params.extra}"
        " -o {tmpdir}"
        " {snakemake.input})"
        " {log}"
    )
    # Get all files in tmpdir
    fasta, report = (snakemake.output.get(key) for key in ["fasta", "report"])

    if fasta:
        file = [f for f in os.listdir(tmpdir) if "_trimmed" in f][0]
        shell("mv {tmpdir}/{file} {fasta}")

    if report:
        # Get filename from snakemake.input[0]
        file = f"{os.path.basename(snakemake.input[0])}_trimming_report.txt"
        shell("mv {tmpdir}/{file} {report}")
