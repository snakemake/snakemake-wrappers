"""Snakemake wrapper for SnpSift gwasCat"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2020, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")
java_opts = ""
# Getting memory in megabytes, if java opts is not filled with -Xmx parameter
# By doing so, backward compatibility is preserved
if "mem_mb" in snakemake.resources.keys() and "-Xmx" not in extra:
    java_opts += " -Xmx{}M".format(snakemake.resources["mem_mb"])

# Getting memory in gigabytes, for user convenience. Please prefer the use
# of mem_mb over mem_gb as advised in documentation.
elif "mem_gb" in snakemake.resources.keys() and "-Xmx" not in extra:
    java_opts += " -Xmx{}G".format(snakemake.resources["mem_gb"])

# Getting java temp directory from output files list, if -Djava.io.tmpdir
# is not provided in java parameters. By doing so, backward compatibility is
# not broken.
if "java_temp" in snakemake.output.keys() and "-Djava.io.tmpdir" not in extra:
    java_opts += " -Djava.io.tmpdir={}".format(snakemake.output["java_temp"])


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
    " {java_opts} {extra} "  # Extra parameters
    " -db {snakemake.input.gwascat} "  # Path to gwasCat file
    " {incall} "  # Path to input vcf file
    " {outcall} "  # Path to output vcf file
    " {log} "  # Logging behaviour
)
