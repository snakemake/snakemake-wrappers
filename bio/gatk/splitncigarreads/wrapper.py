__author__ = "Jan Forster"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "jan.forster@uk-essen.de"
__license__ = "MIT"

import os
import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' SplitNCigarReads"
        " --reference {snakemake.input.ref}"
        " --input {snakemake.input.bam}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " --output {snakemake.output[0]}"
        " {log}"
    )
