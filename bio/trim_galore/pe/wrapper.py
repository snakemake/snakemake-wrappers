"""Snakemake wrapper for trimming paired-end reads using trim_galore."""

__author__ = "Kerrin Mendler"
__copyright__ = "Copyright 2018, Kerrin Mendler"
__email__ = "mendlerke@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import tempfile
import re
import os


def report_filename(infile: str) -> str:
    """Infer report output file name from input
    >>> report_filename('reads/sample.1.fastq.gz')
    'sample.1.fastq.gz_trimming_report.txt
    >>> report_filename('reads/sample_R2.fastq.gz')
    'sample_R2.fastq.gz_trimming_report.txt
    """
    return os.path.basename(infile) + "_trimming_report.txt"


def fasta_filename(infile: str, infix: str, out_gzip: bool) -> str:
    """Infer fasta output file name from input
    >>> fasta_filename('reads/sample.1.fq.gz', infix = '_val_1', out_gzip = False)
    'sample.1_val_1.fq.gz'
    >>> fasta_filename('reads/sample_R2.fastq', infix = '_val_2', out_gzip = True)
    'sample_R2_val_2.fq.gz'
    """
    base_input = os.path.basename(infile)
    suffix = ".gz" if out_gzip or infile.endswith(".gz") else ""
    REGEX_RULES = [r"\.fastq$", "\.fastq\.gz$", r"\.fq$", r"\.fq\.gz$"]
    for regex in REGEX_RULES:
        if re.search(regex, base_input):
            return re.sub(regex, f"{infix}.fq", base_input) + suffix
    return base_input + infix + suffix


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

# Check that two input files were supplied
n = len(snakemake.input)
assert n == 2, "Input must contain 2 files. Given: %r." % n
infile_fwd, infile_rev = snakemake.input[0:2]

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

out_gzip = any((fasta_fwd.endswith("gz"), fasta_rev.endswith("gz")))
if out_gzip:
    extra += " --gzip"

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "(trim_galore"
        " {extra}"
        " --cores {snakemake.threads}"
        " --paired"
        " -o {tmpdir}"
        " {infile_fwd} {infile_rev})"
        " {log}"
    )

    if report_fwd:
        shell(f"mv {tmpdir}/{report_filename(infile_fwd)} {report_fwd}")
    if report_rev:
        shell(f"mv {tmpdir}/{report_filename(infile_rev)} {report_rev}")

    if fasta_fwd:
        shell(
            f"mv {tmpdir}/{fasta_filename(infile_fwd, '_val_1', out_gzip)} {fasta_fwd}"
        )
    if fasta_rev:
        shell(
            f"mv {tmpdir}/{fasta_filename(infile_rev, '_val_2', out_gzip)} {fasta_rev}"
        )
