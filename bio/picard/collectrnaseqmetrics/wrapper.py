__author__ = "Brett Copeland"
__copyright__ = "Copyright 2021, Brett Copeland"
__email__ = "brcopeland@ucsd.edu"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

log = snakemake.log_fmt_shell()

strand = snakemake.params.get("strand", "NONE")
extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)


ref = snakemake.input.get("ref", "")
if ref:
    ref = f"--REFERENCE_SEQUENCE {ref}"


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "picard CollectRnaSeqMetrics"
        " {java_opts} {extra}"
        " --INPUT {snakemake.input.bam}"
        " {ref}"
        " --REF_FLAT {snakemake.input.refflat}"
        " --STRAND_SPECIFICITY {strand}"
        " --TMP_DIR {tmpdir}"
        " --OUTPUT {snakemake.output}"
        " {log}"
    )
