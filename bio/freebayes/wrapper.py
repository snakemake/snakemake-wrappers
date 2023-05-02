__author__ = "Johannes Köster, Felix Mölder, Christopher Schröder"
__copyright__ = "Copyright 2017, Johannes Köster"
__email__ = "johannes.koester@protonmail.com, felix.moelder@uni-due.de"
__license__ = "MIT"


from snakemake.shell import shell
from tempfile import TemporaryDirectory
from snakemake_wrapper_utils.bcftools import get_bcftools_opts


log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")
bcftools_sort_opts = get_bcftools_opts(
    snakemake,
    parse_threads=False,
    parse_ref=False,
    parse_regions=False,
    parse_samples=False,
    parse_targets=False,
    parse_output=False,
    parse_output_format=False,
)


pipe = ""
norm_params = snakemake.params.get("normalize")
if norm_params:
    bcftools_norm_opts = get_bcftools_opts(
        snakemake, parse_regions=False, parse_targets=False, parse_memory=False
    )
    pipe = f"bcftools norm {bcftools_norm_opts} {norm_params}"
else:
    bcftools_view_opts = get_bcftools_opts(
        snakemake,
        parse_ref=False,
        parse_regions=False,
        parse_targets=False,
        parse_memory=False,
    )
    pipe = f"bcftools view {bcftools_view_opts}"


if snakemake.threads == 1:
    freebayes = "freebayes"
else:
    chunksize = snakemake.params.get("chunksize", 100000)
    regions = f"<(fasta_generate_regions.py {snakemake.input.ref}.fai {chunksize})"

    if snakemake.input.get("regions"):
        regions = (
            "<(bedtools intersect -a "
            + r"<(sed 's/:\([0-9]*\)-\([0-9]*\)$/\t\1\t\2/' "
            + f"{regions}) -b {snakemake.input.regions} | "
            + r"sed 's/\t\([0-9]*\)\t\([0-9]*\)$/:\1-\2/')"
        )

    freebayes = f"freebayes-parallel {regions} {snakemake.threads}"


with TemporaryDirectory() as tempdir:
    shell(
        "({freebayes}"
        " --fasta-reference {snakemake.input.ref}"
        " {extra}"
        " {snakemake.input.alns}"
        " | bcftools sort {bcftools_sort_opts} --temp-dir {tempdir}"
        " | {pipe}"
        ") {log}"
    )
