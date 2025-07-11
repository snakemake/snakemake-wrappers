__author__ = "William Rowell"
__copyright__ = "Copyright 2020, William Rowell"
__email__ = "wrowell@pacb.com"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)


# Check output files
per_base_out = quantize_out = thresholds_out = global_dist_out = region_dist_out = (
    regions_bed_out
) = False
for file in snakemake.output:
    if file.endswith(".per-base.bed.gz"):
        per_base_out = file
    if file.endswith(".quantized.bed.gz"):
        quantize_out = file
    if file.endswith(".thresholds.bed.gz"):
        thresholds_out = file
    if file.endswith(".mosdepth.global.dist.txt"):
        global_dist_out = file
    if file.endswith(".mosdepth.region.dist.txt"):
        region_dist_out = file
    if file.endswith(".regions.bed.gz"):
        regions_bed_out = file


if not per_base_out:
    extra += " --no-per-base"


if quantize_out:
    extra += f" --quantize {snakemake.params.quantize}"


if thresholds_out:
    extra += f" --thresholds {snakemake.params.thresholds}"


if region_dist_out or regions_bed_out:
    by = snakemake.input.get("bed", snakemake.params.get("by", False))
    if by:
        extra += f" --by {by}"


precision = snakemake.params.get("precision", "")
if precision:
    precision = f"MOSDEPTH_PRECISION={precision}"


fasta = snakemake.input.get("fasta", "")
if fasta:
    fasta = f"--fasta {fasta}"


# mosdepth uses additional threads for decompression, passed to the '--threads' argument
threads = "" if snakemake.threads <= 1 else "--threads {}".format(snakemake.threads - 1)


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "{precision} mosdepth {threads} {fasta} {extra} {tmpdir}/temp {snakemake.input.bam} {log}"
    )

    if snakemake.output.get("summary"):
        shell(
            "mv --verbose {tmpdir}/temp.mosdepth.summary.txt {snakemake.output.summary} {log}"
        )

    if per_base_out:
        shell("mv --verbose {tmpdir}/temp.per-base.bed.gz {per_base_out} {log}")

    if quantize_out:
        shell("mv --verbose {tmpdir}/temp.quantized.bed.gz {quantize_out} {log}")

    if thresholds_out:
        shell("mv --verbose {tmpdir}/temp.thresholds.bed.gz {thresholds_out} {log}")

    if global_dist_out:
        shell(
            "mv --verbose {tmpdir}/temp.mosdepth.global.dist.txt {global_dist_out} {log}"
        )

    if region_dist_out:
        shell(
            "mv --verbose {tmpdir}/temp.mosdepth.region.dist.txt {region_dist_out} {log}"
        )

    if regions_bed_out:
        shell("mv --verbose {tmpdir}/temp.regions.bed.gz {regions_bed_out} {log}")
