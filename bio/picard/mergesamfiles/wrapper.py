"""Snakemake wrapper for picard MergeSamFiles."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

if snakemake.threads == 1:
    pass
elif snakemake.threads == 2:
    extra += " --USE_THREADING"
else:
    raise ValueError(
        "Picard can use, at most, one extra thread for compression/decompression."
    )

inputs = " ".join("--INPUT {}".format(in_) for in_ in snakemake.input)
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "picard MergeSamFiles"
        " {java_opts}"
        " {inputs}"
        " {extra}"
        " --TMP_DIR {tmpdir}"
        " --OUTPUT {snakemake.output[0]}"
        " {log}"
    )
