__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2019, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com.com"
__license__ = "MIT"

import os

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)


bed = snakemake.input.get("bed", "")
if bed:
    bed = "-L " + bed


known = snakemake.input.get("known", "")
if known:
    if isinstance(known, str):
        known = "-known {}".format(known)
    else:
        known = list(map("-known {}".format, known))


log = snakemake.log_fmt_shell(stdout=True, stderr=True)


shell(
    "gatk3 {java_opts} -T RealignerTargetCreator"
    " -nt {snakemake.threads}"
    " {extra}"
    " -I {snakemake.input.bam}"
    " -R {snakemake.input.ref}"
    " {known}"
    " {bed}"
    " -o {snakemake.output.intervals}"
    " {log}"
)
