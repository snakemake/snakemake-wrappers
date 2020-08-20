__author__ = "Jan Forster"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "jan.forster@uk-essen.de"
__license__ = "MIT"


import os
from pathlib import Path

config_extra = snakemake.params.get("config_extra", "")
run_extra = snakemake.params.get("run_extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

bam = snakemake.input.get("bam")  # input bam file, required
assert bam is not None, "input-> bam is a required input parameter"

if snakemake.output[0].endswith(".vcf.gz"):
    run_dir = Path(snakemake.output[0]).parents[2]
else:
    run_dir = snakemake.output

os.system(
    f"configureStrelkaGermlineWorkflow.py "  # configure the strelka run
    f"--bam {bam} "  # input bam
    f"--referenceFasta {snakemake.input.fasta} "  # reference genome
    f"--runDir {run_dir} "  # output directory
    f"{config_extra} "  # additional parameters for the configuration
    f"&& {run_dir}/runWorkflow.py "  # run the strelka workflow
    f"-m local "  # run in local mode
    f"-j {snakemake.threads} "  # number of threads
    f"{run_extra} "  # additional parameters for the run
    f"{log}"
)  # logging
