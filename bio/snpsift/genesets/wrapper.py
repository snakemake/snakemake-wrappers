"""Snakemake wrapper for SnpSift geneSets"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2020, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")
min_threads = 1

# Uncompression shall be done according to user-defined input
incall = snakemake.input["call"]
if snakemake.input["call"].endswith("bcf"):
    min_threads += 1
    incall = "< <(bcftools view {})".format(incall)
elif snakemake.input["call"].endswith("gz"):
    min_threads += 1
    incall = "< <(gunzip -c {})".format(incall)

# Compression shall be done according to user-defined output
outcall = snakemake.output["call"]
if snakemake.output["call"].endswith("gz"):
    min_threads += 1
    outcall = "| gzip -c > {}".format(outcall)
elif snakemake.output["call"].endswith("bcf"):
    min_threads += 1
    outcall = "| bcftools view > {}".format(outcall)
else:
    outcall = "> {}".format(outcall)

# Each (un)compression step raises the threads requirements
if snakemake.threads < min_threads:
    raise ValueError(
        "At least {} threads required, {} provided".format(
            min_threads, snakemake.threads
        )
    )


shell(
    "SnpSift geneSets"  # Tool and its subcommand
    " {java_opts} {extra}"  # Extra parameters
    " {snakemake.input.gmt}"  # Path to annotation vcf file
    " {incall}"  # Path to input vcf file
    " {outcall}"  # Path to output vcf file
    " {log}"  # Logging behaviour
)
