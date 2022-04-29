__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

# optional input files and directories
strand = snakemake.params.get("strand", 0)

fasta = snakemake.input.get("fasta", "")
if fasta:
    fasta = f"-G {fasta}"

chr_names = snakemake.input.get("chr_names", "")
if chr_names:
    chr_names = f"-A {chr_names}"

r_path = snakemake.params.get("r_path", "")
if r_path:
    r_path = f"--Rpath {r_path}"


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "featureCounts"
        " -T {snakemake.threads}"
        " -s {strand}"
        " -a {snakemake.input.annotation}"
        " {fasta}"
        " {chr_names}"
        " {r_path}"
        " {extra}"
        " --tmpDir {tmpdir}"
        " -o {snakemake.output[0]}"
        " {snakemake.input.samples}"
        " {log}"
    )
