__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2024, Filipe G. Vieira"
__license__ = "MIT"


from pathlib import Path
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


input = snakemake.input.get("input", "")

in_taxdump = snakemake.input.get("taxdump", "")
if in_taxdump:
    in_taxdump = Path(in_taxdump[0]).parent
    in_taxdump = f"--data-dir {in_taxdump}"


out_taxdump = snakemake.output.get("taxdump", "")
if out_taxdump:
    out_taxdump = Path(out_taxdump[0]).parent
    extra += f" --out-dir {out_taxdump}"
else:
    if snakemake.output[0].endswith("json"):
        extra += " --json"
    extra += f" --out-file {snakemake.output}"


shell(
    "taxonkit {snakemake.params.command}"
    " --threads {snakemake.threads}"
    " {in_taxdump}"
    " {extra}"
    " {input}"
    " {log}"
)
