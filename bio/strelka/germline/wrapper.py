__author__ = "Jan Forster"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "jan.forster@uk-essen.de"
__license__ = "MIT"


import os
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

bam = snakemake.input.get("bam")
assert bam is not None, "input-> bam is a required input parameter"


rundir = snakemake.output[0].split("/results/variants/")[0]

shell(
    "configureStrelkaGermlineWorkflow.py "
    "--bam {bam} "
    "--referenceFasta {snakemake.params.ref} "
    "--runDir {rundir} "
    "--callRegions {snakemake.params.callRegions "
    "{params.extra} > {log}"
    "&& {rundir}/runworkflow.py -m local "
    "-j {snakemake.threads} "
    ">> {log}")
