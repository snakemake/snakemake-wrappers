__author__ = "Ilya Flyamer"
__copyright__ = "Copyright 2022, Ilya Flyamer"
__email__ = "flyamer@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
from os import path
import tempfile

## Extract arguments
view = snakemake.input.get("view", "")
if view:
    view = f"--view {view}"

track = snakemake.input.get("track", "")
track_col_name = snakemake.params.get("track_col_name", "")
if track and track_col_name:
    track = f"{track}::{track_col_name}"

expected = snakemake.input.get("expected", "")
range = snakemake.params.get("range", "--qrange 0 1")
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

resolution = snakemake.params.get(
    "resolution", snakemake.wildcards.get("resolution", 0)
)
if not resolution:
    raise ValueError("Please specify resolution either as a wildcard or as a parameter")

fig = snakemake.output.get("fig", "")
if fig:
    ext = path.splitext(fig)[1][1:]
    fig = f"--fig {ext}"

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "(cooltools saddle"
        " {snakemake.input.cooler}::resolutions/{resolution} "
        " {track} "
        " {expected} "
        " {view} "
        " {range} "
        " {fig} "
        " {extra} "
        " -o {tmpdir}/out)"
        " {log}"
    )

    shell("mv {tmpdir}/out.saddledump.npz {snakemake.output.saddle}")
    shell("mv {tmpdir}/out.digitized.tsv {snakemake.output.digitized_track}")
    if fig:
        shell("mv {tmpdir}/out.{ext} {snakemake.output.fig}")
