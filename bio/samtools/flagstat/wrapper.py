__author__ = "Christopher Preusch"
__copyright__ = "Copyright 2017, Christopher Preusch"
__email__ = "cpreusch[at]ust.hk"
__license__ = "MIT"


import os


os.system(f"samtools flagstat {snakemake.input[0]} > {snakemake.output[0]}")
