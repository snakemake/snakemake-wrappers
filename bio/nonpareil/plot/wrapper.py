__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2024, Filipe G. Vieira"
__license__ = "MIT"


from pathlib import Path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


for output in snakemake.output:
    ext = Path(output).suffix.lstrip(".")
    if ext in ["json", "tsv", "pdf"]:
        extra += f" --{ext} {output}"


shell("NonpareilCurves.R {extra} {snakemake.input} {log}")
