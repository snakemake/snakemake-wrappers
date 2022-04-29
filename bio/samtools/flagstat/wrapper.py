__author__ = "Christopher Preusch"
__copyright__ = "Copyright 2017, Christopher Preusch"
__email__ = "cpreusch[at]ust.hk"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import get_samtools_opts

samtools_opts = get_samtools_opts(
    snakemake, parse_write_index=False, parse_output=False, parse_output_format=False
)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "samtools flagstat {samtools_opts} {extra} {snakemake.input[0]} > {snakemake.output[0]} {log}"
)
