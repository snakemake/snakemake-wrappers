__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2023, Thibault Dayris"
__mail__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

annotation = snakemake.input["annotation"]
records = snakemake.output["records"]

# Input format control
if (annotation.endswith(".bed")) and (" --in-bed " not in extra):
    extra += " --in-bed "
elif (annotation.endswith(".tlf")) and (" --in-tlf " not in extra):
    extra += " --in-tlf "


# Output format control
if records.endswith(".gtf") and (" -T " not in extra):
    extra += " -T "
elif (records.endswith(".bed")) and (" --bed " not in extra):
    extra += " --bed "
elif (records.endswith(".tlf")) and (" --tlf " not in extra):
    extra += " --tlf "


# Optional input files
ids = snakemake.input.get("ids", "")
if ids:
    extra += f" --ids {ids} "

nids = snakemake.input.get("nids", "")
if nids:
    extra += f" --nids {nids} "

seq_info = snakemake.input.get("seq_info", "")
if seq_info:
    extra += f" -s {seq_info} "

sort_by = snakemake.input.get("sort_by", "")
if sort_by:
    extra += f" --sort-by {sort_by} "

attr = snakemake.input.get("attr", "")
if attr:
    extra += f" --attrs {attr} "

chr_replace = snakemake.input.get("chr_replace", "")
if chr_replace:
    extra += f" -m {chr_replace} "


# Optional output files
dupinfo = snakemake.output.get("dupinfo", "")
if dupinfo:
    extra += f" -d {dupinfo} "


shell(
    "gffread {extra} "
    "-o {records} "
    "{snakemake.input.fasta} "
    "{annotation} "
    "{log} "
)
