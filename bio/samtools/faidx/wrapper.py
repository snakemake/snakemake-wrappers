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

shell("samtools faidx {samtools_opts} {extra} {snakemake.input[0]} {log}")
