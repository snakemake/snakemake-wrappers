__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell


try:
    exclude = "-x " + snakemake.input.exclude
except AttributeError:
    exclude = ""


extra = snakemake.params.get("extra", "")


shell(
    "OMP_NUM_THREADS={snakemake.threads} delly {extra} "
    "{exclude} {snakemake.params.vartype} -g {snakemake.input.ref} "
    "-o {snakemake.output[0]} {snakemake.input.samples} &> {snakemake.log}")
