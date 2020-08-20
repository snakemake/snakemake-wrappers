__author__ = "Fabian Kilpert"
__copyright__ = "Copyright 2020, Fabian Kilpert"
__email__ = "fkilpert@gmail.com"
__license__ = "MIT"


import os


log = snakemake.log_fmt_shell()


os.system(
    f"picard BedToIntervalList "
    f"{snakemake.params} "
    f"INPUT={snakemake.input.bed} "
    f"SEQUENCE_DICTIONARY={snakemake.input.dict} "
    f"OUTPUT={snakemake.output} "
    f"{log} "
)
