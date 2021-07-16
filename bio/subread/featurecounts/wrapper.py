__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

# optional input files and directories
fasta = snakemake.input.get("fasta", "")
chr_names = snakemake.input.get("chr_names", "")
tmp_dir = snakemake.params.get("tmp_dir", "")
r_path = snakemake.params.get("r_path", "")

if fasta:
    extra += " -G {}".format(fasta)
if chr_names:
    extra += " -A {}".format(chr_names)
if tmp_dir:
    extra += " --tmpDir {}".format(tmp_dir)
if r_path:
    extra += " --Rpath {}".format(r_path)

shell(
    "(featureCounts"
    " {extra}"
    " -T {snakemake.threads}"
    " -J"
    " -a {snakemake.input.annotation}"
    " -o {snakemake.output[0]}"
    " {snakemake.input.sam})"
    " {log}"
)
