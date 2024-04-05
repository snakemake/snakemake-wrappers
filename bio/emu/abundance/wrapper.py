__author__ = "Curro Campuzano Jimenez"
__copyright__ = "Copyright 2024, Curro Campuzano Jimenez"
__email__ = "campuzanocurro@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import tempfile
import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")
threads = snakemake.threads or 1

# Check input (mandatory)
msg_error = "Please provide either one file of single-end 16S reads or two files of short paired-end 16S"
if not snakemake.input.get("reads"):
    raise ValueError(msg_error)
reads = snakemake.input.get("reads")
if isinstance(reads, list) and len(reads) > 2:
    raise ValueError(msg_error)

# Check database (optional)
database_cmd = ""
if database := snakemake.input.get("database_dir"):
    if not os.path.isdir(database):
        raise ValueError("Please provide a valid Emu database directory")
    database_cmd = f"--db {database}"

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "emu abundance {reads} {database_cmd}"
        " --keep-files --output-dir {tmpdir}"
        " --output-basename output --output-unclassified"
        " --threads	{threads}"
        " {extra}"
        " {log}"
    )
    if out_tsv := snakemake.output.get("abundances"):
        shell("mv {tmpdir}/output_rel-abundance.tsv {out_tsv}")
    if out_sam := snakemake.output.get("alignments"):
        shell("mv {tmpdir}/output_emu_alignments.sam {out_sam}")
    if out_fa := snakemake.output.get("unclassified"):
        shell("mv {tmpdir}/output_unclassified.fa {out_fa}")
