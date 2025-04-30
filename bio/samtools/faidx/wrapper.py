__author__ = "Michael Chambers"
__copyright__ = "Copyright 2019, Michael Chambers"
__email__ = "greenkidneybean@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import get_samtools_opts

samtools_opts = get_samtools_opts(
    snakemake, parse_write_index=False, parse_output_format=False
)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
region = snakemake.params.get("region", "")

# Get FAI and GZI files
fai = snakemake.input.get("fai", snakemake.output.get("fai", ""))
if fai:
    fai = f"--fai-idx {fai}"
gzi = snakemake.input.get("gzi", snakemake.output.get("gzi", ""))
if gzi:
    gzi = f"--gzi-idx {gzi}"


shell(
    "samtools faidx {fai} {gzi} {samtools_opts} {extra} {snakemake.input[0]} {region:q} {log}"
)
