__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
java_opts = snakemake.params.get("java_opts", "")
if "mem_mb" in snakemake.resources.keys() and not "-Xmx" in java_opts:
    java_opts += " -Xmx{}M".format(snakemake.resources["mem_mb"])

filters = [
    "--filter-name {} --filter-expression '{}'".format(name, expr.replace("'", "\\'"))
    for name, expr in snakemake.params.filters.items()
]

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
shell(
    "gatk --java-options '{java_opts}' VariantFiltration -R {snakemake.input.ref} -V {snakemake.input.vcf} "
    "{extra} {filters} -O {snakemake.output.vcf} {log}"
)
