__author__ = "Brett Copeland"
__copyright__ = "Copyright 2021, Brett Copeland"
__email__ = "brcopeland@ucsd.edu"
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
        "gatk --java-options '{java_opts}' ApplyVQSR"
        " --variant {snakemake.input.vcf}"
        " --recal-file {snakemake.input.recal}"
        " --reference {snakemake.input.ref}"
        " --tranches-file {snakemake.input.tranches}"
        " --mode {snakemake.params.mode}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " --output {snakemake.output.vcf}"
        " {log}"
    )
