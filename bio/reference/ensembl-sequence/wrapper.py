__author__ = "Johannes Köster"
__copyright__ = "Copyright 2019, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import subprocess as sp
import sys
from itertools import product
from snakemake.shell import shell

species = snakemake.params.species.lower()
release = int(snakemake.params.release)
build = snakemake.params.build

branch = ""
if release >= 81 and build == "GRCh37":
    # use the special grch37 branch for new releases
    branch = "grch37/"

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

spec = ("{build}" if int(release) > 75 else "{build}.{release}").format(
    build=build, release=release
)

suffixes = ""
datatype = snakemake.params.get("datatype", "")
chromosome = snakemake.params.get("chromosome", "")
if datatype == "dna":
    if chromosome:
        suffixes = ["dna.chromosome.{}.fa.gz".format(chromosome)]
    else:
        suffixes = ["dna.primary_assembly.fa.gz", "dna.toplevel.fa.gz"]
elif datatype == "cdna":
    suffixes = ["cdna.all.fa.gz"]
elif datatype == "cds":
    suffixes = ["cds.all.fa.gz"]
elif datatype == "ncrna":
    suffixes = ["ncrna.fa.gz"]
elif datatype == "pep":
    suffixes = ["pep.all.fa.gz"]
else:
    raise ValueError("invalid datatype, must be one of dna, cdna, cds, ncrna, pep")

if chromosome:
    if not datatype == "dna":
        raise ValueError(
            "invalid datatype, to select a single chromosome the datatype must be dna"
        )

success = False
for suffix in suffixes:
    url = "ftp://ftp.ensembl.org/pub/{branch}release-{release}/fasta/{species}/{datatype}/{species_cap}.{spec}.{suffix}".format(
        release=release,
        species=species,
        datatype=datatype,
        spec=spec.format(build=build, release=release),
        suffix=suffix,
        species_cap=species.capitalize(),
        branch=branch,
    )

    try:
        shell("curl -sSf {url} > /dev/null 2> /dev/null")
    except sp.CalledProcessError:
        continue

    shell("(curl -L {url} | gzip -d > {snakemake.output[0]}) {log}")
    success = True
    break

if not success:
    print(
        "Unable to download requested sequence data from Ensembl. "
        "Did you check that this combination of species, build, and release is actually provided?",
        file=sys.stderr,
    )
    exit(1)
