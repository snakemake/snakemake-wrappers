__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2023, Thibault Dayris"
__mail__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

annotation = snakemake.input.annotation
records = snakemake.output.records

# Input format control
if annotation.endswith(".bed"):
    extra += " --in-bed "
elif annotation.endswith(".tlf"):
    extra += " --in-tlf "
elif annotation.endswith(".gtf"):
    pass
else:
    raise ValueError("Unknown annotation format")


# Output format control
if records.endswith((".gtf", ".gff", ".gff3")):
    extra += " -T "
elif records.endswith(".bed"):
    extra += " --bed "
elif records.endswith(".tlf"):
    extra += " --tlf "
elif records.endswith((".fasta", ".fa", ".fna")):
    pass
else:
    raise ValueError("Unknown records format")


# Optional input files
ids = snakemake.input.get("ids", "")
if ids:
    extra += f" --ids {ids} "

nids = snakemake.input.get("nids", "")
if nids:
    if ids:
        raise ValueError(
            "Provide either sequences ids to keep, or to drop."
            " Or else, an empty file is produced."
        )
    extra += f" --nids {nids} "

seq_info = snakemake.input.get("seq_info", "")
if seq_info:
    extra += f" -s {seq_info} "

sort_by = snakemake.input.get("sort_by", "")
if sort_by:
    extra += f" --sort-by {sort_by} "

attr = snakemake.input.get("attr", "")
if attr:
    if not records.endswith((".gtf", ".gff", ".gff3")):
        raise ValueError(
            "GTF attributes specified in input, "
            "but records are not in GTF/GFF format."
        )
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
