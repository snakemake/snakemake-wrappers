__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2018, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

shell(
    "bcftools merge {snakemake.params} -o {snakemake.output[0]} "
    "{snakemake.input.calls}"
)
