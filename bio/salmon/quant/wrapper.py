"""Snakemake wrapper for Salmon Quant"""

__author__ = "Tessa Pierce"
__copyright__ = "Copyright 2018, Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"


from os.path import dirname
from snakemake.shell import shell


class MixedPairedUnpairedInput(Exception):
    def __init__(self):
        super().__init__(
            "Salmon cannot quantify mixed paired/unpaired input files. "
            "Please input either `r1`, `r2` (paired) or `r` (unpaired)"
        )


class MissingMateError(Exception):
    def __init__(self):
        super().__init__(
            "Salmon requires an equal number of paired reads in `r1` and `r2`,"
            " or a list of unpaired reads `r`"
        )


def uncompress_bz2(snake_io, salmon_threads):
    """
    Provide bzip2 on-the-fly decompression

    For each of these b-unzipping, a thread will be used. Therefore, the maximum number of threads given to Salmon
    shall be reduced by one in order not to be killed on a cluster.
    """

    # Asking forgiveness instead of permission
    try:
        # If no error are raised, then we have a string.
        if snake_io.endswith("bz2"):
            return [f"<( bzip2 --decompress --stdout {snake_io} )"], salmon_threads - 1
        return [snake_io], salmon_threads
    except AttributeError:
        # As an error has been raise, we have a list of fastq files.
        fq_files = []
        for fastq in snake_io:
            if fastq.endswith("bz2"):
                fq_files.append(f"<( bzip2 --decompress --stdout {fastq} )")
                salmon_threads -= 1
            else:
                fq_files.append(fastq)
        return fq_files, salmon_threads


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
libtype = snakemake.params.get("libtype", "A")
max_threads = snakemake.threads

extra = snakemake.params.get("extra", "")
if "--validateMappings" in extra:
    raise DeprecationWarning("`--validateMappings` is deprecated and has no effect")

r1 = snakemake.input.get("r1")
r2 = snakemake.input.get("r2")
r = snakemake.input.get("r")


if all(mate is not None for mate in [r1, r2]):
    r1, max_threads = uncompress_bz2(r1, max_threads)
    r2, max_threads = uncompress_bz2(r2, max_threads)

    if len(r1) != len(r2):
        raise MissingMateError()
    if r is not None:
        raise MixedPairedUnpairedInput()

    r1_cmd = " --mates1 {}".format(" ".join(r1))
    r2_cmd = " --mates2 {}".format(" ".join(r2))
    read_cmd = " ".join([r1_cmd, r2_cmd])

elif r is not None:
    if any(mate is not None for mate in [r1, r2]):
        raise MixedPairedUnpairedInput()

    r, max_threads = uncompress_bz2(r, max_threads)
    read_cmd = " --unmatedReads {}".format(" ".join(r))

else:
    raise MissingMateError()

gene_map = snakemake.input.get("gtf", "")
if gene_map:
    gene_map = f"--geneMap {gene_map}"

bam = snakemake.output.get("bam", "")
if bam:
    bam = f"--writeMappings {bam}"

outdir = dirname(snakemake.output.get("quant"))
index = snakemake.input["index"]
if isinstance(index, list):
    index = dirname(index[0])

if max_threads < 1:
    raise ValueError(
        "On-the-fly b-unzipping have raised the required number of threads. "
        f"Please request at least {1 - max_threads} more threads."
    )

shell(
    "salmon quant --index {index} "
    " --libType {libtype} {read_cmd} --output {outdir} {gene_map} "
    " --threads {max_threads} {extra} {bam} {log}"
)
