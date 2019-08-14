"""Snakemake wrapper for Strelka"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell
from snakemake.utils import makedirs

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

config_extra = snakemake.params.get("config_extra", "")
run_extra = snakemake.params.get("run_extra", "")

# If a normal bam is given in input,
# then it should be provided in the input
# block, so Snakemake will perform additional
# tests on file existance.
normal = (
    "--normalBam {}".format(snakemake.input["normal"])
    if "normalBam" in snakemake.input.keys()
    else ""
)

makedirs(snakemake.output)

shell(
    "(configureStrelkaSomaticWorkflow.py "       # Configuration script
    "{normal} "                                  # Path to normal bam (if any)
    "--tumorBam {snakemake.input.tumor} "        # Path to tumor bam
    "--referenceFasta {snakemake.input.fasta} "  # Path to fasta file
    "--runDir {snakemake.output} "               # Path to output directory
    " && "
    "{snakemake.output}/runWorkflow.py "         # Run the pipeline
    "--mode local "                              # Stop internal job submission
    "--jobs {snakemake.threads}) "                         # Nomber of threads
    "{log}"                                      # Logging behaviour
)
