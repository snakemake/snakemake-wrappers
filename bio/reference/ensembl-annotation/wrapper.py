__author__ = "Johannes Köster"
__copyright__ = "Copyright 2019, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from ftplib import FTP

species = snakemake.params.species.lower()
release = snakemake.params.release
fmt = snakemake.params.fmt
build = snakemake.params.build

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

suffix = ""
if fmt == "gtf":
    suffix = "gtf.gz"
elif fmt == "gff3":
    suffix = "gff3.gz"

url = "ftp://ftp.ensembl.org/pub/release-{release}/{fmt}/{species}/{species_cap}.{build}.{release}.{suffix}".format(
    release=release,
    build=build,
    species=species,
    fmt=fmt,
    species_cap=species.capitalize(),
    suffix=suffix,
)

shell("curl -L {url} > {snakemake.output[0]} 2> {log}")
