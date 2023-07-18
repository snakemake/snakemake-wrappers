__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2023, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

if snakemake.input.get("normal"):
    extra += f" --matched-normal {snakemake.input.normal}"

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' CalculateContamination"
        " --input {snakemake.input.tumor}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " --output {snakemake.output}"
        " {log}"
    )
