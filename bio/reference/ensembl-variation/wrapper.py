__author__ = "Johannes Köster"
__copyright__ = "Copyright 2019, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import tempfile
import subprocess
import sys
from snakemake.shell import shell
from snakemake.exceptions import WorkflowError

species = snakemake.params.species.lower()
release = int(snakemake.params.release)
build = snakemake.params.build
type = snakemake.params.type

branch = ""
if release >= 81 and build == "GRCh37":
    # use the special grch37 branch for new releases
    branch = "grch37/"

log = snakemake.log[0]

if type == "all":
    if species == "homo_sapiens" and release >= 93:
        suffixes = [
            "-chr{}".format(chrom) for chrom in list(range(1, 23)) + ["X", "Y", "MT"]
        ]
    else:
        suffixes = [""]
elif type == "somatic":
    suffixes = ["_somatic"]
elif type == "structural_variations":
    suffixes = ["_structural_variations"]
else:
    raise ValueError(
        "Unsupported type {} (only all, somatic, structural_variations are allowed)".format(
            type
        )
    )

species_filename = species if release >= 91 else species.capitalize()

urls = [
    "ftp://ftp.ensembl.org/pub/{branch}release-{release}/variation/vcf/{species}/{species_filename}{suffix}.vcf.gz".format(
        release=release,
        species=species,
        suffix=suffix,
        species_filename=species_filename,
        branch=branch,
    )
    for suffix in suffixes
]

names = [os.path.basename(url) for url in urls]

download = (
    "bcftools concat -Oz {urls}" if len(urls) > 1 else "bcftools view -Oz {urls}"
).format(urls=" ".join(urls))

try:
    # in case of a given .fai, reheader the VCF such that contig lengths are defined
    with tempfile.TemporaryDirectory() as tmpdir:
        # download all vcfs
        shell("(cd {tmpdir} && curl -O {urls}) 2> {log}")
        if len(names) > 1:
            # concatenate and recompress with bgzip
            shell("(cd {tmpdir} && bcftools concat -Oz {names} > out.vcf.gz) 2>> {log}")
        else:
            # recompress with bgzip
            shell("(cd {tmpdir} && bcftools view -Oz {names} > out.vcf.gz) 2>> {log}")
        
        if snakemake.input.get("fai"):
            # reheader, adding sequence lenghts
            shell("bcftools reheader --fai {snakemake.input.fai} {tmpdir}/out.vcf.gz > {snakemake.output} 2>> {log}")
        else:
            # just move to final place
            shell("mv {tmpdir}/out.vcf.gz {snakemake.output}")
except subprocess.CalledProcessError as e:
    if snakemake.log:
        sys.stderr = open(snakemake.log[0], "a")
    print(
        "Unable to download variation data from Ensembl. "
        "Did you check that this combination of species, build, and release is actually provided?",
        file=sys.stderr,
    )
    exit(1)
