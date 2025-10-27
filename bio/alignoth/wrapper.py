__author__ = "Felix Wiegand"
__copyright__ = "Copyright 2025, Felix Wiegand"
__email__ = "felix.wiegand@uni-due.de"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

cmd = ["alignoth"]

# BAM input
if snakemake.input.get("bam", ""):
    cmd.append(f"-b {snakemake.input.bam}")
else:
    raise ValueError("BAM input required")

# Reference
if snakemake.input.get("reference", ""):
    cmd.append(f"-r {snakemake.input.reference}")
else:
    raise ValueError("Reference input required")

# Optional VCF
if snakemake.input.get("vcf", ""):
    cmd.append(f"-v {snakemake.input.vcf}")

# Optional BED
if snakemake.input.get("bed", ""):
    cmd.append(f"--bed {snakemake.input.bed}")

cmd.append(f"{extra}")

# HTML output
if snakemake.output.html:
    cmd.append("--html")
    shell(f"{' '.join(cmd)} > {snakemake.output.html} {log}")
# Multiple files output into directory
elif snakemake.output.dir:
    cmd.append(f"-o {snakemake.output.dir}")
    shell(f"{' '.join(cmd)} {log}")
# Default: JSON output to single file via stdout
elif snakemake.output.json:
    shell(f"{' '.join(cmd)} > {snakemake.output.json} {log}")
else:
    raise ValueError("No output specified")
