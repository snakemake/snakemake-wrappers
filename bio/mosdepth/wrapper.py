__author__ = "William Rowell"
__copyright__ = "Copyright 2020, William Rowell"
__email__ = "wrowell@pacb.com"
__license__ = "MIT"

import sys
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

bed = snakemake.input.get("bed", "")
by = snakemake.params.get("by", "")
if by:
    if bed:
        sys.exit(
            "Either provide a bed input file OR a window size via params.by, not both."
        )
    else:
        by = f"--by {by}"
if bed:
    by = f"--by {bed}"

quantize_out = False
thresholds_out = False
regions_bed_out = False
region_dist_out = False
for file in snakemake.output:
    if ".per-base." in file and "--no-per-base" in extra:
        sys.exit(
            "You asked not to generate per-base output (--no-per-base), but your rule specifies a '.per-base.' output file. Remove one of the two."
        )
    if ".quantized.bed.gz" in file:
        quantize_out = True
    if ".thresholds.bed.gz" in file:
        thresholds_out = True
    if ".mosdepth.region.dist.txt" in file:
        region_dist_out = True
    if ".regions.bed.gz" in file:
        regions_bed_out = True


if by and not regions_bed_out:
    sys.exit(
        "You ask for by-region output. Please also specify *.regions.bed.gz as a rule output."
    )

if by and not region_dist_out:
    sys.exit(
        "You ask for by-region output. Please also specify *.mosdepth.region.dist.txt as a rule output."
    )

if (region_dist_out or regions_bed_out) and not by:
    sys.exit(
        "You specify *.regions.bed.gz and/or *.mosdepth.region.dist.txt as a rule output. You also need to ask for by-region output via 'input.bed' or 'params.by'."
    )

quantize = snakemake.params.get("quantize", "")
if quantize:
    if not quantize_out:
        sys.exit(
            "You ask for quantized output via params.quantize. Please also specify *.quantized.bed.gz as a rule output."
        )
    quantize = f"--quantize {quantize}"

if not quantize and quantize_out:
    sys.exit(
        "The rule has output *.quantized.bed.gz specified. Please also specify params.quantize to actually generate it."
    )


thresholds = snakemake.params.get("thresholds", "")
if thresholds:
    if not thresholds_out:
        sys.exit(
            "You ask for --thresholds output via params.thresholds. Please also specify *.thresholds.bed.gz as a rule output."
        )
    thresholds = f"--thresholds {thresholds}"

if not thresholds and thresholds_out:
    sys.exit(
        "The rule has output *.thresholds.bed.gz specified. Please also specify params.thresholds to actually generate it."
    )


precision = snakemake.params.get("precision", "")
if precision:
    precision = f"MOSDEPTH_PRECISION={precision}"


fasta = snakemake.input.get("fasta", "")
if fasta:
    fasta = f"--fasta {fasta}"


# mosdepth takes additional threads through its option --threads
# One thread for mosdepth
# Other threads are *additional* decompression threads passed to the '--threads' argument
threads = "" if snakemake.threads <= 1 else "--threads {}".format(snakemake.threads - 1)


# named output summary = "*.mosdepth.summary.txt" is required
prefix = snakemake.output.summary.replace(".mosdepth.summary.txt", "")


shell(
    "({precision} mosdepth {threads} {fasta} {by} {quantize} {thresholds} {extra} {prefix} {snakemake.input.bam}) {log}"
)
