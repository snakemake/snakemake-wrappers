from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)


shell(
    "diamond blastx"
    " --threads {snakemake.threads}"
    " --db {snakemake.input.fname_db}"
    " --query {snakemake.input.fname_fastq}"
    " --out {snakemake.output.fname}"
    " {extra}"
    " {log}"
)
