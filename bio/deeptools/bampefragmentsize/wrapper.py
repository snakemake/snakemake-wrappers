__author__ = "Niek Wit"
__copyright__ = "Copyright 2025, Niek Wit"
__email__ = "niekwit@gmail.com"
__license__ = "MIT"

import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Get input files
bam_files = snakemake.input.get("bams", "")
blacklist = snakemake.input.get("blacklist", "")
if blacklist:
    blacklist = f"--blackListFileName {blacklist}"

# Get/create sample labels (remove .bam extension and dir)
# If no labels are provided, use the basename of the bam file
sample_label = snakemake.params.get("labels", "")
if not sample_label:
    sample_label = [os.path.basename(bam.replace(".bam", "")) for bam in bam_files]

# Check if the number of labels is equal to the number of bam files
assert len(sample_label) == len(
    bam_files
), "Number of labels must be equal to the number of bam files"

out_file = snakemake.output.get("hist")

# Check output format
out_format = out_file.split(".")[-1]
if not out_format in ["png", "pdf", "svg", "eps", "plotly"]:
    raise ValueError(
        "Output format must be either 'png', 'pdf', 'svg', 'eps', or 'plotly'"
    )

# Optional output
out_raw = snakemake.output.get("raw", "")
if out_raw:
    optional_output = " --outRawFragmentLengths {out_tab} ".format(out_tab=out_raw)

# Parameters
extra = snakemake.params.get("extra", "")

shell(
    "bamPEFragmentSize "
    "--numberOfProcessors {snakemake.threads} "
    "-b {bam_files} "
    "-o {out_file} "
    "{blacklist} {optional_output} {extra} {log}"
)
