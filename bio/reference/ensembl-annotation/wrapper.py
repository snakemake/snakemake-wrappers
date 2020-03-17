__author__ = "Johannes Köster"
__copyright__ = "Copyright 2019, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from snakemake.shell import shell

species = snakemake.params.species.lower()
release = snakemake.params.release
fmt = snakemake.params.fmt
build = snakemake.params.build
flavor = snakemake.params.get("flavor", "")

if flavor:
    flavor += "."

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

suffix = ""
if fmt == "gtf":
    suffix = "gtf.gz"
elif fmt == "gff3":
    suffix = "gff3.gz"

url = "ftp://ftp.ensembl.org/pub/release-{release}/{fmt}/{species}/{species_cap}.{build}.{release}.{flavor}{suffix}".format(
    release=release,
    build=build,
    species=species,
    fmt=fmt,
    species_cap=species.capitalize(),
    suffix=suffix,
    flavor=flavor,
)

shell("(curl -L {url} | gzip -d > {snakemake.output[0]}) {log}")
