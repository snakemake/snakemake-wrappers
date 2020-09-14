__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")

shell(
    "bcftools concat {extra} -o {snakemake.output[0]} "
    "{snakemake.input.calls}"
)
