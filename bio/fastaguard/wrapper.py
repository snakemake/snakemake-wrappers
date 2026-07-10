from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
allowed_exit_codes = snakemake.params.get("allowed_exit_codes", [0])
if isinstance(allowed_exit_codes, int):
    allowed_exit_codes = [allowed_exit_codes]
allowed_exit_codes = " ".join(str(code) for code in allowed_exit_codes)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "set +e; "
    "fastaguard {snakemake.input.fasta} "
    "--out {snakemake.output.html} "
    "--json {snakemake.output.json} "
    "--tsv {snakemake.output.tsv} "
    "--multiqc {snakemake.output.multiqc} "
    "{extra} "
    "{log}; "
    'status="$?"; '
    "set -e; "
    'printf "%s\\n" "$status" > {snakemake.output.exit_code}; '
    'case " {allowed_exit_codes} " in *" $status "*) ;; *) exit "$status" ;; esac'
)
