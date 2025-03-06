__author__ = "Ivan Ruiz Manuel"
__copyright__ = "Copyright 2025, Ivan Ruiz Manuel"
__email__ = "i.ruizmanuel@tudelft.nl"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
command = (
    "overturemaps download "
    f"-f {snakemake.params.format} "
    f"--type={snakemake.params.type} "
    f"-o {snakemake.output.path} "
)

bbox = snakemake.params.get("bbox", "")
if bbox:
    if isinstance(bbox, list):
        bbox = ",".join(map(str, bbox))
    command += f"--bbox {bbox}"

shell(command)
