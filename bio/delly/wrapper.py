__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell


exclude = (
    "-x {}".format(snakemake.input.exclude)
    if snakemake.input.get("exclude", "")
    else ""
)

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "OMP_NUM_THREADS={snakemake.threads} delly call {extra} "
    "{exclude} -g {snakemake.input.ref} "
    "-o {snakemake.output[0]} {snakemake.input.samples} {log}"
)
