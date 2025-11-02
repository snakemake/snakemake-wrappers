__author__ = "Felix Wiegand"
__copyright__ = "Copyright 2025, Felix Wiegand"
__email__ = "felix.wiegand@uni-due.de"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")
output = snakemake.output[0]

cmd = ["alignoth"]

# BAM input
if snakemake.input.get("bam", ""):
    if snakemake.input.get("bam_idx", ""):
        cmd.append(f"-b {snakemake.input.bam}")
    else:
        raise ValueError("BAM input given without bai index")
else:
    raise ValueError("BAM input required")

# Reference
if snakemake.input.get("reference", ""):
    if snakemake.input.get("reference_idx", ""):
        cmd.append(f"-r {snakemake.input.reference}")
    else:
        raise ValueError("Reference input given without fai index")
else:
    raise ValueError("Reference input required")

# Optional VCF with required csi/tbi index
if snakemake.input.get("vcf", ""):
    if snakemake.input.get("vcf_idx", ""):
        cmd.append(f"-v {snakemake.input.vcf}")
    else:
        raise ValueError("VCF input given without csi/tbi index")

# Optional BED
if snakemake.input.get("bed", ""):
    cmd.append(f"--bed {snakemake.input.bed}")

cmd.append(f"{extra}")

# HTML output
if output.endswith(".html"):
    cmd.append("--html")
    shell(f"{' '.join(cmd)} > {output} {log}")
# Default: JSON output to single file via stdout
elif output.endswith(".json"):
    shell(f"{' '.join(cmd)} > {output} {log}")
# Assume output is directory
else:
    cmd.append(f"-o {output}")
    shell(f"{' '.join(cmd)} {log}")
