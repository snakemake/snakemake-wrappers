__author__ = "Johannes Köster"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from pathlib import Path
from snakemake.shell import shell

get_child = lambda path: next(path.iterdir())

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

stats = snakemake.output.stats
cache = snakemake.input.cache
plugins = snakemake.input.plugins
entrypath = get_child(get_child(Path(cache)))
species = entrypath.parent.name
release, build = entrypath.name.split("_")

load_plugins = " ".join(map("--plugin {}".format, snakemake.params.plugins))

if snakemake.output.calls.endswith(".vcf.gz"):
    fmt = "z"
elif snakemake.output.calls.endswith(".bcf"):
    fmt = "b"
else:
    fmt = "v"

shell(
    "(bcftools view {snakemake.input.calls} | "
    "vep {extra} "
    "--format vcf "
    "--vcf "
    "--cache "
    "--cache_version {release} "
    "--species {species} "
    "--assembly {build} "
    "--dir_cache {cache} "
    "--dir_plugins {plugins} "
    "{load_plugins} "
    "--output_file STDOUT "
    "--stats_file {stats} | "
    "bcftools view -O{fmt} > {snakemake.output.calls}) {log}"
)
