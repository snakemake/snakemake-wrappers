__author__ = "Brandon Seah, Johannes Köster"
__copyright__ = "Copyright 2025, Brandon Seah, Johannes Köster"
__email__ = "brandon_seah@tll.org.sg"
__license__ = "MIT"

import subprocess as sp
import sys

from snakemake.shell import shell
from snakemake.logging import logger
from pathlib import Path
from snakemake_wrapper_utils.snakemake import get_format

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

species = snakemake.params.species.lower()
release = int(snakemake.params.release)
division = snakemake.params.division.lower()
assembly = snakemake.params.assembly

available_divisions = ["fungi", "metazoa", "plants", "protists"]
if division not in available_divisions:
    raise ValueError(
        f"Invalid division. Division must be one of: {', '.join(available_divisions)}"
    )

# TODO: bacteria, fungi/ascomycota folders are further subdivided
# TODO: chromosome file names may not follow standard naming convention, e.g.
# Plasmodium_falciparum.GCA000002765v3.dna.primary_assembly.Pf3D7_01_v3.fa.gz

out_fmt = get_format(str(snakemake.output[0]))
out_gz = str(snakemake.output[0]).endswith(".gz")

if out_fmt not in ["gtf", "gff3"]:
    raise ValueError(
        "invalid format specified. Only 'gtf[.gz]' and 'gff3[.gz]' are currently supported."
    )
else:
    suffix = out_fmt + ".gz"

url = snakemake.params.get("url", "https://ftp.ebi.ac.uk/ensemblgenomes/pub")
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
