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
            "Salmon requires an equal number of paried reads in `r1` and `r2`,"
            " or a list of unpaired reads `r`"
        )


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
libtype = snakemake.params.get("libtype", "A")

extra = snakemake.params.get("extra", "")
if "--validateMappings" in extra:
    raise DeprecationWarning("`--validateMappings` is deprecated and has no effect")

r1 = snakemake.input.get("r1")
r2 = snakemake.input.get("r2")
r = snakemake.input.get("r")


if all(mate is not None for mate in [r1, r2]):
    r1 = (
        [snakemake.input.r1]
        if isinstance(snakemake.input.r1, str)
        else snakemake.input.r1
    )
    r2 = (
        [snakemake.input.r2]
        if isinstance(snakemake.input.r2, str)
        else snakemake.input.r2
    )

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

    r = [snakemake.input.r] if isinstance(snakemake.input.r, str) else snakemake.input.r
    read_cmd = " --unmatedReads {}".format(" ".join(r))

else:
    raise MissingMateError()

gene_map = ""
if "gtf" in snakemake.input.keys():
    gene_map = "--geneMap {}"

bam = ""
if "bam" in snakemake.output.keys():
    bam = "--writeMappings {}".format(snakemake.output["bam"])

outdir = dirname(snakemake.output.get("quant"))

shell(
    "salmon quant --index {snakemake.input.index} "
    " --libType {libtype} {read_cmd} --output {outdir} {gene_map} "
    " --threads {snakemake.threads} {extra} {bam} {log}"
)
