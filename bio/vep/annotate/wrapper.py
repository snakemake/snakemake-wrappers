__author__ = "Johannes Köster"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import os
from pathlib import Path


def get_only_child_dir(path):
    children = [child for child in path.iterdir() if child.is_dir()]
    assert (
        len(children) == 1
    ), "Invalid VEP cache directory, only a single entry is allowed, make sure that cache was created with the snakemake VEP cache wrapper"
    return children[0]


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

fork = "--fork {}".format(snakemake.threads) if snakemake.threads > 1 else ""
stats = snakemake.output.stats
cache = snakemake.input.cache
plugins = snakemake.input.plugins

entrypath = get_only_child_dir(get_only_child_dir(Path(cache)))
species = entrypath.parent.name
release, build = entrypath.name.split("_")

load_plugins = " ".join(map("--plugin {}".format, snakemake.params.plugins))

if snakemake.output.calls.endswith(".vcf.gz"):
    fmt = "z"
elif snakemake.output.calls.endswith(".bcf"):
    fmt = "b"
else:
    fmt = "v"

os.system(
    f"(bcftools view {snakemake.input.calls} | "
    f"vep {extra} {fork} "
    f"--format vcf "
    f"--vcf "
    f"--cache "
    f"--cache_version {release} "
    f"--species {species} "
    f"--assembly {build} "
    f"--dir_cache {cache} "
    f"--dir_plugins {plugins} "
    f"--offline "
    f"{load_plugins} "
    f"--output_file STDOUT "
    f"--stats_file {stats} | "
    f"bcftools view -O{fmt} > {snakemake.output.calls}) {log}"
)
