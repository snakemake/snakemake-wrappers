__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

os.system(
    f"picard "
    f"CreateSequenceDictionary "
    f"{extra} "
    f"R={snakemake.input[0]} "
    f"O={snakemake.output[0]} "
    f"{log}"
)
