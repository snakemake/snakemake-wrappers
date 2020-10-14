__author__ = "Daniel Standage"
__copyright__ = "Copyright 2020, Daniel Standage"
__email__ = "daniel.standage@nbacc.dhs.gov"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
shell(
    "(bowtie2-build --threads {snakemake.threads} {snakemake.params.extra} "
    "{snakemake.input[0]} {snakemake.params.base}"
)
