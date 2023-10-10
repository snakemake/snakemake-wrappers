"""Snakemake wrapper for ragtag-patch."""

__author__ = "Curro Campuzano Jiménez"
__copyright__ = "Copyright 2023, Curro Campuzano Jiménez"
__email__ = "campuzanocurro@gmail.com"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

assert snakemake.output.keys(), "Output must contain at least one named file."

valid_keys = [
    "agp",
    "fasta",
    "rename_agp",
    "rename_fasta",
    "comps_fasta",
    "ctg_agp",
    "ctg_fasta",
    "asm_dir",
]
for key in snakemake.output.keys():
    assert (
        key in valid_keys
    ), "Invalid key in output. Valid keys are: %r. Given: %r." % (valid_keys, key)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "ragtag.py patch"
        " {snakemake.input.ref}"
        " {snakemake.input.query}"
        " {extra}"
        " -o {tmpdir} -t {snakemake.threads}"
        " {log}"
    )
    for key in valid_keys[:-1]:
        outfile = snakemake.output.get(key)
        if outfile:
            extension = key.replace("_", ".")
            shell("mv {tmpdir}/ragtag.patch.{extension} {outfile}")
    outdir = snakemake.output.get("asm_dir")
    if outdir:
        # Move files into directory outdir
        shell("mkdir -p {outdir} && mv {tmpdir}/ragtag.patch.asm.* {outdir}")
