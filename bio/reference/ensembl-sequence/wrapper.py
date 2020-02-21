__author__ = "Johannes Köster"
__copyright__ = "Copyright 2019, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import subprocess as sp
from snakemake.shell import shell

species = snakemake.params.species.lower()
release = snakemake.params.release
build = snakemake.params.build

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

suffixes = ""
datatype = snakemake.params.get("datatype", "")
if datatype == "dna":
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

success = False
for suffix in suffixes:
    url = "ftp://ftp.ensembl.org/pub/release-{release}/fasta/{species}/{datatype}/{species_cap}.{build}.{suffix}".format(
        release=release,
        species=species,
        datatype=datatype,
        build=build,
        suffix=suffix,
        species_cap=species.capitalize(),
    )

    try:
        shell("curl -sSf {url} > /dev/null 2> /dev/null")
    except sp.CalledProcessError:
        continue

    shell("(curl -L {url} | gzip -d > {snakemake.output[0]}) {log}")
    success = True
    break

if not success:
    raise ValueError(
        "Requested sequence does not seem to exist on ensembl FTP servers or servers are unavailable (url {})".format(
            url
        )
    )
