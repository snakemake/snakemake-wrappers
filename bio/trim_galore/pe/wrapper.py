"""Snakemake wrapper for trimming paired-end reads using trim_galore."""

__author__ = "Kerrin Mendler"
__copyright__ = "Copyright 2018, Kerrin Mendler"
__email__ = "mendlerke@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import tempfile
import os


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")
# Check that two input files were supplied
n = len(snakemake.input)
assert n == 2, "Input must contain 2 files. Given: %r." % n

# Don't run with `--fastqc` flag
if "--fastqc" in snakemake.params.get("extra", ""):
    raise ValueError(
        "The trim_galore Snakemake wrapper cannot "
        "be run with the `--fastqc` flag. Please "
        "remove the flag from extra params. "
        "You can use the fastqc Snakemake wrapper on "
        "the input and output files instead."
    )

# Check that four output files were supplied
m = len(snakemake.output)
assert m == 4, "Output must contain 4 files. Given: %r." % m

fasta_fwd, fasta_rev, report_fwd, report_rev = (
    snakemake.output.get(key)
    for key in ["fasta_fwd", "fasta_rev", "report_fwd", "report_rev"]
)

if fasta_fwd.endswith("gz") and fasta_rev.endswith("gz"):
    extra += " --gzip"

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "(trim_galore"
        " {extra}"
        " --cores {snakemake.threads}"
        " --paired"
        " -o {tmpdir}"
        " {snakemake.input})"
        " {log}"
    )

    if report_fwd:
        # Get filename from snakemake.input[0]
        file = f"{os.path.basename(snakemake.input[0])}_trimming_report.txt"
        shell("mv {tmpdir}/{file} {report_fwd}")

    if report_rev:
        file = f"{os.path.basename(snakemake.input[1])}_trimming_report.txt"
        shell("mv {tmpdir}/{file} {report_rev}")

    if fasta_fwd:
        shell("mv {tmpdir}/*_val_1* {fasta_fwd}")

    if fasta_rev:
        shell("mv {tmpdir}/*_val_2* {fasta_rev}")
