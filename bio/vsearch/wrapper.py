__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"

from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


fasta_arg = snakemake.params.get("fasta_arg", "")
if fasta_arg:
    fasta_arg = f"{fasta_arg} {snakemake.input.fasta}"


fastq_arg = snakemake.params.get("fastq_arg", "")
if fastq_arg:
    fastq_arg = f"{fastq_arg} {snakemake.input.fastq}"


db = snakemake.input.get("db", "")
if db:
    db = f"--db {db}"


out_arg = snakemake.params.get("out_arg", "")
if out_arg:
    out_arg = out_arg.replace("{", "{snakemake.")


out_log = snakemake.output.get("log", "")
if out_log:
    out_log = f"--log {out_log}"


shell(
    "vsearch --threads {snakemake.threads}"
    " {fasta_arg}"
    " {fastq_arg}"
    " {db}"
    " {extra}"
    " " + out_arg + " {out_log}"
    " {log}"
)
