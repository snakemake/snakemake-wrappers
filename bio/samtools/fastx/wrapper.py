__author__ = "William Rowell"
__copyright__ = "Copyright 2020, William Rowell"
__email__ = "wrowell@pacb.com"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import get_samtools_opts

samtools_opts = get_samtools_opts(
    snakemake, parse_write_index=False, parse_output_format=False
)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


shell(
    "samtools {snakemake.params.outputtype} {samtools_opts} {extra} {snakemake.input} {log}"
)
