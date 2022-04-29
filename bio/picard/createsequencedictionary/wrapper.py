__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "picard CreateSequenceDictionary"
        " {java_opts} {extra}"
        " --REFERENCE {snakemake.input[0]}"
        " --TMP_DIR {tmpdir}"
        " --OUTPUT {snakemake.output[0]}"
        " {log}"
    )
