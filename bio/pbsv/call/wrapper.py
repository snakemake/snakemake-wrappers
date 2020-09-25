__author__ = "William Rowell"
__copyright__ = "Copyright 2020, William Rowell"
__email__ = "wrowell@pacb.com"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    """
    (pbsv call \
        --log-level {snakemake.params.loglevel} \
        --num-threads {snakemake.threads} \
        {extra} \
        {snakemake.input.reference} {snakemake.input.svsigs} {snakemake.output}) {log}
    """
)
