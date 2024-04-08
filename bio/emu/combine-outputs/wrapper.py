__author__ = "Curro Campuzano Jimenez"
__copyright__ = "Copyright 2024, Curro Campuzano Jimenez"
__email__ = "campuzanocurro@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import tempfile
import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

input_files = snakemake.input
if not isinstance(input_files, list):
    raise ValueError("Input should be a list of files: " + str(input_files) + "!")

if snakemake.output.get("abundance") and snakemake.output.get("taxonomy"):
    split = True
    extra += " --split-tables"
    taxonomy = snakemake.output.get("taxonomy")
    abundances = snakemake.output.get("abundance")
elif isinstance(snakemake.output[0], str):
    split = False
    table = snakemake.output[0]
else:
    raise ValueError(
        "Please provide either one TSV file, or two named TSV files (abundances and taxonomy)"
    )

if "--split-tables" in extra and not split:
    raise ValueError("You cannot use --split-tables and produce a single output.")

rank = snakemake.params.get("rank", "tax_id")
counts = "--counts" in extra


with tempfile.TemporaryDirectory() as tmpdir:
    for infile in input_files:
        # Files has to end in tsv, and contain rel_abundances
        temp = os.path.join(tmpdir, os.path.basename(infile))
        if not temp.endswith("rel_abundances.tsv"):
            temp = os.path.splitext(infile)[0] + "-rel_abundances.tsv"
        os.symlink(infile, temp)
    shell("emu combine-outputs {tmpdir} {rank} {extra} {log}")
    if split and counts:
        shell("mv {tmpdir}/emu-combined-taxonomy-{rank}.tsv {taxonomy}")
        shell("mv {tmpdir}/emu-combined-abundance-{rank}-counts.tsv {abundances}")
    elif split and not counts:
        shell("mv {tmpdir}/emu-combined-taxonomy-{rank}.tsv {taxonomy}")
        shell("mv {tmpdir}/emu-combined-abundance-{rank}.tsv {abundances}")
    elif not split and counts:
        shell("mv {tmpdir}/emu-combined-{rank}-counts.tsv {table}")
    elif not split and not counts:
        shell("mv {tmpdir}/emu-combined-{rank}.tsv {table}")
