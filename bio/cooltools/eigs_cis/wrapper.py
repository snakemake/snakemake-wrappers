__author__ = "Ilya Flyamer"
__copyright__ = "Copyright 2022, Ilya Flyamer"
__email__ = "flyamer@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
import tempfile


## Extract arguments
view = snakemake.input.get("view", "")
if view:
    view = f"--view {view}"
track = snakemake.input.get("track", "")
track_col_name = snakemake.params.get("track_col_name", "")
if track and track_col_name:
    track = f"--phasing-track {track}::{track_col_name}"
elif track:
    track = f"--phasing-track {track}"

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

bigwig = snakemake.output.get("bigwig", "")
if bigwig:
    bigwig = "--bigwig"

resolution = snakemake.params.get("resolution", snakemake.wildcards.get("resolution"))
assert (
    resolution
), "Please specify resolution either as a `wildcard` or as a `parameter`"

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "cooltools eigs-cis"
        " {snakemake.input.cooler}::resolutions/{resolution} "
        " {track}"
        " {view} "
        " {bigwig}"
        " {extra} "
        " -o {tmpdir}/out"
        " {log}"
    )

    shell("mv {tmpdir}/out.cis.vecs.tsv {snakemake.output.vecs}")
    shell("mv {tmpdir}/out.cis.lam.txt {snakemake.output.lam}")
    if bigwig:
        shell("mv {tmpdir}/out.cis.bw {snakemake.output.bigwig}")
