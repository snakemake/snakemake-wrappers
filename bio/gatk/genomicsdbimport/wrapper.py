__author__ = "Brett Copeland"
__copyright__ = "Copyright 2021, Brett Copeland"
__email__ = "brcopeland@ucsd.edu"
__license__ = "MIT"


import os

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

gvcfs = list(map("-V {}".format, snakemake.input.gvcfs))
tmp_dir = snakemake.params.get("tmp_dir", "")
if tmp_dir:
    tmp_dir = "--tmp-dir {}".format(tmp_dir)

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
shell(
    "gatk --java-options '{java_opts}' GenomicsDBImport {extra} "
    "{gvcfs} "
    "{tmp_dir} "
    "-L {snakemake.input.interval_file} "
    "--genomicsdb-workspace-path {snakemake.output.genomicsdb_dir} {log}"
)
