__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "picard MarkDuplicatesWithMateCigar"
        " {java_opts} {extra}"
        " --INPUT {snakemake.input}"
        " --TMP_DIR {tmpdir}"
        " --OUTPUT {snakemake.output.bam}"
        " --METRICS_FILE {snakemake.output.metrics}"
        " {log}"
    )
