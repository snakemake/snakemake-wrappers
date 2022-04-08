__author__ = "Johannes Köster"
__copyright__ = "Copyright 2019, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import subprocess
import sys
from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=False, stderr=True)


species = snakemake.params.species.lower()
build = snakemake.params.build
release = int(snakemake.params.release)
fmt = snakemake.params.fmt


branch = ""
if release >= 81 and build == "GRCh37":
    # use the special grch37 branch for new releases
    branch = "grch37/"


flavor = snakemake.params.get("flavor", "")
if flavor:
    flavor += "."


suffix = ""
if fmt == "gtf" or fmt == "gtf.gz":
    suffix = "gtf.gz"
elif fmt == "gff3" or fmt == "gff3.gz":
    suffix = "gff3.gz"
else:
    raise ValueError(
        "invalid format specified. Only 'gtf[.gz]' and 'gff3[.gz]' are currently supported."
    )


url = "ftp://ftp.ensembl.org/pub/{branch}release-{release}/{fmt}/{species}/{species_cap}.{build}.{release}.{flavor}{suffix}".format(
    release=release,
    build=build,
    species=species,
    fmt=fmt,
    species_cap=species.capitalize(),
    suffix=suffix,
    flavor=flavor,
    branch=branch,
)


try:
    if fmt.endswith(".gz"):
        shell("(curl -L {url} > {snakemake.output[0]}) {log}")
    else:
        shell("(curl -L {url} | gzip -d > {snakemake.output[0]}) {log}")
except subprocess.CalledProcessError as e:
    if snakemake.log:
        sys.stderr = open(snakemake.log[0], "a")
    print(
        "Unable to download annotation data from Ensembl. "
        "Did you check that this combination of species, build, and release is actually provided?",
        file=sys.stderr,
    )
    exit(1)
