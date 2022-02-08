__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

filters = [
    "--filter-name {} --filter-expression '{}'".format(name, expr.replace("'", "\\'"))
    for name, expr in snakemake.params.filters.items()
]

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' VariantFiltration"
        " --variant {snakemake.input.vcf}"
        " --reference {snakemake.input.ref}"
        " {filters}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " --output {snakemake.output.vcf}"
        " {log}"
    )
