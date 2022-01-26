__author__ = "Fabian Kilpert"
__copyright__ = "Copyright 2020, Fabian Kilpert"
__email__ = "fkilpert@gmail.com"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

log = snakemake.log_fmt_shell()

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "picard BedToIntervalList"
        " {java_opts} {extra}"
        " --INPUT {snakemake.input.bed}"
        " --SEQUENCE_DICTIONARY {snakemake.input.dict}"
        " --TMP_DIR {tmpdir}"
        " --OUTPUT {snakemake.output}"
        " {log}"
    )
