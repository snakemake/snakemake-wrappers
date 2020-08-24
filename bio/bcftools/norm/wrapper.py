__author__ = "Dayne Filer"
__copyright__ = "Copyright 2019, Dayne Filer"
__email__ = "dayne.filer@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell


shell(
    "bcftools norm {snakemake.params} {snakemake.input[0]} " "-o {snakemake.output[0]}"
)
