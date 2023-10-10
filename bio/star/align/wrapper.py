__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import os
import tempfile
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)


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
    readcmd = "--readFilesCommand gunzip -c"
elif fq1[0].endswith(".bz2"):
    readcmd = "--readFilesCommand bunzip2 -c"
else:
    readcmd = ""

out_unmapped = snakemake.output.get("unmapped", "")
if out_unmapped:
    out_unmapped = "--outReadsUnmapped Fastx"

index = snakemake.input.get("idx")
if not index:
    index = snakemake.params.get("idx", "")


if "--outSAMtype BAM SortedByCoordinate" in extra:
    stdout = "BAM_SortedByCoordinate"
elif "BAM Unsorted" in extra:
    stdout = "BAM_Unsorted"
else:
    stdout = "SAM"


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "STAR "
        " --runThreadN {snakemake.threads}"
        " --genomeDir {index}"
        " --readFilesIn {input_str}"
        " {readcmd}"
        " {extra}"
        " {out_unmapped}"
        " --outTmpDir {tmpdir}/STARtmp"
        " --outFileNamePrefix {tmpdir}/"
        " --outStd {stdout}"
        " > {snakemake.output.aln}"
        " {log}"
    )

    if snakemake.output.get("reads_per_gene"):
        shell("cat {tmpdir}/ReadsPerGene.out.tab > {snakemake.output.reads_per_gene:q}")
    if snakemake.output.get("chim_junc"):
        shell("cat {tmpdir}/Chimeric.out.junction > {snakemake.output.chim_junc:q}")
    if snakemake.output.get("sj"):
        shell("cat {tmpdir}/SJ.out.tab > {snakemake.output.sj:q}")
    if snakemake.output.get("log"):
        shell("cat {tmpdir}/Log.out > {snakemake.output.log:q}")
    if snakemake.output.get("log_progress"):
        shell("cat {tmpdir}/Log.progress.out > {snakemake.output.log_progress:q}")
    if snakemake.output.get("log_final"):
        shell("cat {tmpdir}/Log.final.out > {snakemake.output.log_final:q}")
    unmapped = snakemake.output.get("unmapped")
    if unmapped:
        # SE
        if not fq2:
            unmapped = [unmapped]

        for i, out_unmapped in enumerate(unmapped, 1):
            cmd = "gzip -c" if out_unmapped.endswith("gz") else "cat"
            shell("{cmd} {tmpdir}/Unmapped.out.mate{i} > {out_unmapped}")
