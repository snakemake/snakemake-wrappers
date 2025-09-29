__author__ = "William Rowell"
__copyright__ = "Copyright 2020, William Rowell"
__email__ = "wrowell@pacb.com"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)


if not snakemake.output.get("per_base"):
    extra += " --no-per-base"


if snakemake.output.get("quant"):
    extra += f" --quantize {snakemake.params.quantize}"


if snakemake.output.get("thres"):
    extra += f" --thresholds {snakemake.params.thresholds}"


if snakemake.output.get("bed_dist") or snakemake.output.get("bed"):
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

    if snakemake.output.get("per_base"):
        assert snakemake.output.per_base.endswith("gz")
        shell(
            "mv --verbose {tmpdir}/temp.per-base.bed.gz {snakemake.output.per_base} {log}"
        )

    if snakemake.output.get("quant"):
        assert snakemake.output.quant.endswith("gz")
        shell(
            "mv --verbose {tmpdir}/temp.quantized.bed.gz {snakemake.output.quant} {log}"
        )

    if snakemake.output.get("thres"):
        assert snakemake.output.thres.endswith("gz")
        shell(
            "mv --verbose {tmpdir}/temp.thresholds.bed.gz {snakemake.output.thres} {log}"
        )

    if snakemake.output.get("dist"):
        shell(
            "mv --verbose {tmpdir}/temp.mosdepth.global.dist.txt {snakemake.output.dist} {log}"
        )

    if snakemake.output.get("bed_dist"):
        shell(
            "mv --verbose {tmpdir}/temp.mosdepth.region.dist.txt {snakemake.output.bed_dist} {log}"
        )

    if snakemake.output.get("bed"):
        assert snakemake.output.bed.endswith("gz")
        shell("mv --verbose {tmpdir}/temp.regions.bed.gz {snakemake.output.bed} {log}")
