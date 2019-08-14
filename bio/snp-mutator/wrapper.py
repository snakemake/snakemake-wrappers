"""Snakemake wrapper for SNP Mutator."""

__author__ = "Michael Hall"
__copyright__ = "Copyright 2019, Michael Hall"
__email__ = "mbhall88@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
from pathlib import Path

# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")
num_simulations = snakemake.params.get("num_simulations", 100)
fasta_outdir = Path(snakemake.output.sequences[0]).absolute().parent
# Formats the log redrection string
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Executed shell command
shell(
    "snpmutator {extra} "
    "--num-simulations {num_simulations} "
    "--vcf {snakemake.output.vcf} "
    "-F {fasta_outdir} "
    "{snakemake.input} {log} "
)
