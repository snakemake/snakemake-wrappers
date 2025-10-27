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

region = snakemake.params.get("region")
around = snakemake.params.get("around")
highlight = snakemake.params.get("highlight")
aux_tags = snakemake.params.get("aux_tags")
max_read_depth = snakemake.params.get("max_read_depth")
no_embed_js = snakemake.params.get("no_embed_js")
html = snakemake.params.get("html")
format = snakemake.params.get("format")

if region:
    cmd.append(f"-g {region}")
elif around:
    cmd.append(f"-a {around}")

if highlight:
    for h in highlight:
        cmd.append(f"-h {h}")

# Optional Maximum read depth
if max_read_depth:
    cmd.append(f"-d {max_read_depth}")

if no_embed_js:
    cmd.append("--no-embed-js")

# HTML output
if html:
    cmd.append("--html")
    # Redirect output to file if output specified
    if snakemake.output.html:
        shell(f"{' '.join(cmd)} > {snakemake.output.html} {log}")
    else:
        raise ValueError(
            "HTML output requires a file path defined in output named 'html'"
        )
# Directory output
elif snakemake.output.dir:
    cmd.append(f"-o {snakemake.output.dir}")
    if format:
        cmd.append(f"-f {format}")
    shell(f"{' '.join(cmd)} {log}")
# Default: JSON output to single file via stdout
elif snakemake.output.json:
    shell(f"{' '.join(cmd)} > {snakemake.output.json} {log}")
else:
    raise ValueError(
        "Plot spec output requires a file path defined in output named 'json'"
    )
