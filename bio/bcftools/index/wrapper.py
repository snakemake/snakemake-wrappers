__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.bcftools import get_bcftools_opts


bcftools_opts = get_bcftools_opts(
    snakemake, parse_ref=False, parse_output_format=False, parse_memory=False
)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


if "--tbi" in extra or "--csi" in extra:
    raise ValueError(
        "You have specified index format (`--tbi/--csi`) in `params.extra`; this is automatically infered from the first output file."
    )

if snakemake.output[0].endswith(".tbi"):
    extra += " --tbi"
elif snakemake.output[0].endswith(".csi"):
    extra += " --csi"
else:
    raise ValueError("invalid index file format ('.tbi', '.csi').")


shell("bcftools index {bcftools_opts} {extra} {snakemake.input[0]} {log}")
