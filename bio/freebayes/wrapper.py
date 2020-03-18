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

# check for optional bed file
targets = (
    ""
    if snakemake.params.targets == ""
    else "--targets {}".format(snakemake.params.targets)
)

# check for optional cnvMap file
cnv = (
    ""
    if snakemake.params.cnvMap == ""
    else "--cnv-map {}".format(snakemake.params.cnvMap)
)

# check for optional cnvMap file
pop = (
    ""
    if snakemake.params.populations == ""
    else "--populations {}".format(snakemake.params.populations)
)

if snakemake.threads == 1:
    freebayes = "freebayes"
else:
    chunksize = snakemake.params.get("chunksize", 100000)
    freebayes = (
        "freebayes-parallel <(fasta_generate_regions.py "
        "{snakemake.input.ref}.fai {chunksize}) "
        "{snakemake.threads}"
    ).format(snakemake=snakemake, chunksize=chunksize)

shell(
    "({freebayes} {targets} {cnv} {pop} {params} -f {snakemake.input.ref}"
    " {snakemake.input.samples} {pipe} > {snakemake.output[0]}) {log}"
)
