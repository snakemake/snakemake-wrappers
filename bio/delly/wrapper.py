__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.bcftools import infer_out_format


exclude = (
    "-x {}".format(snakemake.input.exclude)
    if snakemake.input.get("exclude", "")
    else ""
)

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


# Infer output format
out_format = infer_out_format(
    snakemake.output[0], snakemake.params.get("uncompressed_bcf", False)
)


with NamedTemporaryFile().name as tmpout:
    shell(
        "(OMP_NUM_THREADS={snakemake.threads} delly call"
        " -g {snakemake.input.ref}"
        " -o {tmpout}"
        " {exclude}"
        " {extra}"
        " {snakemake.input.samples};"
        # Convert output to specified format
        "bcftools view"
        " -O {out_format}"
        " -o {snakemake.output[0]}"
        " {tmpout}"
        ") {log}"
    )
