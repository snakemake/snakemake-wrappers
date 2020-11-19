__author__ = "William Rowell"
__copyright__ = "Copyright 2020, William Rowell"
__email__ = "wrowell@pacb.com"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    """
    (whatshap phase \
        {extra} \
        --chromosome {snakemake.wildcards.chromosome} \
        --output {snakemake.output} \
        --reference {snakemake.input.reference} \
        {snakemake.input.vcf} \
        {snakemake.input.phaseinput}) {log}
    """
)
