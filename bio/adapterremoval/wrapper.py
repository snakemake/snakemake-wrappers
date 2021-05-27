__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2020, Filipe G. Vieira"
__license__ = "MIT"

from snakemake.shell import shell
from pathlib import Path
import tempfile

extra = snakemake.params.get("extra", "") + " "
adapters = snakemake.params.get("adapters", "")
collapse_pe = (
    True if "--collapse " in extra or "--collapse-deterministic " in extra else False
)
merge_singletons = snakemake.params.get("merge_singletons", False)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


# Check input files
n = len(snakemake.input.sample)
assert (
    n == 1 or n == 2
), "input->sample must have 1 (single-end) or 2 (paired-end) elements."


# Input files
if n == 1 or "--interleaved " in extra or "--interleaved-input " in extra:
    reads = "--file1 {}".format(snakemake.input.sample)
else:
    reads = "--file1 {} --file2 {}".format(*snakemake.input.sample)


# Gzip or Bzip compressed output?
compress_out = ""
if all(
    [
        Path(value).suffix == ".gz"
        for key, value in snakemake.output.items()
        if key != "settings"
    ]
):
    compress_out = "--gzip"
elif all(
    [
        Path(value).suffix == ".bz2"
        for key, value in snakemake.output.items()
        if key != "settings"
    ]
):
    compress_out = "--bzip2"
else:
    raise ValueError(
        "all output files (except for 'settings') must be compressed the same way"
    )


# Output files
if n == 1 or "--interleaved " in extra or "--interleaved-output " in extra:
    trimmed = f"--output1 {snakemake.output.fq}"
else:
    trimmed = f"--output1 {snakemake.output.fq1} --output2 {snakemake.output.fq2}"


# Collapsed reads output
if n == 2:
    trimmed += f" --singleton {snakemake.output.singleton}"
    if collapse_pe:
        if merge_singletons:
            out_collapsed = tempfile.NamedTemporaryFile()
            out_collapsed_trunc = tempfile.NamedTemporaryFile()
            trimmed += f" --outputcollapsed {out_collapsed.name} --outputcollapsedtruncated {out_collapsed_trunc.name}"
        else:
            trimmed += f" --outputcollapsed {snakemake.output.collapsed} --outputcollapsedtruncated {snakemake.output.collapsed_trunc}"


shell(
    "(AdapterRemoval --threads {snakemake.threads} "
    "{reads} "
    "{adapters} "
    "{extra} "
    "{compress_out} "
    "{trimmed} "
    "--discarded {snakemake.output.discarded} "
    "--settings {snakemake.output.settings}"
    ") {log}"
)


if collapse_pe and merge_singletons:
    shell("cat {out_collapsed.name} >> {snakemake.output.singleton}")
    out_collapsed.close()
    shell("cat {out_collapsed_trunc.name} >> {snakemake.output.singleton}")
    out_collapsed_trunc.close()
