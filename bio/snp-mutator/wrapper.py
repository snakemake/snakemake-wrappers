"""Snakemake wrapper for SNP Mutator."""

__author__ = "Michael Hall"
__copyright__ = "Copyright 2019, Michael Hall"
__email__ = "mbhall88@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")
num_simulations = snakemake.params.get("num_simulations", 100)
# Formats the log redrection string
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Executed shell command
shell(
    "snpmutator {extra} "
    "--num-simulations {num_simulations} "
    "--vcf {snakemake.output.vcf} "
    "{snakemake.input} {log} "
)
