__author__ = "Brandon Seah, Johannes Köster"
__copyright__ = "Copyright 2025, Brandon Seah, Johannes Köster"
__email__ = "brandon_seah@tll.org.sg"
__license__ = "MIT"

import subprocess as sp
import sys
from itertools import product
from snakemake.shell import shell
from snakemake.logging import logger
from os import path

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

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

if path.splitext(snakemake.output[0])[1] == ".gz":
    decompress = ""
else:
    decompress = " | gzip -d"

suffixes = ""
datatype = snakemake.params.get("datatype", "")
chromosome = snakemake.params.get("chromosome", "")
if datatype == "dna":
    if chromosome:
        suffixes = [f"dna.chromosome.{chrom}.fa.gz" for chrom in chromosome]
    else:
        # TODO: ensembl genomes does not always have a single dna.primary_assembly.fa.gz file
        suffixes = ["dna.toplevel.fa.gz"]
elif datatype == "dna_rm":  # masked genomic sequence
    suffixes = ["dna_rm.toplevel.fa.gz"]
elif datatype == "dna_sm":  # softmasked genomic sequence
    suffixes = ["dna_sm.toplevel.fa.gz"]
elif datatype == "cdna":
    suffixes = ["cdna.all.fa.gz"]
elif datatype == "cds":
    suffixes = ["cds.all.fa.gz"]
elif datatype == "ncrna":
    suffixes = ["ncrna.fa.gz"]
elif datatype == "pep":
    suffixes = ["pep.all.fa.gz"]
else:
    raise ValueError(
        "Invalid datatype, must be one of dna, dna_rm, dna_sm, cdna, cds, ncrna, pep"
    )

if chromosome:
    if not datatype == "dna":
        raise ValueError(
            "Invalid datatype. To select individual chromosomes, the datatype must be dna."
        )

url = snakemake.params.get("url", "https://ftp.ebi.ac.uk/ensemblgenomes/pub/")
url_prefix = f"{url}/release-{release}/{division}/fasta/{species}/{datatype}/{species.capitalize()}.{assembly}"

for suffix in suffixes:
    success = False
    use_ftp = False
    url = f"{url_prefix}.{suffix}"
    # FTP works as a fallback, in case an HTTPS connection doesn't succeed
    url_ftp = url.replace("https://", "ftp://")

    try:
        # --location follows redirects, --head only gets the header without any download,
        # Content-Length is only there if the file exists, for both https:// and ftp://
        shell("curl --location --head {url} | grep 'Content-Length'")
    except sp.CalledProcessError:
        try:
            shell("curl --location --head {url_ftp} | grep 'Content-Length'")
        except sp.CalledProcessError:
            if chromosome:
                logger.error(
                    f"Unable to download the requested chromosome sequence from Ensembl at either of: \n"
                    f"* {url}\n"
                    f"* {url_ftp}",
                )
                break
            else:
                continue
        else:
            use_ftp = True

    if use_ftp:
        shell("(curl -L {url_ftp} {decompress} >> {snakemake.output[0]}) {log}")
    else:
        shell("(curl -L {url} {decompress} >> {snakemake.output[0]}) {log}")
    success = True
    if not chromosome:
        break

if not success:
    if not chromosome:
        if len(suffixes) > 1:
            url = f"{url_prefix}.[{'|'.join(suffixes)}]"
        else:
            url = f"{url_prefix}.{suffixes[0]}"
        logger.error(
            f"Unable to download the requested reference sequence data from Ensembl Genomes at: {url}.",
        )
    logger.error(
        "Please check whether above URL is currently available (might be a temporary server issue). \n"
        "Apart from that, did you check that this combination of division, species, assembly, and release is actually provided?",
    )
    exit(1)
