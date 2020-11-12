__author__ = "Christopher Schröder"
__copyright__ = "Copyright 2020, Christopher Schröder"
__email__ = "christopher.schroeder@tu-dortmund.de"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
shell(
    "gatk --java-options '{java_opts}' ApplyBQSR {extra} "
    "-R {snakemake.input.ref} -I {snakemake.input.bam} "
    "--bqsr-recal-file {snakemake.input.recal_table} "
    "-O {snakemake.output.bam} {log}"
)
