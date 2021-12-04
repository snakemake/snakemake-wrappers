__author__ = "Johannes Köster, Felix Mölder, Christopher Schröder"
__copyright__ = "Copyright 2017, Johannes Köster"
__email__ = "johannes.koester@protonmail.com, felix.moelder@uni-due.de"
__license__ = "MIT"


from os import path
from snakemake.shell import shell
from tempfile import TemporaryDirectory

shell.executable("bash")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

params = snakemake.params.get("extra", "")
norm = snakemake.params.get("normalize", False)


# Infer output format
uncompressed_bcf = snakemake.params.get("uncompressed_bcf", False)
out_name, out_ext = path.splitext(snakemake.output[0])
if out_ext == ".vcf":
    out_format = "v"
elif out_ext == ".bcf":
    if uncompressed_bcf:
        out_format = "u"
    else:
        out_format = "b"
elif out_ext == ".gz":
    out_name, out_ext = path.splitext(out_name)
    if out_ext == ".vcf":
        out_format = "z"
    else:
        raise ValueError("output file with invalid extension (.vcf, .vcf.gz, .bcf).")
else:
    raise ValueError("output file with invalid extension (.vcf, .vcf.gz, .bcf).")


pipe = ""
if norm:
    pipe = f"| bcftools norm {norm} --output-type {out_format} -"
else:
    pipe = f"| bcftools view --output-type {out_format} -"


if snakemake.threads == 1:
    freebayes = "freebayes"
else:
    chunksize = snakemake.params.get("chunksize", 100000)
    regions = (
        "<(fasta_generate_regions.py {snakemake.input.ref}.fai {chunksize})".format(
            snakemake=snakemake, chunksize=chunksize
        )
    )
    if snakemake.input.get("regions", ""):
        regions = (
            "<(bedtools intersect -a "
            r"<(sed 's/:\([0-9]*\)-\([0-9]*\)$/\t\1\t\2/' "
            "{regions}) -b {snakemake.input.regions} | "
            r"sed 's/\t\([0-9]*\)\t\([0-9]*\)$/:\1-\2/')"
        ).format(regions=regions, snakemake=snakemake)
    freebayes = ("freebayes-parallel {regions} {snakemake.threads}").format(
        snakemake=snakemake, regions=regions
    )

with TemporaryDirectory() as tempdir:
    shell(
        "({freebayes} {params} -f {snakemake.input.ref}"
        " {snakemake.input.samples} | bcftools sort -T {tempdir} - {pipe} > {snakemake.output[0]}) {log}"
    )
