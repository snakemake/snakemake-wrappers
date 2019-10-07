__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell


shell(
    "bgzip --stdout {snakemake.input} > {snakemake.output} && tabix -p vcf {snakemake.output}"
)
