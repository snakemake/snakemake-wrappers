__author__ = "Ilya Flyamer"
__copyright__ = "Copyright 2022, Ilya Flyamer"
__email__ = "flyamer@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

## Extract arguments
view = snakemake.input.get("view", "")
if view:
    view = f"--view {view}"
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

resolution = snakemake.params.get(
    "resolution", snakemake.wildcards.get("resolution", 0)
)
if not resolution:
    raise ValueError("Please specify resolution either as a wildcard or as a parameter")

shell(
    "(cooltools expected-trans"
    " {snakemake.input.cooler}::resolutions/{resolution} "
    " {view} "
    " -p {snakemake.threads} "
    " {extra} "
    " -o {snakemake.output}) {log}"
)
