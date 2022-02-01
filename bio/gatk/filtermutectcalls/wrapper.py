__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2021, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' FilterMutectCalls"
        " --variant {snakemake.input.vcf}"
        " --reference {snakemake.input.ref}"
        " {extra}"
        " --tmp-file {tmpdir}"
        " --output {snakemake.output.vcf}"
        " {log}"
    )
