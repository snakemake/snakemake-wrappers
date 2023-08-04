__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")


clusters = snakemake.output.get("clusters", "")
if clusters:
    clusters = f"--output-cluster-definition {clusters}"


repres = snakemake.output.get("repres", "")
if repres:
    repres = f"--output-representative-list {repres}"


with tempfile.NamedTemporaryFile() as tmp:
    shell("ls {snakemake.input} > {tmp.name}")

    shell(
        "galah cluster"
        " --threads {snakemake.threads}"
        " --genome-fasta-list {tmp.name}"
        " {extra}"
        " {clusters}"
        " {repres}"
        " {log}"
    )
