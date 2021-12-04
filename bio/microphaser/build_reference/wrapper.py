__author__ = "Jan Forster"
__copyright__ = "Copyright 2021, Jan Forster"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "microphaser build_reference "
    "{extra} "
    "--reference {snakemake.input.ref_peptides} "
    "--output {snakemake.output.bin} "
    "> {snakemake.output.peptides} "
    "{log}"
)
