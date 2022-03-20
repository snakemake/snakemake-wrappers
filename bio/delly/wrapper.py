__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.bcftools import get_bcftools_opts


bcftools_opts = get_bcftools_opts(snakemake, parse_memory=False)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


exclude = (
    "-x {}".format(snakemake.input.exclude)
    if snakemake.input.get("exclude", "")
    else ""
)


with NamedTemporaryFile().name as tmpout:
    shell(
        "(OMP_NUM_THREADS={snakemake.threads} delly call"
        " -g {snakemake.input.ref}"
        " -o {tmpout}"
        " {exclude}"
        " {extra}"
        " {snakemake.input[0]};"
        # Convert output to specified format
        "bcftools view"
        " {bcftools_opts}"
        " {tmpout}"
        ") {log}"
    )
