"""Snakemake wrapper for Salmon Index."""

__author__ = "Tessa Pierce"
__copyright__ = "Copyright 2018, Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
from tempfile import TemporaryDirectory

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

decoys = ""
if "decoys" in snakemake.input.keys():
    decoys = "--decoys {}".format(snakemake.input["decoys"])

resources_tmp = snakemake.resources.get("tmpdir", None)
with TemporaryDirectory(dir=resources_tmp) as tempdir:
    shell(
        "salmon index "
        "--transcripts {snakemake.input.sequences} "
        "--index {snakemake.output} "
        "--threads {snakemake.threads} "
        "--tmpdir {tempdir} "
        "{decoys} "
        "{extra} "
        "{log}"
    )
