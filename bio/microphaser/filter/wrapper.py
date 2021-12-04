__author__ = "Jan Forster"
__copyright__ = "Copyright 2021, Jan Forster"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "microphaser filter "
    "{extra} "
    "--tsv {snakemake.input.tsv} "
    "--reference {snakemake.input.ref_peptides} "
    "--normal-output {snakemake.output.normal} "
    "--tsv-output {snakemake.output.tsv} "
    "--similar-removed {snakemake.output.removed_tsv} "
    "--removed-peptides {snakemake.output.removed_fasta} "
    " > {snakemake.output.tumor} "
    "{log}"
)
