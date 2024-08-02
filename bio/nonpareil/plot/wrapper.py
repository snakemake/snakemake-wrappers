__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2024, Filipe G. Vieira"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


json = snakemake.output.get("json", "")
if json:
    json = f"--json {json}"

tsv = snakemake.output.get("tsv", "")
if tsv:
    tsv = f"--tsv {tsv}"

pdf = snakemake.output.get("pdf", "")
if pdf:
    pdf = f"--pdf {pdf}"


shell("NonpareilCurves.R {extra} {json} {tsv} {pdf} {snakemake.input} {log}")
