__author__ = "Hamdiye Uzuner"
__copyright__ = "Copyright 2024, Hamdiye Uzuner"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
        "orthanq candidates virus --genome {snakemake.input.genome} --lineages "
        " {snakemake.input.lineages} --output {snakemake.output[0]} {log}"
)
