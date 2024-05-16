__author__ = "William Rowell"
__copyright__ = "Copyright 2020, William Rowell"
__email__ = "wrowell@pacb.com"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


if snakemake.input[0].endswith(".gz"):
    extra += " --decompress"


shell(
    "bgzip --threads {snakemake.threads} {extra} --output {snakemake.output[0]} {snakemake.input[0]} {log}"
)
