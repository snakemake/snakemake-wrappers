__author__ = "Lauri Mesilaakso"
__copyright__ = "Copyright 2022, Lauri Mesilaakso"
__email__ = "lauri.mesilaakso@gmail.com"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

java_opts = get_java_opts(snakemake)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' DepthOfCoverage"
        " --input {snakemake.input.bam}"
        " --intervals {snakemake.input.intervals}"
        " --reference {snakemake.input.fasta}"
        " --output {snakemake.output.basename}"
        " --tmp-dir {tmpdir}"
        " {extra}"
        " {log}"
    )
