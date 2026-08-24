"""Snakemake wrapper for falco."""

__author__ = "Yoann Pradat"
__copyright__ = "Copyright 2025, Yoann Pradat"
__email__ = "yoann.pradat@gustaveroussy.fr"
__license__ = "MIT"

from pathlib import Path
from tempfile import TemporaryDirectory
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import move_files

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# We use a temp dir to clean up intermediate files.
with TemporaryDirectory() as tempdir:
    # Get input file basename
    basename = Path(snakemake.input[0].removesuffix(".gz")).with_suffix("").name
    mapping = {
        "html": Path(tempdir) / basename / "fastqc_report.html",
        "data": Path(tempdir) / basename / "fastqc_data.txt",
        "summ": Path(tempdir) / basename / "summary.txt",
    }

    shell(
        "falco"
        " --threads {snakemake.threads}"
        " --mem {snakemake.resources.mem_mb}M"
        " {extra}"
        " --output {tempdir:q}"
        " {snakemake.input[0]:q}"
        " {log}"
    )

    log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
    for move_cmd in move_files(snakemake, mapping):
        shell("{move_cmd} {log}")
