__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import os

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

os.system(f"tabix {snakemake.params} {snakemake.input[0]} {log}")
