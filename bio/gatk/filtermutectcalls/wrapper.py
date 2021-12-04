__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2021, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "gatk --java-options '{java_opts}' FilterMutectCalls "
    "-R {snakemake.input.ref} -V {snakemake.input.vcf} "
    "{extra} "
    "-O {snakemake.output.vcf} "
    "{log}"
)
