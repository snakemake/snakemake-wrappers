__author__ = "Curro Campuzano Jimenez"
__copyright__ = "Copyright 2024, Curro Campuzano Jimenez"
__email__ = "campuzanocurro@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import tempfile
import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

taxonomy = snakemake.output.get("taxonomy", "")
abundances = snakemake.output.get("abundances", "")
if taxonomy and abundances:
    split = True
    extra += " --split-tables"
else:
    split = False

rank = snakemake.params.get("rank", "tax_id")
counts = "--counts" in extra


with tempfile.TemporaryDirectory() as tmpdir:
    for infile in snakemake.input:
        # Files has to end in tsv, and contain rel_abundances
        temp_basename = os.path.basename(infile)
        if not temp_basename.endswith("_rel-abundance.tsv"):
            temp_basename = os.path.splitext(infile)[0] + "_rel-abundance.tsv"
        temp = os.path.join(tmpdir, temp_basename)
        os.link(infile, temp)
    shell("emu combine-outputs {tmpdir} {rank} {extra} {log}")
    if split and counts:
        shell("mv {tmpdir}/emu-combined-taxonomy-{rank}.tsv {taxonomy}")
        shell("mv {tmpdir}/emu-combined-abundance-{rank}-counts.tsv {abundances}")
    elif split and not counts:
        shell("mv {tmpdir}/emu-combined-taxonomy-{rank}.tsv {taxonomy}")
        shell("mv {tmpdir}/emu-combined-abundance-{rank}.tsv {abundances}")
    elif not split and counts:
        shell("mv {tmpdir}/emu-combined-{rank}-counts.tsv {abundances}")
    elif not split and not counts:
        shell("mv {tmpdir}/emu-combined-{rank}.tsv {abundances}")
