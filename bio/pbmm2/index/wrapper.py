__author__ = "William Rowell"
__copyright__ = "Copyright 2020, William Rowell"
__email__ = "wrowell@pacb.com"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    """
    (pbmm2 index \
    --num-threads {snakemake.threads} \
    --preset {snakemake.params.preset} \
    --log-level DEBUG \
    {extra} \
    {snakemake.input.reference} {snakemake.output}) {log}
    """
)
