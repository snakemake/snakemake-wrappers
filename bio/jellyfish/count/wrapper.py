__author__ = "William Rowell"
__copyright__ = "Copyright 2020, William Rowell"
__email__ = "wrowell@pacb.com"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


shell(
    """
    (jellyfish count \
        {extra} \
        --mer-len={snakemake.params.kmer_length} \
        --size={snakemake.params.size} \
        --threads={snakemake.threads} \
        --output={snakemake.output} \
        {snakemake.input}) {log}
    """
)
