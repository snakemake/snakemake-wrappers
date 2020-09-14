__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")

shell(
    "bcftools view {extra} {snakemake.input[0]} " "-o {snakemake.output[0]}"
)
