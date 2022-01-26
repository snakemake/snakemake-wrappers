__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

log = snakemake.log_fmt_shell()

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "picard CollectInsertSizeMetrics"
        " {java_opts} {extra}"
        " --INPUT {snakemake.input}"
        " --TMP_DIR {tmpdir}"
        " --OUTPUT {snakemake.output.txt}"
        " --Histogram_FILE {snakemake.output.pdf}"
        " {log}"
    )
