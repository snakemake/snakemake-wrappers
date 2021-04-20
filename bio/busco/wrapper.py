"""Snakemake wrapper for BUSCO assessment"""

__author__ = "Tessa Pierce"
__copyright__ = "Copyright 2018, Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
from os import path
import tempfile

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")
mode = snakemake.params.get("mode")
assert mode is not None, "please input a run mode: genome, transcriptome or proteins"
lineage = snakemake.params.get("lineage_path")
assert lineage is not None, "please input the path to a lineage for busco assessment"

# busco does not allow you to direct output location: handle this by moving output
outdir = snakemake.output[0]
download_path_dir = snakemake.params.get("download_path", "")
download_path = " --download_path {download_path_dir} " if download_path_dir else ""

# note: --force allows snakemake to handle rewriting files as necessary
# without needing to specify *all* busco outputs as snakemake outputs
with tempfile.TemporaryDirectory(prefix="busco_", dir="") as tmp_dir:
    shell(
        "busco --in {snakemake.input} --out {tmp_dir} --force "
        "--cpu {snakemake.threads} --mode {mode} --lineage {lineage} "
        "{download_path} "
        "{extra} {log}"
    )

    # move to intended location
    shell("cp -r {tmp_dir} {outdir}")
