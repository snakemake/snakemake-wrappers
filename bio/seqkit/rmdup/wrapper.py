__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


dup_num = snakemake.output.get("dup_num", "")
if dup_num:
    dup_num = f"--dup-num-file {dup_num}"


dup_seq = snakemake.output.get("dup_seq", "")
if dup_seq:
    dup_seq = f"--dup-seqs-file {dup_seq}"


shell(
    "seqkit rmdup"
    " --threads {snakemake.threads}"
    " {extra}"
    " --out-file {snakemake.output.fastx}"
    " {dup_num}"
    " {dup_seq}"
    " {snakemake.input.fastx}"
    " {log}"
)
