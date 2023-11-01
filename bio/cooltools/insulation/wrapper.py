__author__ = "Ilya Flyamer"
__copyright__ = "Copyright 2022, Ilya Flyamer"
__email__ = "flyamer@gmail.com"
__license__ = "MIT"

import sndhdr
from snakemake.shell import shell

## Extract arguments
window = snakemake.params.get("window", "")
if isinstance(window, list):
    window = " ".join([str(w) for w in window])
else:
    window = str(window)

view = snakemake.input.get("view", "")
if view:
    view = f"--view {view}"
chunksize = snakemake.params.get("chunksize", 20000000)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

resolution = snakemake.params.get(
    "resolution", snakemake.wildcards.get("resolution", 0)
)
if not resolution:
    raise ValueError("Please specify resolution either as a wildcard or as a parameter")


shell(
    "(cooltools insulation"
    " {snakemake.input.cooler}::resolutions/{resolution} "
    " {window} --chunksize {chunksize} "
    " {view} "
    " -p {snakemake.threads} "
    " {extra} "
    " -o {snakemake.output}) {log}"
)
