"""Snakemake wrapper for picard SortSam."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


import os


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

fastq1 = snakemake.output.fastq1
fastq2 = snakemake.output.get("fastq2", None)
fastq_unpaired = snakemake.output.get("unpaired_fastq", None)

if not isinstance(fastq1, str):
    raise ValueError("f1 needs to be provided")

output = " FASTQ=" + fastq1

if isinstance(fastq2, str):
    output += " SECOND_END_FASTQ=" + fastq2

if isinstance(fastq_unpaired, str):
    if not isinstance(fastq2, str):
        raise ValueError("f2 is required if fastq_unpaired is set")
    else:
        output += " UNPAIRED_FASTQ=" + fastq_unpaired

os.system(
    f"picard"
    " SamToFastq"
    " {extra}"
    " INPUT={snakemake.input[0]}"
    " {output}"
    " {log}"
)
