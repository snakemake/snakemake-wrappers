__author__ = "Ilya Flyamer"
__copyright__ = "Copyright 2022, Ilya Flyamer"
__email__ = "flyamer@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

## Extract arguments
view = " ".format(snakemake.params.get("view", ""))
if view:
    view = f"--view {view}"
else:
    view = ""
track = snakemake.input.get("track", "")
track_col_name = snakemake.params.get("track_col_name", "")
if track and track_col_name:
    track = f"--phasing-track {track}::{track_col_name}"
else:
    track = f"--phasing-track {track}"

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


shell(
    "(cooltools eigs-cis"
    " {snakemake.input.cooler}::resolutions/{snakemake.wildcards.resolution} "
    " {track}"
    " {view} "
    " {extra} "
    " -o {snakemake.output}) {log}"
)
