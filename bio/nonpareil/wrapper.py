__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

from os import path
import tempfile
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

uncomp = ""
in_name, in_ext = path.splitext(snakemake.input[0])
if in_ext in [".gz", ".bz2"]:
    uncomp = "zcat" if in_ext == ".gz" else "bzcat"
    in_name, in_ext = path.splitext(in_name)

# Infer output format
if in_ext in [".fa", ".fas", ".fasta"]:
    in_format = "fasta"
elif in_ext in [".fq", ".fastq"]:
    in_format = "fastq"
else:
    raise ValueError("invalid input format")

# Redundancy summary
redund_sum = snakemake.output.get("redund_sum", "")
if redund_sum:
    redund_sum = f"-o {redund_sum}"

# Redundancy values
redund_val = snakemake.output.get("redund_val", "")
if redund_val:
    redund_val = f"-a {redund_val}"

# Mate distribution
mate_distr = snakemake.output.get("mate_distr", "")
if mate_distr:
    mate_distr = f"-C {mate_distr}"

# Log
out_log = snakemake.output.get("log", "")
if out_log:
    out_log = f"-l {out_log}"


with tempfile.NamedTemporaryFile() as tmp:
    in_uncomp = snakemake.input[0]
    if uncomp:
        in_uncomp = tmp.name
        shell("{uncomp} {snakemake.input[0]} > {in_uncomp}")

    shell(
        "nonpareil"
        " -T {snakemake.params.alg}"
        " -s {in_uncomp}"
        " -f {in_format}"
        " {extra}"
        " {redund_sum}"
        " {redund_val}"
        " {mate_distr}"
        " {out_log}"
        " {log}"
    )
