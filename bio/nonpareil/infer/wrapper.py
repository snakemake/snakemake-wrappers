__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

from os import path
import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_mem


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")
mem_mb = get_mem(snakemake, out_unit="MiB")

uncomp = ""
in_name, in_ext = path.splitext(snakemake.input[0])
if in_ext in [".gz", ".bz2"]:
    uncomp = (
        f"pigz --processes {snakemake.threads} --decompress --stdout"
        if in_ext == ".gz"
        else f"pbzip2 -p{snakemake.threads} --decompress --stdout"
    )
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
    if uncomp:
        in_uncomp = tmp.name
        shell("{uncomp} {snakemake.input[0]} > {tmp.name}")
    else:
        in_uncomp = snakemake.input[0]

    # Auto infer -X value
    if snakemake.params.get("infer_X", True):
        # Get total number of lines
        total_n_lines = sum(1 for line in open(in_uncomp, "rb"))
        # Get total number of reads (depends on format)
        total_n_reads = total_n_lines / 4 if in_format == "fastq" else total_n_lines / 2
        # Get total number of reads to sample
        sample_n_reads = max(1, int(total_n_reads * 0.1) - 1)
        # Get total number of reads to sample, depending on defaults
        sample_n_reads = (
            min(1000, sample_n_reads)
            if snakemake.params.alg == "alignment"
            else min(10000, sample_n_reads)
        )
        extra += f" -X {sample_n_reads}"

    shell(
        "nonpareil"
        " -t {snakemake.threads}"
        " -R {mem_mb}"
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
