__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

os.system(
    f"picard "
    "CreateSequenceDictionary "
    "{extra} "
    "R={snakemake.input[0]} "
    "O={snakemake.output[0]} "
    "{log}"
)
