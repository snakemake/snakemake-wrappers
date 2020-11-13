__author__ = "Fabian Kilpert"
__copyright__ = "Copyright 2020, Fabian Kilpert"
__email__ = "fkilpert@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

log = snakemake.log_fmt_shell()

extra = snakemake.params
java_opts = get_java_opts(snakemake)

shell(
    "picard BedToIntervalList "
    "{java_opts} {extra} "
    "INPUT={snakemake.input.bed} "
    "SEQUENCE_DICTIONARY={snakemake.input.dict} "
    "OUTPUT={snakemake.output} "
    "{log} "
)
