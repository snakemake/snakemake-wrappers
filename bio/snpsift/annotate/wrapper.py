"""Snakemake wrapper for SnpSift annotate"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2020, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell

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

shell(
    "SnpSift annotate"  # Tool and its subcommand
    " {extra}"  # Extra parameters
    " {snakemake.input.database}"  # Path to annotation vcf file
    " {incall} "  # Path to input vcf file
    " {outcall} "  # Path to output vcf file
    " {log}"  # Logging behaviour
)
