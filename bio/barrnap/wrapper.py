"""Snakemake wrapper for barrnap."""

__author__ = "Curro Campuzano Jiménez"
__copyright__ = "Copyright 2023, Curro Campuzano Jiménez"
__email__ = "campuzanocurro@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")
kingdom = snakemake.params.get("kingdom", "bac")

fasta_out = snakemake.output.get("fasta")
if fasta_out:
    extra += f" -o {fasta_out}"

shell(
    "barrnap"
    " --threads {snakemake.threads}"
    " -k {kingdom}"
    " {extra}"
    " < {snakemake.input.fasta}"
    " > {snakemake.output.gff}"
    " {log}"
)
