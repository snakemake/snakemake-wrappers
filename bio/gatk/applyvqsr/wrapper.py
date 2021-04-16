__author__ = "Brett Copeland"
__copyright__ = "Copyright 2021, Brett Copeland"
__email__ = "brcopeland@ucsd.edu"
__license__ = "MIT"


import os

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
shell(
    "gatk --java-options '{java_opts}' ApplyVQSR {extra} "
    "-R {snakemake.input.ref} -V {snakemake.input.vcf} "
    "--recal-file {snakemake.input.recal} "
    "--tranches-file {snakemake.input.tranches} "
    "-mode {snakemake.params.mode} "
    "--output {snakemake.output.vcf} "
    "{log}"
)
