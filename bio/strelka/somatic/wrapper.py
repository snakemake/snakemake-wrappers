__author__ = "Jan Forster"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "jan.forster@uk-essen.de"
__license__ = "MIT"


import os
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

normal = snakemake.input.get("normal")
assert normal is not None, "input-> normal is a required input parameter"
tumor = snakemake.input.get("tumor")
assert tumor is not None, "input-> tumor is a required input parameter"

rundir = snakemake.output[0].split("/results/variants/")[0]

shell(
    "configureStrelkaSomaticWorkflow.py "
    "--normalBam {normal} "
    "-tumorBam {tumor} "
    "--referenceFasta {snakemake.params.ref} "
    "--runDir {rundir} "
    "--callRegions {snakemake.params.callRegions "
    "{params.extra} > {log}"
    "&& {rundir}/runworkflow.py -m local "
    "-j {snakemake.threads} "
    ">> {log}")
