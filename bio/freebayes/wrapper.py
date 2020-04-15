__author__ = "Johannes Köster"
__copyright__ = "Copyright 2017, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


from snakemake.shell import shell

shell.executable("bash")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

params = snakemake.params.get("extra", "")

pipe = ""
if snakemake.output[0].endswith(".bcf"):
    pipe = "| bcftools view -Ob -"

if snakemake.threads == 1:
    freebayes = "freebayes"
else:
    chunksize = snakemake.params.get("chunksize", 100000)
    regions = "fasta_generate_regions.py {snakemake.input.ref}.fai {chunksize}".format(
        snakemake=snakemake, chunksize=chunksize
    )
    if snakemake.input.get("regions", ""):
        regions = "<(bedtools intersect -a =(sed ('s/:/\t/g; s/-/\t/g') <({regions})) -b {snakemake.input.regions})".format(
            regions=regions, snakemake=snakemake
        )
    else:
        regions = "<({regions})".format(regions=regions)
    freebayes = ("freebayes-parallel {regions} {snakemake.threads}").format(
        snakemake=snakemake, regions=regions
    )

shell(
    "({freebayes} {params} -f {snakemake.input.ref}"
    " {snakemake.input.samples} {pipe} > {snakemake.output[0]}) {log}"
)
