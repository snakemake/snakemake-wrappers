__author__ = "Brett Copeland"
__copyright__ = "Copyright 2021, Brett Copeland"
__email__ = "brcopeland@ucsd.edu"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

log = snakemake.log_fmt_shell()

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "picard CollectGcBiasMetrics"
        " {java_opts} {extra}"
        " --INPUT {snakemake.input.bam}"
        " --TMP_DIR {tmpdir}"
        " --OUTPUT {snakemake.output.metrics}"
        " --CHART {snakemake.output.chart}"
        " --SUMMARY_OUTPUT {snakemake.output.summary}"
        " --REFERENCE_SEQUENCE {snakemake.input.ref}"
        " {log}"
    )
