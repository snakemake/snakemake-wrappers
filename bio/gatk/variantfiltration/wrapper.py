__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

filters = [
    "--filter-name {} --filter-expression '{}'".format(name, expr.replace("'", "\\'"))
    for name, expr in snakemake.params.filters.items()
]

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
shell(
    "gatk --java-options '{java_opts}' VariantFiltration -R {snakemake.input.ref} -V {snakemake.input.vcf} "
    "{extra} {filters} -O {snakemake.output.vcf} {log}"
)
