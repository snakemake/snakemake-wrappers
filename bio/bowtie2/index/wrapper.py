__author__ = "N Tessa Pierce"
__copyright__ = "Copyright 2018, N Tessa Pierce"
__email__ = "ntpierce@ucdavis.edu"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "bowtie2-build --threads {snakemake.threads} {snakemake.params.extra} {snakemake.input} {snakemake.params.index} {log}"
)
shell("touch {snakemake.output.donefile}")
