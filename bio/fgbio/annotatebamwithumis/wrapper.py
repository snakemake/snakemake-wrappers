__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2018, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra_params = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

shell(
    "fgbio {java_opts} AnnotateBamWithUmis"
    " -i {snakemake.input.bam}"
    " -f {snakemake.input.umi}"
    " {extra_params}"
    " -o {snakemake.output[0]}"
    " {log}"
)
