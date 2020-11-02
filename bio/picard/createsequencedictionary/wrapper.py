__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "picard "
    "CreateSequenceDictionary "
    "{java_opts} {extra} "
    "R={snakemake.input[0]} "
    "O={snakemake.output[0]} "
    "{log}"
)
