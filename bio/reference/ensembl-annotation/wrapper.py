__author__ = "Johannes Köster"
__copyright__ = "Copyright 2019, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import subprocess
import sys
from pathlib import Path
from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=False, stderr=True)


species = snakemake.params.species.lower()
build = snakemake.params.build
release = int(snakemake.params.release)
gtf_release = release
out_fmt = Path(snakemake.output[0]).suffixes
out_gz = (out_fmt.pop() and True) if out_fmt[-1] == ".gz" else False
out_fmt = out_fmt.pop().lstrip(".")


branch = ""
if build == "GRCh37":
    if release >= 81:
        # use the special grch37 branch for new releases
        branch = "grch37/"
    if release > 87:
        gtf_release = 87
elif snakemake.params.get("branch"):
    branch = snakemake.params.branch + "/"


flavor = snakemake.params.get("flavor", "")
if flavor:
    flavor += "."


suffix = ""
if out_fmt == "gtf":
    suffix = "gtf.gz"
elif out_fmt == "gff3":
    suffix = "gff3.gz"
else:
    raise ValueError(
        "invalid format specified. Only 'gtf[.gz]' and 'gff3[.gz]' are currently supported."
    )


url = "ftp://ftp.ensembl.org/pub/{branch}release-{release}/{out_fmt}/{species}/{species_cap}.{build}.{gtf_release}.{flavor}{suffix}".format(
    release=release,
    gtf_release=gtf_release,
    build=build,
    species=species,
    out_fmt=out_fmt,
    species_cap=species.capitalize(),
    suffix=suffix,
    flavor=flavor,
    branch=branch,
)


try:
    if out_gz:
        shell("curl -L {url} > {snakemake.output[0]} {log}")
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
