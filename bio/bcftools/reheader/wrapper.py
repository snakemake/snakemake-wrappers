__author__ = "Jan Forster"
__copyright__ = "Copyright 2020, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"


import tempfile
from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.bcftools import get_bcftools_opts


bcftools_opts = get_bcftools_opts(
    snakemake, parse_ref=False, parse_samples=False, parse_memory=False
)
extra = snakemake.params.get("extra", "")
view_extra = snakemake.params.get("view_extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)


## Extract arguments
header = snakemake.input.get("header", "")
if header:
    header = f"--header {header}"

samples = snakemake.input.get("samples", "")
if samples:
    samples = f"--samples {samples}"


with tempfile.TemporaryDirectory() as tmpdir:
    tmp_prefix = Path(tmpdir) / "bcftools_reheader."

    shell(
        "(bcftools reheader"
        " --threads {snakemake.threads}"
        " {header}"
        " {samples}"
        " {extra}"
        " --temp-prefix {tmp_prefix}"
        " {snakemake.input[0]}"
        "| bcftools view"
        " {bcftools_opts}"
        " {view_extra}"
        ") {log}"
    )
