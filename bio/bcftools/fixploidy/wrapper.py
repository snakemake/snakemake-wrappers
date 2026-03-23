__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2026, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.bcftools import get_bcftools_opts


bcftools_opts = get_bcftools_opts(snakemake, parse_ref=False, parse_memory=False)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
min_threads = 1


# Uncompression shall be done according to user-defined input
incall = snakemake.input[0]
if snakemake.input["call"].endswith(("gz", "bcf")):
    min_threads += 1
    incall = "< <(bcftools view {})".format(incall)

# Compression shall be done according to user-defined output
outcall = snakemake.output[0]
if snakemake.output["call"].endswith(("gz", "bcf")):
    min_threads += 1
    outcall = "| bcftools view {} > {}".format(bcftools_opts, outcall)
else:
    outcall = "> {}".format(outcall)

# Each (un)compression step raises the threads requirements
if snakemake.threads < min_threads:
    raise ValueError(
        "At least {} threads required, {} provided".format(
            min_threads, snakemake.threads
        )
    )

shell("(bcftools plugin fixploidy {extra} {incall} {outcall}) {log}")
