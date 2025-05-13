__author__ = "Johannes Köster"
__copyright__ = "Copyright 2024, Johannes Köster"
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

if release < 87:
    raise ValueError(
        "Comprehensive GFF files are only available for release 87 or newer."
    )

if build == "GRCh37":
    grch37 = "grch37/"
else:
    grch37 = ""


suffix = ""
if out_fmt == "gff":
    suffix = "gff.gz"
elif out_fmt == "gff3":
    suffix = "gff3.gz"
else:
    raise ValueError(
        "Invalid format specified."
        "Only 'gff[.gz]' (for releases before 112, and for build GRCh37) and"
        "'gff3[.gz]' (for any release from 112 onwards) are currently supported."
    )


url = snakemake.params.get("url", "ftp://ftp.ensembl.org/pub")
if release < 112 or build == "GRCh37":
    if out_fmt != "gff":
        raise ValueError(
            f"Invalid suffix for output file '{snakemake.output[0]}'."
            "For releases older than 112 and for human build GRCh37, only .gff or .gff.gz are valid."
        )
    url = f"{url}/{grch37}release-{release}/regulation/{species}/{species}.{build}.Regulatory_Build.regulatory_features.*.{suffix}"
else:
    if out_fmt != "gff3":
        raise ValueError(
            f"Invalid suffix for output file '{snakemake.output[0]}'."
            "For (non-GRCh37) releases from 112 onwards, only .gff3 or .gff3.gz are valid."
        )
    url = f"{url}/release-{release}/regulation/{species}/{build}/annotation/{species.capitalize()}.{build}.regulatory_features.v{release}.{suffix}"

try:
    if out_gz:
        shell('wget "{url}" -O {snakemake.output[0]} {log}')
    else:
        shell('(wget "{url}" -O - | gzip -d > {snakemake.output[0]}) {log}')
except subprocess.CalledProcessError as e:
    if snakemake.log:
        sys.stderr = open(snakemake.log[0], "a")
    print(
        "Unable to download regulatory feature data from Ensembl. "
        "Did you check that this combination of species, build, and release is actually provided?"
        "A good entry point for a search is: https://www.ensembl.org/info/data/ftp/index.html",
        file=sys.stderr,
    )
    exit(1)
