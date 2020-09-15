"""Snakemake wrapper for SnpSift gwasCat"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2020, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")

min_threads = 1

# Uncompression shall be done based on user input
incall = snakemake.input["call"]
if incall.endswith("bcf"):
    min_threads += 1
    incall = "< <(bcftools view {})".format(incall)
elif incall.endswith("gz"):
    min_threads += 1
    incall = "< <(gunzip -c {})".format(incall)


# Compression shall be done based on user-defined output
outcall = snakemake.output["call"]
if outcall.endswith("bcf"):
    min_threads += 1
    outcall = "| bcftools view {}".format(outcall)
elif outcall.endswith("gz"):
    min_threads += 1
    outcall = "| gzip -c > {}".format(outcall)
else:
    outcall = "> {}".format(outcall)


# Each additional (un)compression step requires more threads
if snakemake.threads < min_threads:
    raise ValueError(
        "At least {} threads required, {} provided".format(
            min_threads, snakemake.threads
        )
    )

shell(
    "SnpSift gwasCat "  # Tool and its subcommand
    " {extra} "  # Extra parameters
    " -db {snakemake.input.gwascat} "  # Path to gwasCat file
    " {incall} "  # Path to input vcf file
    " {outcall} "  # Path to output vcf file
    " {log} "  # Logging behaviour
)
