__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2023, Thibault Dayris"
__mail__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Input files
annotation = snakemake.input.annotation

# Output files
records = snakemake.output.get("records", "")
if records:
    extra += f" -o {records}"

dupinfo = snakemake.output.get("dupinfo", "")
if dupinfo:
    extra += f" -d {dupinfo}"

transcript_fasta = snakemake.output.get("transcript_fasta", "")
if transcript_fasta:
    extra += f" -w {transcript_fasta}"

cds_fasta = snakemake.output.get("cds_fasta", "")
if cds_fasta:
    extra += f" -x {cds_fasta}"

protein_fasta = snakemake.output.get("protein_fasta", "")
if protein_fasta:
    extra += f" -y {protein_fasta}"


# Input format control
if annotation.endswith(".bed"):
    extra += " --in-bed"
elif annotation.endswith(".tlf"):
    extra += " --in-tlf"
elif annotation.endswith((".gtf", ".gff", ".gff3")):
    pass
else:
    raise ValueError("Unknown annotation format")

# Output format control
if not records:
    pass
elif records.endswith((".gtf", ".gff", ".gff3")):
    extra += " -T"
elif records.endswith(".bed"):
    extra += " --bed"
elif records.endswith(".tlf"):
    extra += " --tlf"
else:
    raise ValueError("Unknown records format")


# Optional input files
ids = snakemake.input.get("ids", "")
if ids:
    extra += f" --ids {ids}"

nids = snakemake.input.get("nids", "")
if nids:
    if ids:
        raise ValueError(
            "Provide either sequences ids to keep, or to drop."
            " Or else, an empty file is produced."
        )
    extra += f" --nids {nids}"

seq_info = snakemake.input.get("seq_info", "")
if seq_info:
    extra += f" -s {seq_info}"

sort_by = snakemake.input.get("sort_by", "")
if sort_by:
    extra += f" --sort-by {sort_by}"

attr = snakemake.input.get("attr", "")
if attr:
    if not records.endswith((".gtf", ".gff", ".gff3")):
        raise ValueError(
            "GTF attributes specified in input, "
            "but records are not in GTF/GFF format."
        )
    extra += f" --attrs {attr}"

chr_replace = snakemake.input.get("chr_replace", "")
if chr_replace:
    extra += f" -m {chr_replace}"


shell("gffread {extra} -g {snakemake.input.fasta} {annotation} {log}")
