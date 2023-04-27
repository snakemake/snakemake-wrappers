__author__ = "Jan Forster, Christopher Schröder"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "jan.forster@uk-essen.de"
__license__ = "MIT"

import os, shutil

from pathlib import Path
from snakemake.shell import shell

config_extra = snakemake.params.get("config_extra", "")
run_extra = snakemake.params.get("run_extra", "")
rm_existing = snakemake.params.get("rm_existing", False)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

bam = snakemake.input.get("bam")  # input bam file, required
assert bam is not None, "input-> bam is a required input parameter"
if isinstance(bam, str):
    bam = [bam]

if snakemake.output[0].endswith(".vcf.gz"):
    run_dir = Path(snakemake.output[0]).parents[2]
else:
    run_dir = snakemake.output

# delete existing run directory
if rm_existing and os.path.exists(run_dir):
    shutil.rmtree(run_dir)

bam_input = " ".join(f"--bam {b}" for b in bam)

shell(
    "(configureStrelkaGermlineWorkflow.py "  # configure the strelka run
    "{bam_input} "  # input bam
    "--referenceFasta {snakemake.input.fasta} "  # reference genome
    "--runDir {run_dir} "  # output directory
    "{config_extra} "  # additional parameters for the configuration
    "&& {run_dir}/runWorkflow.py "  # run the strelka workflow
    "-m local "  # run in local mode
    "-j {snakemake.threads} "  # number of threads
    "{run_extra}) "  # additional parameters for the run
    "{log}"
)  # logging
