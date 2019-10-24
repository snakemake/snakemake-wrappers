__author__ = "Johannes Köster and N Tessa Pierce"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"

## modified from original wrapper to enable multiple files per sample
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# if multiple files, join them with ',' before mapping with bt2
r1 = snakemake.input.get("r1")
r2 =  snakemake.input.get("r2")
r = snakemake.input.get("r")

assert (r1 is not None and r2 is not None) or r is not None, "either r1 and r2 (paired), or r (unpaired) are required as input"
if r1:
    r1 = [snakemake.input.r1] if isinstance(snakemake.input.r1, str) else snakemake.input.r1
    r2 = [snakemake.input.r2] if isinstance(snakemake.input.r2, str) else snakemake.input.r2
    assert len(r1) == len(r2), "input-> equal number of files required for r1 and r2" # true?
    r1_cmd = ' -1 ' + ",".join(r1)
    r2_cmd = ' -2 ' + ",".join(r2)
    read_cmd = " ".join([r1_cmd,r2_cmd])
if r:
    assert r1 is None and r2 is None, "Bowtie2 cannot quantify mixed paired/unpaired input files. Please input either r1,r2 (paired) or r (unpaired)"
    r = [snakemake.input.r] if isinstance(snakemake.input.r, str) else snakemake.input.r
    read_cmd = ' -U ' + ",".join(r)

shell(
    "(bowtie2 --threads {snakemake.threads} {snakemake.params.extra} "
    "-x {snakemake.params.index} {read_cmd} "
    "| samtools view -Sbh -o {snakemake.output[0]} -) {log}")
