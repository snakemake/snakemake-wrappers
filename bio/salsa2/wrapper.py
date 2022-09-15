__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


enzyme = snakemake.params.get("enzyme", "")
if enzyme:
    enzyme = f"--enzyme {enzyme}"

gfa = snakemake.input.get("gfa", "")
if gfa:
    gfa = f"--gfa {gfa}"


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "run_pipeline.py"
        " --assembly {snakemake.input.fas}"
        " --length {snakemake.input.fai}"
        " --bed {snakemake.input.bed}"
        " {enzyme}"
        " {gfa}"
        " {extra}"
        " --output {tmpdir}"
        " {log}"
    )

    if snakemake.output.get("agp"):
        shell("cat {tmpdir}/scaffolds_FINAL.agp > {snakemake.output.agp}")
    if snakemake.output.get("fas"):
        shell("cat {tmpdir}/scaffolds_FINAL.fasta > {snakemake.output.fas}")
