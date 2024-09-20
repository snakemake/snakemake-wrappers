__author__ = "Curro Campuzano Jimenez"
__copyright__ = "Copyright 2024, Curro Campuzano Jimenez"
__email__ = "campuzanocurro@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import tempfile
import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

# Infer format of input file
if len(snakemake.input.reads) == 1:
    in_fmt = "fasta"
elif len(snakemake.input.reads) == 2:
    in_fmt = "fastq"
else:
    raise ValueError("invalid number of input files")

if db := snakemake.input.get("db", "")
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
    if out_unclassified_fq := snakemake.output.get("unclassified"):
        shell("mv {tmpdir}/output_unclassified_mapped.{in_fmt} {out_unclassified_fq}")
    if out_unmapped_fq := snakemake.output.get("unmapped"):
        shell("mv {tmpdir}/output_unmapped.{in_fmt} {out_unmapped_fq}")
