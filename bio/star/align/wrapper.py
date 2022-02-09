__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import os
import tempfile
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

fq1 = snakemake.input.get("fq1")
assert fq1 is not None, "input-> fq1 is a required input parameter"
fq1 = (
    [snakemake.input.fq1]
    if isinstance(snakemake.input.fq1, str)
    else snakemake.input.fq1
)
fq2 = snakemake.input.get("fq2")
if fq2:
    fq2 = (
        [snakemake.input.fq2]
        if isinstance(snakemake.input.fq2, str)
        else snakemake.input.fq2
    )
    assert len(fq1) == len(
        fq2
    ), "input-> equal number of files required for fq1 and fq2"
input_str_fq1 = ",".join(fq1)
input_str_fq2 = ",".join(fq2) if fq2 is not None else ""
input_str = " ".join([input_str_fq1, input_str_fq2])

if fq1[0].endswith(".gz"):
    readcmd = "--readFilesCommand zcat"
else:
    readcmd = ""

if "SortedByCoordinate" in extra:
    bamprefix = "Aligned.sortedByCoord.out."
else:
    bamprefix = "Aligned.out."

index = snakemake.input.get("idx")
if not index:
    index = snakemake.params.get("idx", "")

outprefix = snakemake.output[0].split(bamprefix)[0]
if outprefix == os.path.dirname(snakemake.output[0]):
    outprefix += "/"

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "STAR "
        " --runThreadN {snakemake.threads}"
        " --genomeDir {index}"
        " --readFilesIn {input_str}"
        " {readcmd}"
        " {extra}"
        " --outTmpDir {tmpdir}/STARtmp"
        " --outFileNamePrefix {outprefix}"
        " --outStd Log"
        " {log}"
    )

    if snakemake.output.get("bam"):
        shell("cp {outprefix}{bamprefix}bam {snakemake.output.bam:q}")
    elif snakemake.output.get("bam"):
        shell("cp {outprefix}{bamprefix}sam {snakemake.output.sam:q}")
