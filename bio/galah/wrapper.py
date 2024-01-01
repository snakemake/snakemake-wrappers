__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")


fas = snakemake.input.get("fas", "")
if fas:
    fas = f"--genome-fasta-files {' '.join(fas)}"


fas_list = snakemake.input.get("fas_list", "")
if fas_list:
    fas_list = f"--genome-fasta-list {fas_list}"


clusters = snakemake.output.get("clusters", "")
if clusters:
    clusters = f"--output-cluster-definition {clusters}"


repres = snakemake.output.get("repres", "")
if repres:
    repres = f"--output-representative-list {repres}"


shell(
    "galah cluster"
    " --threads {snakemake.threads}"
    " {fas}"
    " {fas_list}"
    " {extra}"
    " {clusters}"
    " {repres}"
    " {log}"
)
