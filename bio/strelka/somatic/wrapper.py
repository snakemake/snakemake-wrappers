"""Snakemake wrapper for Strelka"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

import os
from pathlib import Path

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

config_extra = snakemake.params.get("config_extra", "")
run_extra = snakemake.params.get("run_extra", "")

# If a normal bam is given in input,
# then it should be provided in the input
# block, so Snakemake will perform additional
# tests on file existance.
normal = (
    "--normalBam {}".format(snakemake.input["normal"])
    if "normal" in snakemake.input.keys()
    else ""
)

if snakemake.output[0].endswith("vcf.gz"):
    run_dir = Path(snakemake.output[0]).parents[2]
else:
    run_dir = snakemake.output

os.system(
    "(configureStrelkaSomaticWorkflow.py "  # Configuration script
    "%s "  # Path to normal bam (if any)
    "--tumorBam %s "  # Path to tumor bam
    "--referenceFasta %s "  # Path to fasta file
    "--runDir %s "  # Path to output directory
    "%s "  # Extra parametersfor configuration
    " && "
    "%s/runWorkflow.py "  # Run the pipeline
    "--mode local "  # Stop internal job submission
    "--jobs %s "  # Nomber of threads
    "%s) "  # Extra parameters for runWorkflow
    "%s"
    % (
        normal,
        snakemake.input.tumor,
        snakemake.input.fasta,
        run_dir,
        config_extra,
        run_dir,
        snakemake.threads,
        run_extra,
        log,
    )
)
