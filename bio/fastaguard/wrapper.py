from snakemake.shell import shell

profile = snakemake.params.get("profile", "assembly")
gate = snakemake.params.get("gate", "pipeline")
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "set +e; "
    "fastaguard {snakemake.input.fasta} "
    "--profile {profile} "
    "--gate {gate} "
    "--out {snakemake.output.html} "
    "--json {snakemake.output.json} "
    "--tsv {snakemake.output.tsv} "
    "--multiqc {snakemake.output.multiqc} "
    "{extra} "
    "{log}; "
    'status="$?"; '
    "set -e; "
    'printf "%s\\n" "$status" > {snakemake.output.exit_code}; '
    'if [ "$status" -eq 3 ] || [ "$status" -gt 3 ]; then exit "$status"; fi'
)
