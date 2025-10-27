__author__ = "Felix Wiegand"
__copyright__ = "Copyright 2025, Felix Wiegand"
__email__ = "felix.wiegand@uni-due.de"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

cmd = ["alignoth"]

# BAM input
if hasattr(snakemake.input, "bam"):
    cmd.append(f"-b {snakemake.input.bam}")
else:
    raise ValueError("BAM input required")

# Reference
if hasattr(snakemake.input, "reference"):
    cmd.append(f"-r {snakemake.input.reference}")
else:
    raise ValueError("Reference input required")

# Optional VCF
if hasattr(snakemake.input, "vcf"):
    cmd.append(f"-v {snakemake.input.vcf}")

# Optional BED
if hasattr(snakemake.input, "bed"):
    cmd.append(f"--bed {snakemake.input.bed}")

# Region / around
if "region" in snakemake.params:
    cmd.append(f"-g {snakemake.params.region}")
elif "around" in snakemake.params:
    cmd.append(f"-a {snakemake.params.around}")

# Optional highlights
if "highlight" in snakemake.params:
    for h in snakemake.params.highlight:
        cmd.append(f"-h {h}")

# Optional aux tags
if "aux_tags" in snakemake.params:
    for t in snakemake.params.aux_tag:
        cmd.append(f"-x {t}")

# Optional Maximum read depth
if "max_read_depth" in snakemake.params:
    cmd.append(f"-d {snakemake.params.max_read_depth}")

if "no_embed_js" in snakemake.params:
    cmd.append("--no-embed-js")

# HTML output
if snakemake.params.get("html", False):
    cmd.append("--html")
    # Redirect output to file if output specified
    if hasattr(snakemake.output, "html"):
        shell(f"{' '.join(cmd)} > {snakemake.output.html} {log}")
    else:
        raise ValueError(
            "HTML output requires a file path defined in output named 'html'"
        )
# Directory output
elif hasattr(snakemake.output, "dir"):
    cmd.append(f"-o {snakemake.output.dir}")
    if "format" in snakemake.params:
        cmd.append(f"-f {snakemake.params.format}")
    shell(f"{' '.join(cmd)} {log}")
# Default: JSON output to single file via stdout
elif hasattr(snakemake.output, "json"):
    shell(f"{' '.join(cmd)} > {snakemake.output.json} {log}")
else:
    raise ValueError(
        "Plot spec output requires a file path defined in output named 'json'"
    )
