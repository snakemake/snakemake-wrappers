"""Snakemake wrapper for SnpSift annotate"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2020, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

import os

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")
min_threads = 1

incall = snakemake.input["call"]
if snakemake.input["call"].endswith("bcf"):
    min_threads += 1
    incall = "< <(bcftools view {})".format(incall)
elif snakemake.input["call"].endswith("gz"):
    min_threads += 1
    incall = "< <(gunzip -c {})".format(incall)

outcall = snakemake.output["call"]
if snakemake.output["call"].endswith("gz"):
    min_threads += 1
    outcall = "| gzip -c > {}".format(outcall)
elif snakemake.output["call"].endswith("bcf"):
    min_threads += 1
    outcall = "| bcftools view > {}".format(outcall)
else:
    outcall = "> {}".format(outcall)

if snakemake.threads < min_threads:
    raise ValueError(
        "At least {} threads required, {} provided".format(
            min_threads, snakemake.threads
        )
    )

os.system(
    f"SnpSift annotate"  # Tool and its subcommand
    f" {extra}"  # Extra parameters
    f" {snakemake.input.database}"  # Path to annotation vcf file
    f" {incall} "  # Path to input vcf file
    f" {outcall} "  # Path to output vcf file
    f" {log}"  # Logging behaviour
)
