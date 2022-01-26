__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2019, Patrik Smeds"
__email__ = "patrik.smeds@mail.com"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


log = snakemake.log_fmt_shell()

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "picard CollectTargetedPcrMetrics"
        " {java_opts} {extra}"
        " --INPUT {snakemake.input.bam}"
        " --TMP_DIR {tmpdir}"
        " --OUTPUT {snakemake.output[0]}"
        " --AMPLICON_INTERVALS {snakemake.input.amplicon_intervals}"
        " --TARGET_INTERVALS {snakemake.input.target_intervals}"
        " {log}"
    )
