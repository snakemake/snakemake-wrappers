__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

from snakemake.shell import shell
from pathlib import Path


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# subcommands concat and common use multiple input files
if snakemake.params.command in ["concat", "common", "stats"]:
    input = " ".join(snakemake.input)
else:
    input = snakemake.input[0]

extra_input = " ".join(
    [
        (
            f"--{key.replace('_','-')} {value}"
            if key in ["bed", "gtf"]
            else f"--{key.replace('_','-')}-file {value}"
        )
        for key, value in snakemake.input.items()
    ][1:]
)

extra_output = " ".join(
    [
        (
            f"--{key.replace('_','-')} {value}"
            if key in ["read1", "read2"]
            else f"--{key.replace('_','-')}-file {value}"
        )
        for key, value in snakemake.output.items()
    ][1:]
)


if snakemake.params.get("out_bgzip"):
    assert Path(snakemake.output[0]).suffix in [
        ".gz",
        ".bgz",
        ".bgzip",
    ], "invalid output file extension"
    input = input + f" | bgzip --threads {snakemake.threads} > {snakemake.output[0]}"
else:
    input = f"--out-file {snakemake.output[0]} " + input

shell(
    "(seqkit {snakemake.params.command}"
    " --threads {snakemake.threads}"
    " {extra_input}"
    " {extra_output}"
    " {extra}"
    " {input}"
    ") {log}"
)
