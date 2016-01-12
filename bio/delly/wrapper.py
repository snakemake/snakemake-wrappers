__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell


shell(
    "OMP_NUM_THREADS={snakemake.threads} delly {snakemake.params} "
    "-t {snakemake.wildcards.type} -g {snakemake.input.ref} "
    "-o {snakemake.output[0]} {snakemake.input.samples} &> {snakemake.log}")
