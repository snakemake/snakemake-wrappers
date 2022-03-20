__author__ = "Michael Hall"
__copyright__ = "Copyright 2020, Michael Hall"
__email__ = "michael@mbh.sh"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.bcftools import get_bcftools_opts


bcftools_opts = get_bcftools_opts(snakemake, parse_memory=False)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


class MissingReferenceError(Exception):
    pass


# determine if a fasta reference is provided or not and add to extra
if "--no-reference" not in extra:
    ref = snakemake.input.get("ref", "")
    if not ref:
        raise MissingReferenceError(
            "The --no-reference option was not given, but no fasta reference was "
            "provided."
        )
    extra += f" --fasta-ref {ref}"


shell("bcftools mpileup {extra} {snakemake.input[0]} {log}")
