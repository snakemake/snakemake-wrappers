__author__ = "Johannes Köster and N. Tessa Pierce"
__copyright__ = "Copyright 2016, Johannes Köster and 2019, N. Tessa Pierce"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"

## modified from original wrapper to enable multiple files per sample
import os
import re
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# if multiple files, join them with ',' before mapping with bt2
r1 = snakemake.input.get("read1")
r2 = snakemake.input.get("read2")
r = snakemake.input.get("single")

assert (
    r1 is not None and r2 is not None
) or r is not None, "either r1 and r2 (paired), or r (unpaired) are required as input"
if r1:
    r1 = (
        [snakemake.input.read1]
        if isinstance(snakemake.input.read1, str)
        else snakemake.input.read1
    )
    r2 = (
        [snakemake.input.read2]
        if isinstance(snakemake.input.read2, str)
        else snakemake.input.read2
    )
    assert len(r1) == len(
        r2
    ), "input-> equal number of files required for r1 and r2"  # true?
    r1_cmd = " -1 " + ",".join(r1)
    r2_cmd = " -2 " + ",".join(r2)
    read_cmd = " ".join([r1_cmd, r2_cmd])
if r:
    assert (
        r1 is None and r2 is None
    ), "Bowtie2 cannot quantify mixed paired/unpaired input files. Please input either r1,r2 (paired) or r (unpaired)"
    r = (
        [snakemake.input.single]
        if isinstance(snakemake.input.single, str)
        else snakemake.input.single
    )
    read_cmd = " -U " + ",".join(r)

index = snakemake.input.get("index")
try:
    index_dirname = os.path.dirname(index)
    # get index prefix from index file. pattern should be <prefix>.(\d).bt2 or <prefix>.rev.(\d).bt2
    index_prefix = re.match(
        "^([^.]*).(rev.)?\d+.bt2", os.path.basename(index)
    ).groups()[0]
    index_prefix = os.path.join(index_dirname, index_prefix)
except:
    raise ValueError(
        "please index your assembly with bowtie2-build and provide an index file (e.g. with '.1.bt2' extension) via the 'index' input param"
    )

shell(
    "(bowtie2 --threads {snakemake.threads} {snakemake.params.extra} "
    "-x {index_prefix} {read_cmd} "
    "| samtools view -Sbh -o {snakemake.output[0]} -) {log}"
)
