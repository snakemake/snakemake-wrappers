__author__ = "Brandon Seah, Johannes Köster"
__copyright__ = "Copyright 2025, Brandon Seah, Johannes Köster"
__email__ = "brandon_seah@tll.org.sg"
__license__ = "MIT"

import subprocess as sp
import sys

from snakemake.shell import shell
from snakemake.logging import logger
from pathlib import Path

species = snakemake.params.species.lower()
release = int(snakemake.params.release)
division = snakemake.params.division.lower()
assembly = snakemake.params.assembly

out_fmt = Path(snakemake.output[0]).suffixes
out_gz = (out_fmt.pop() and True) if out_fmt[-1] == ".gz" else False
out_fmt = out_fmt.pop().lstrip(".")

available_divisions = ["fungi", "metazoa", "plants", "protists"]
if division not in available_divisions:
    raise ValueError(
        f"Invalid division. Division must be one of: {', '.join(available_divisions)}"
    )

# TODO: bacteria, fungi/ascomycota folders are further subdivided
# TODO: chromosome file names may not follow standard naming convention, e.g.
# Plasmodium_falciparum.GCA000002765v3.dna.primary_assembly.Pf3D7_01_v3.fa.gz

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

suffix = ""
if out_fmt == "gtf":
    suffix = "gtf.gz"
elif out_fmt == "gff3":
    suffix = "gff3.gz"
else:
    raise ValueError(
        "invalid format specified. Only 'gtf[.gz]' and 'gff3[.gz]' are currently supported."
    )

url = snakemake.params.get("url", "https://ftp.ebi.ac.uk/ensemblgenomes/pub/")
url = f"{url}/release-{release}/{division}/{out_fmt}/{species}/{species.capitalize()}.{assembly}.{release}.{suffix}"
ftp_url = url.replace("https://", "ftp://")

try:
    if out_gz:
        shell("curl --fail -L {url} > {snakemake.output[0]} {log}")
    else:
        shell("(curl --fail -L {url} | gzip -d > {snakemake.output[0]}) {log}")
except sp.CalledProcessError:
    try:
        if out_gz:
            shell("curl --fail -L {ftp_url} > {snakemake.output[0]} {log}")
        else:
            shell("(curl --fail -L {ftp_url} | gzip -d > {snakemake.output[0]}) {log}")
    except sp.CalledProcessError:
        if snakemake.log:
            sys.stderr = open(snakemake.log[0], "a")
        print(
            "Unable to download annotation data from Ensembl Genomes.\n"
            "Did you check that this combination of species, division, assembly, and release is actually provided?",
            file=sys.stderr,
        )
        exit(1)
