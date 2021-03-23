__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2020, Filipe G. Vieira"
__license__ = "MIT"


from os import path
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

out_name, out_ext = path.splitext(snakemake.output[0])
out_ext = out_ext[1:].upper()

shell(
    "samtools calmd --threads {snakemake.threads} {snakemake.params} --output-fmt {out_ext} {snakemake.input.aln} {snakemake.input.ref} > {snakemake.output[0]} {log}"
)
