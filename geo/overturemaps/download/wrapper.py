__author__ = "Ivan Ruiz Manuel"
__copyright__ = "Copyright 2025, Ivan Ruiz Manuel"
__email__ = "i.ruizmanuel@tudelft.nl"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

bbox = snakemake.params.get("bbox", "")
if bbox:
    if isinstance(bbox, list):
        bbox = ",".join(map(str, bbox))
    bbox = f"--bbox {bbox}"

command = (
    "overturemaps download "
    f"-f {snakemake.params.format} "
    f"--type={snakemake.params.type} "
    f"-o {snakemake.output.path} "
    f"{bbox} "
    f"{snakemake.params.get("extra", "")} "
)

shell(f"({command}) {log}")
