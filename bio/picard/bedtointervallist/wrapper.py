__author__ = "Fabian Kilpert"
__copyright__ = "Copyright 2020, Fabian Kilpert"
__email__ = "fkilpert@gmail.com"
__license__ = "MIT"


import os


log = snakemake.log_fmt_shell()


os.system(
    f"picard BedToIntervalList "
    "{snakemake.params} "
    "INPUT={snakemake.input.bed} "
    "SEQUENCE_DICTIONARY={snakemake.input.dict} "
    "OUTPUT={snakemake.output} "
    "{log} "
)
