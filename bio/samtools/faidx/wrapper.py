__author__ = "Michael Chambers"
__copyright__ = "Copyright 2019, Michael Chambers"
__email__ = "greenkidneybean@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import get_samtools_opts

samtools_opts = get_samtools_opts(
    snakemake, parse_threads=False, parse_write_index=False, parse_output_format=False
)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


# Get regions (if present)
regions = snakemake.input.get("regions", "")
if regions:
    regions = f"--region-file {regions}"

region = snakemake.params.get("region", "")


# Get FAI and GZI files
if region or regions:
    fai = snakemake.input.get("fai", "")
    gzi = snakemake.input.get("gzi", "")
else:
    fai = snakemake.output.get("fai", "")
    gzi = snakemake.output.get("gzi", "")

if fai:
    fai = f"--fai-idx {fai}"
if gzi:
    gzi = f"--gzi-idx {gzi}"


shell(
    "samtools faidx {fai} {gzi} {regions} {samtools_opts} {extra} {snakemake.input[0]} {region:q} {log}"
)
