__author__ = "Curro Campuzano Jimenez"
__copyright__ = "Copyright 2024, Curro Campuzano Jimenez"
__email__ = "campuzanocurro@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import tempfile
import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")
db = snakemake.input.get("db", "")
if db:
    db = f"--db {db}"

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "emu abundance {snakemake.input.reads} {db}"
        " --keep-files --output-dir {tmpdir}"
        " --output-basename output --output-unclassified"
        " --threads {snakemake.threads}"
        " {extra}"
        " {log}"
    )
    if out_tsv := snakemake.output.get("abundances"):
        shell("mv {tmpdir}/output_rel-abundance.tsv {out_tsv}")
    if out_sam := snakemake.output.get("alignments"):
        shell("mv {tmpdir}/output_emu_alignments.sam {out_sam}")
    if out_fa := snakemake.output.get("unclassified"):
        shell("mv {tmpdir}/output_unclassified.fa {out_fa}")
