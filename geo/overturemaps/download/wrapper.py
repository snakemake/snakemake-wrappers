__author__ = "Ivan Ruiz Manuel"
__copyright__ = "Copyright 2025, Ivan Ruiz Manuel"
__email__ = "i.ruizmanuel@tudelft.nl"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

extra = snakemake.params.get("extra", "")
bbox = snakemake.params.get("bbox", "")
if bbox:
    if isinstance(bbox, list):
        bbox = ",".join(map(str, bbox))
    bbox = f"--bbox {bbox}"

shell(
    "overturemaps download"
    f" -f {snakemake.params.format}"
    f" --type {snakemake.params.type}"
    f" {bbox}"
    f" {extra}"
    f" --output {snakemake.output.path}"
    f" {log}"
)
