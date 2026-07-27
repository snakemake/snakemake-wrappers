from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "fastaguard {snakemake.input.fasta} "
    "--out {snakemake.output.html} "
    "--json {snakemake.output.json} "
    "--tsv {snakemake.output.tsv} "
    "--multiqc {snakemake.output.multiqc} "
    "{extra} "
    "{log}"
)
