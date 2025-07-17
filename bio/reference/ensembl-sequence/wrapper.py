__author__ = "Johannes Köster"
__copyright__ = "Copyright 2019, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import subprocess as sp
import sys
from itertools import product
from snakemake.shell import shell
from snakemake.logging import logger
from os import path

species = snakemake.params.species.lower()
release = int(snakemake.params.release)
build = snakemake.params.build

branch = ""
if release >= 81 and build == "GRCh37":
    # use the special grch37 branch for new releases
    branch = "grch37/"
elif snakemake.params.get("branch"):
    branch = snakemake.params.branch + "/"

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

spec = ("{build}" if int(release) > 75 else "{build}.{release}").format(
    build=build, release=release
)

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
            "Invalid datatype. To select individual chromosomes, the datatype must be dna."
        )

url = snakemake.params.get("url", "https://ftp.ensembl.org/pub")
spec = spec.format(build=build, release=release)
url_prefix = f"{url}/{branch}release-{release}/fasta/{species}/{datatype}/{species.capitalize()}.{spec}"

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
            f"Unable to download the requested reference sequence data from Ensembl at: {url}.",
        )
    logger.error(
        "Please check whether above URL is currently available (might be a temporal server issue). \n"
        "Apart from that, did you check that this combination of species, build, and release is actually provided?",
    )
    exit(1)
