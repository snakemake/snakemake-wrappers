__author__ = "Ilya Flyamer"
__copyright__ = "Copyright 2022, Ilya Flyamer"
__email__ = "flyamer@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
from os import path

## Extract arguments
view = snakemake.params.get("view", "")
if view:
    view = f"--view {view}"

track = snakemake.input.get("track", "")
track_col_name = snakemake.params.get("track_col_name", "")
if track and track_col_name:
    track = f"{track}::{track_col_name}"
elif track:
    pass
else:
    track = ""

expected = snakemake.input.get("expected", "")
range = snakemake.params.get("range", "--qrange 0 1")
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

resolution = snakemake.params.get(
    "resolution", snakemake.wildcards.get("resolution", 0)
)
if not resolution:
    raise ValueError("Please specify resolution either as a wildcard or as a parameter")

output = snakemake.output[0]

shell(
    "(cooltools saddle"
    " {snakemake.input.cooler}::resolutions/{resolution} "
    " {track} "
    " {expected} "
    " {view} "
    " {range} "
    " {extra} "
    " -o {output} &&"
    " mv {snakemake.output}.saddledump.npz {snakemake.output}) && "
    " {log}"
)
