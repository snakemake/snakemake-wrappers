__author__ = "Christopher Schröder"
__copyright__ = "Copyright 2020, Christopher Schröder"
__email__ = "christopher.schroeder@tu-dortmund.de"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
known = snakemake.input.get("known", "")
if known:
    if isinstance(known, str):
        known = [known]
    known = list(map("--known-sites {}".format, known))

shell(
    "gatk --java-options '{java_opts}' BaseRecalibrator {extra} "
    "-R {snakemake.input.ref} -I {snakemake.input.bam} "
    "-O {snakemake.output.recal_table} {known} {log}"
)
