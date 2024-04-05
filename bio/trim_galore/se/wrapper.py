"""Snakemake wrapper for trimming unpaired reads using trim_galore."""

__author__ = "Kerrin Mendler"
__copyright__ = "Copyright 2018, Kerrin Mendler"
__email__ = "mendlerke@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import os
import re
import tempfile


def report_filename(infile: str) -> str:
    """Infer report output file name from input
    >>> report_filename('reads/sample.fastq.gz')
    'sample.fastq.gz_trimming_report.txt'
    """
    return os.path.basename(infile) + "_trimming_report.txt"


def fasta_filename(infile: str, out_gzip: bool) -> str:
    """Infer fasta output file name from input
    >>> fasta_filename('reads/sample.fq.gz', out_gzip = False)
    'sample_trimmed.fq.gz'
    >>> fasta_filename('reads/sample.fastq.gz', out_gzip = False)
    'sample_trimmed.fq.gz'
    >>> fasta_filename('reads/sample.fastq', out_gzip = False)
    'sample_trimmed.fq'
    >>> fasta_filename('reads/sample.fastq', out_gzip = True)
    'sample_trimmed.fq.gz'
    """
    base_input = os.path.basename(infile)
    suffix = ".gz" if out_gzip or infile.endswith(".gz") else ""
    REGEX_RULES = [r"\.fastq$", "\.fastq\.gz$", r"\.fq$", r"\.fq\.gz$"]
    for regex in REGEX_RULES:
        if re.search(regex, base_input):
            return re.sub(regex, "_trimmed.fq", base_input) + suffix
    return base_input + "_trimmed.fq" + suffix


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

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
infile = snakemake.input[0]

# Check that two output files were supplied
m = len(snakemake.output)
assert m == 2, "Output must contain 2 files. Given: %r." % m
fasta, report = (snakemake.output.get(key) for key in ["fasta", "report"])

out_gzip = fasta.endswith("gz")
if out_gzip:
    extra += " --gzip"

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "(trim_galore"
        " {extra}"
        " --cores {snakemake.threads}"
        " -o {tmpdir}"
        " {infile})"
        " {log}"
    )
    if report:
        shell(f"mv {tmpdir}/{report_filename(infile)} {report}")

    if fasta:
        shell(f"mv {tmpdir}/{fasta_filename(infile, out_gzip)} {fasta}")
