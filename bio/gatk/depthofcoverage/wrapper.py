__author__ = "Lauri Mesilaakso"
__copyright__ = "Copyright 2022, Lauri Mesilaakso"
__email__ = "lauri.mesilaakso@gmail.com"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts
from os import path

java_opts = get_java_opts(snakemake)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Extract basename from the output file names
out_basename = path.commonprefix(snakemake.output).rstrip(".")

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' DepthOfCoverage"
        " --input {snakemake.input.bam}"
        " --intervals {snakemake.input.intervals}"
        " --reference {snakemake.input.fasta}"
        " --output {out_basename}"
        " --tmp-dir {tmpdir}"
        " {extra}"
        " {log}"
    )
