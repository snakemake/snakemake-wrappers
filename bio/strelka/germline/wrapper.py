__author__ = "Jan Forster"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "jan.forster@uk-essen.de"
__license__ = "MIT"


import os
from snakemake.shell import shell

config_extra = snakemake.params.get("config_extra", "")
run_extra = snakemake.params.get("run_extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

bam = snakemake.input.get("bam") # input bam file, required
assert bam is not None, "input-> bam is a required input parameter"

shell(
    "configureStrelkaGermlineWorkflow.py " # configure the strelka run
    "--bam {bam} " # input bam
    "--referenceFasta {snakemake.params.ref} " # reference genome
    "--runDir {snakemake.output} " # output directory
    "{config_extra} " # additional parameters for the configuration
    "&& {snakemake.output}/runWorkflow.py " # run the strelka workflow
    "-m local " # run in local mode
    "-j {snakemake.threads} " # number of threads
    "{run_extra} " # additional parameters for the run
    "{log}") # logging
