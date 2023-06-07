__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import os
from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import get_samtools_opts


def get_format(path: str) -> str:
    """
    Return file format since Bowtie2 reads files that
    could be gzip'ed (extension: .gz) or bzip2'ed (extension: .bz2).
    """
    if path.endswith((".gz", ".bz2")):
        return path.split(".")[-2].lower()
    return path.split(".")[-1].lower()


bowtie2_threads = snakemake.threads - 1
if bowtie2_threads < 1:
    raise ValueError(
        f"This wrapper expected at least two threads, got {snakemake.threads}"
    )

# Setting parse_threads to false since samtools performs only
# bam compression. Thus the wrapper would use *twice* the amount
# of threads reserved by user otherwise.
samtools_opts = get_samtools_opts(snakemake, parse_threads=False)

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


n = len(snakemake.input.sample)
assert (
    n == 1 or n == 2
), "input->sample must have 1 (single-end) or 2 (paired-end) elements."

reads = ""
if n == 1:
    if get_format(snakemake.input.sample[0]) in ("bam", "sam"):
        reads = f"-b {snakemake.input.sample}"
    else:
        if snakemake.params.get("interleaved", False):
            reads = f"--interleaved {snakemake.input.sample}"
        else:
            reads = f"-U {snakemake.input.sample}"
else:
    reads = "-1 {} -2 {}".format(*snakemake.input.sample)


if all(get_format(sample) in ("fastq", "fq") for sample in snakemake.input.sample):
    extra += " -q "
elif all(get_format(sample) == "tab5" for sample in snakemake.input.sample):
    extra += " --tab5 "
elif all(get_format(sample) == "tab6" for sample in snakemake.input.sample):
    extra += " --tab6 "
elif all(
    get_format(sample) in ("fa", "mfa", "fasta") for sample in snakemake.input.sample
):
    extra += " -f "


metrics = snakemake.output.get("metrics")
if metrics:
    extra += f" --met-file {metrics} "

unaligned = snakemake.output.get("unaligned")
if unaligned:
    extra += f" --un {unaligned} "

unpaired = snakemake.output.get("unpaired")
if unpaired:
    extra += f" --al {unpaired} "

unconcordant = snakemake.output.get("unconcordant")
if unconcordant:
    extra += f" --un-conc {unconcordant} "

concordant = snakemake.output.get("concordant")
if concordant:
    extra += f" --al-conc {concordant} "


index = os.path.commonprefix(snakemake.input.idx).rstrip(".")


shell(
    "(bowtie2"
    " --threads {bowtie2_threads}"
    " {reads} "
    " -x {index}"
    " {extra}"
    "| samtools view --with-header "
    " {samtools_opts}"
    " -"
    ") {log}"
)
