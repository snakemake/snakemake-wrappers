"""Snakemake wrapper for gridss assemble"""

__author__ = "Christopher Schröder"
__copyright__ = "Copyright 2020, Christopher Schröder"
__email__ = "christopher.schroede@tu-dortmund.de"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell
from os import path

# Creating log
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")

# Check inputs/arguments.
reference = snakemake.input.get("reference")

if not snakemake.params.workingdir:
    raise ValueError("Please set params.workingdir to provide a working directory.")

if not snakemake.input.reference:
    raise ValueError("Please set input.reference to provide reference genome.")

for ending in (".amb", ".ann", ".bwt", ".pac", ".sa", ".dict"):
    if not path.exists("{}{}".format(reference, ending)):
        raise ValueError(
            "{reference}{ending} missing. Please make sure the reference was properly indexed by bwa.".format(
                reference=reference, ending=ending
            )
        )

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "(gridss -s assemble "  # Tool
        "--reference {reference} "  # Reference
        "--threads {snakemake.threads} "  # Threads
        "--workingdir {snakemake.params.workingdir} "  # Working directory
        "--assembly {snakemake.output.assembly} "  # Assembly output
        "--picardoptions TMP_DIR={tmpdir} "
        "{snakemake.input.bam} "
        "{extra}"
        ") {log}"
    )
