__author__ = "Niek Wit"
__copyright__ = "Copyright 2025, Niek Wit"
__email__ = "niekwit@gmail.com"
__license__ = "MIT"

from pathlib import Path
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Get input files
# Let Snakemake handle the error if bams are missing
bam_files = snakemake.input.bams
blacklist = snakemake.input.get("blacklist", "")
if blacklist:
    blacklist = f"--blackListFileName {blacklist}"

# Get/create sample labels (remove .bam extension and dir)
# If no labels are provided, use the basename of the bam file
sample_label = snakemake.params.get("labels", "")
if not sample_label:
    sample_label = [Path(bam).stem for bam in bam_files if Path(bam).suffix == ".bam"]

# Check if the number of labels is equal to the number of bam files
assert len(sample_label) == len(
    bam_files
), "Number of labels must be equal to the number of bam files"

# Check output format
out_format = Path(snakemake.output.hist).suffix
VALID_FORMATS = {".png", ".pdf", ".svg", ".eps", ".plotly"}
if out_format not in VALID_FORMATS:
    raise ValueError(
        f"Invalid output format '{out_format}'. Must be one of: {', '.join(sorted(VALID_FORMATS))}"
    )

# Optional output
out_raw = snakemake.output.get("raw", "")
if out_raw:
    out_raw = f"--outRawFragmentLengths {out_raw}"

# Parameters
extra = snakemake.params.get("extra", "")

shell(
    "bamPEFragmentSize "
    "--numberOfProcessors {snakemake.threads} "
    "-b {bam_files} "
    "-o {snakemake.output.hist} "
    "{blacklist} {out_raw} {extra} {log}"
)
