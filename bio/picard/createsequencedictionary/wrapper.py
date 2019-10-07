__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "picard "
    "CreateSequenceDictionary "
    "{extra} "
    "R={snakemake.input[0]} "
    "O={snakemake.output[0]} "
    "{log}"
)
