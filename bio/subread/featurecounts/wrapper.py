__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

# optional input files and directories
fasta = snakemake.input.get("fasta", "")
chr_names = snakemake.input.get("chr_names", "")
r_path = snakemake.params.get("r_path", "")

if fasta:
    extra += " -G {}".format(fasta)
if chr_names:
    extra += " -A {}".format(chr_names)
if r_path:
    extra += " --Rpath {}".format(r_path)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "featureCounts"
        " -T {snakemake.threads}"
        " -a {snakemake.input.annotation}"
        " {extra}"
        " --tmpDir {tmpdir}"
        " -o {snakemake.output[0]}"
        " {snakemake.input.samples}"
        " {log}"
    )
