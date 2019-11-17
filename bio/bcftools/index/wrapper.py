__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell

## Extract arguments
extra = snakemake.params.get("extra", "")

shell("bcftools index" " {extra}" " {snakemake.input[0]}")
