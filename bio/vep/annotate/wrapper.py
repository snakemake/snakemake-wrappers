__author__ = "Johannes Köster"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from pathlib import Path
from snakemake.shell import shell


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
cache = snakemake.input.get("cache", "")
plugins = snakemake.input.plugins

load_plugins = " ".join(map("--plugin {}".format, snakemake.params.plugins))

if snakemake.output.calls.endswith(".vcf.gz"):
    fmt = "z"
elif snakemake.output.calls.endswith(".bcf"):
    fmt = "b"
else:
    fmt = "v"

fasta = snakemake.input.get("fasta", "")
if fasta:
    fasta = "--fasta {}".format(fasta)

gff = snakemake.input.get("gff", "")
if gff:
    gff = "--gff {}".format(gff)

if cache:
    entrypath = get_only_child_dir(get_only_child_dir(Path(cache)))
    species = (
        entrypath.parent.name[:-7]
        if entrypath.parent.name.endswith("_refseq")
        else entrypath.parent.name
    )
    release, build = entrypath.name.split("_")
    cache = (
        "--offline --cache --dir_cache {cache} --cache_version {release} --species {species} --assembly {build}"
    ).format(cache=cache, release=release, build=build, species=species)

shell(
    "(bcftools view '{snakemake.input.calls}' | "
    "vep {extra} {fork} "
    "--format vcf "
    "--vcf "
    "{cache} "
    "{gff} "
    "{fasta} "
    "--dir_plugins {plugins} "
    "{load_plugins} "
    "--output_file STDOUT "
    "--stats_file {stats} | "
    "bcftools view -O{fmt} > {snakemake.output.calls}) {log}"
)
