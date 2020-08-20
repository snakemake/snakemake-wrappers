__author__ = "Dayne Filer"
__copyright__ = "Copyright 2019, Dayne Filer"
__email__ = "dayne.filer@gmail.com"
__license__ = "MIT"


import os


os.system(
    f"bcftools norm {snakemake.params} {snakemake.input[0]} " "-o {snakemake.output[0]}"
)
