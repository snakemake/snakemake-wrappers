"""Snakemake wrapper for Salmon Index."""

__author__ = "Tessa Pierce"
__copyright__ = "Copyright 2018, Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from os.path import dirname
from snakemake.shell import shell
from tempfile import TemporaryDirectory

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

decoys = snakemake.input.get("decoys", "")
if decoys:
    decoys = f"--decoys {decoys}"

output = snakemake.output
if len(output) > 1:
    output = dirname(snakemake.output[0])

with TemporaryDirectory() as tempdir:
    shell(
        "salmon index "
        "--transcripts {snakemake.input.sequences} "
        "--index {output} "
        "--threads {snakemake.threads} "
        "--tmpdir {tempdir} "
        "{decoys} "
        "{extra} "
        "{log}"
    )
