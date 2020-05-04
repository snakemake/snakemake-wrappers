__author__ = "Johannes Köster"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

cache = snakemake.input.cache
entrypath = next(next(Path(cache).iterdir()).iterdir())
species = entrypath.parent.name
release, build = entrypath.name.split("_")

if snakemake.output.calls.endswith(".vcf.gz"):
    fmt = "z"
elif snakemake.output.calls.endswith(".bcf"):
    fmt = "b"
else:
    fmt = "v"

shell(
    "(bcftools view {snakemake.input.calls} | "
    "vep {extra} "
    "--cache "
    "--cache_version {release} "
    "--species {species} "
    "--assembly {build} "
    "--dir_cache {cache} "
    "--output_file STDOUT | "
    "bcftools view -O{fmt} > {snakemake.output.calls}) {log}"
)
