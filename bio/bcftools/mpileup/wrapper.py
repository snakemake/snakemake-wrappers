__author__ = "Michael Hall"
__copyright__ = "Copyright 2020, Michael Hall"
__email__ = "michael@mbh.sh"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.bcftools import get_bcftools_opts


extra = snakemake.params.get("extra", "")
bcftools_opts = get_bcftools_opts(
    snakemake, parse_ref=("--no-reference" not in extra), parse_memory=False
)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


class MissingReferenceError(Exception):
    pass


shell("bcftools mpileup {bcftools_opts} {extra} {snakemake.input.alignments} {log}")
