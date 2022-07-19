__author__ = "Ilya Flyamer"
__copyright__ = "Copyright 2022, Ilya Flyamer"
__email__ = "flyamer@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

## Extract arguments
view = snakemake.params.get("view", "")
if view:
    view = f"--view {view}"

track = snakemake.input.get("track", "")
track_col_name = snakemake.params.get("track_col_name", "")
if track and track_col_name:
    track = f"--phasing-track {track}::{track_col_name}"
elif track:
    track = f"--phasing-track {track}"
else:
    track = ""

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

resolution = snakemake.params.get(
    "resolution", snakemake.wildcards.get("resolution", 0)
)
if not resolution:
    raise ValueError("Please specify resolution either as a wildcard or as a parameter")

shell(
    "(cooltools eigs-trans"
    " {snakemake.input.cooler}::resolutions/{resolution} "
    " {track}"
    # " {view} "
    " {extra} "
    " -o {snakemake.output} && "
    " mv {snakemake.output}.trans.vecs.tsv {snakemake.output} && "
    " mv  {snakemake.output}.trans.lam.txt {snakemake.output}.lam.txt ) {log}"
)
