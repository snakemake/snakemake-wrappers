"""Snakemake wrapper for barrnap."""

__author__ = "Curro Campuzano Jiménez"
__copyright__ = "Copyright 2023, Curro Campuzano Jiménez"
__email__ = "campuzanocurro@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")

assert snakemake.output.keys(), "Output must contain at least one named file."

valid_keys = ["gff", "fasta"]
for key in snakemake.output.keys():
    assert (
        key in valid_keys
    ), "Invalid key in output. Valid keys are: %r. Given: %r." % (valid_keys, key)

gff_out = snakemake.output.get("gff")
fasta_out = snakemake.output.get("fasta")

if fasta_out:
    extra += f" -o {fasta_out}"

shell(
    "barrnap"
    " --threads {snakemake.threads}"
    " {extra}"
    " < {snakemake.input}"
    " > {gff_out}"
    " {log}"
)
