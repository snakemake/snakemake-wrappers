__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)


shell(
    "rsem-calculate-expression "
    "{snakemake.params} "
    "-p {snakemake.threads} "
    "--alignments "
    "{snakemake.input[0]} "
    "{snakemake.params.index} "
    "{snakemake.params.prefix} "
    "{log}")
