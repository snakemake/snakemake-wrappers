from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)


shell(
    "diamond makedb"
    " --threads {snakemake.threads}"
    " --in {snakemake.input.fname}"
    " --db {snakemake.output.fname}}"
    " {extra}"
    " {log}"
)
