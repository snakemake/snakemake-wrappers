__author__ = "Jan Forster"
__copyright__ = "Copyright 2021, Jan Forster"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "microphaser somatic {snakemake.input.bam} "
    "{extra} "
    "--ref {snakemake.input.ref} "
    "--variants {snakemake.input.variants} "
    "--normal-output {snakemake.output.normal} "
    "--tsv {snakemake.output.tsv} "
    "> {snakemake.output.tumor} "
    "< {snakemake.input.annotation} "
    "{log}"
)
