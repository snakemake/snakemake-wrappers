__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

import tempfile
from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import is_arg


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)


# Subcommands with multiple input files
if snakemake.params.command in ["concat", "common", "stats"]:
    input = " ".join(snakemake.input)
# Subcommands with a single input file (if more than one provided, concat'em all)
elif snakemake.params.command in ["stats", "sum", "rmdup", "split", "split2", "sample", "sort"]:
    input = "<(cat " + " ".join(snakemake.input) + ")"
else:
    input = snakemake.input[0]


# Extra input
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


# Extra output
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


if snakemake.params.command in ["split", "split2"]:
    # Check type of splitting
    if is_arg("-i", extra) or is_arg("--by-id", extra):
        split_by = "id"
    elif is_arg("-p", extra) or is_arg("--by-part", extra):
        split_by = "part"
    elif is_arg("-r", extra) or is_arg("--by-region", extra):
        split_by = "region"
    elif is_arg("-s", extra) or is_arg("--by-size", extra):
        split_by = "size"
    elif is_arg("-l", extra) or is_arg("--by-length", extra):
        split_by = "length"

    out_dir = Path(snakemake.output[0]).parent
    output = f"--out-dir {out_dir} --by-{split_by}-prefix output_part. --extension .fas"
else:
    if snakemake.params.get("out_bgzip"):
        assert Path(snakemake.output[0]).suffix in [
            ".gz",
            ".bgz",
            ".bgzip",
    ], "invalid output file extension"
        output = f"| bgzip --threads {snakemake.threads} > {snakemake.output[0]}"
    else:
        output = f"--out-file {snakemake.output[0]}"



shell(
    "(seqkit {snakemake.params.command}"
    " --threads {snakemake.threads}"
    " {extra_input}"
    " {extra_output}"
    " {extra}"
    " {input}"
    " {output}"
    ") {log}"
)


# Rename output files
if snakemake.params.command in ["split", "split2"]:
    for idx, output_file in enumerate(snakemake.output, start=1):
        shell("mv {out_dir}/output_part.{idx:03d}.fas {output_file}")
