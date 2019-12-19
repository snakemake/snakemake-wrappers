__author__ = "Johannes Köster"
__copyright__ = "Copyright 2019, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell

species = snakemake.params.species.lower()
release = snakemake.params.release
type = snakemake.params.type

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

if type == "all":
    if species == "homo_sapiens":
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

urls = [
    "ftp://ftp.ensembl.org/pub/release-{release}/variation/vcf/{species}/{species}{suffix}.vcf.gz".format(
        release=release, species=species, suffix=suffix
    )
    for suffix in suffixes
]

if snakemake.input.get("fai"):
    # in case of a given .fai, reheader the VCF such that contig lengths are defined
    with tempfile.TemporaryDirectory() as tmpdir:
        shell(
            "(bcftools concat -Ob {urls} > {tmpdir}/out.bcf && "
            " bcftools reheader --fai {snakemake.input.fai} {tmpdir}/out.bcf | bcftools view -Oz -o {snakemake.output[0]}) {log}"
        )
else:
    # without .fai, just concatenate
    shell("bcftools concat -Oz {urls} > {snakemake.output[0]} {log}")
