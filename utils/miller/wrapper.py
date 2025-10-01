__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2024, Filipe G. Vieira"
__license__ = "MIT"

import os
from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format, is_arg


log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")


compress_formats = {
    ".gz": "gzip",
    ".bgz": "gzip",
    ".bz2": "bzip2",
    ".xz": "xz",
}
io_formats = [
    "asv",
    "asvlite",
    "csv",
    "csvlite",
    "tsv",
    "tsvlite",
    "json",
    "jsonl",
    "md",
    "markdown",
    "nidx",
    "pprint",
    "usv",
    "usvlite",
    "xtab",
    "dkvp",
]


io_opts = ""
### INPUT
inputs = Path(snakemake.input[0])
# Compressed
for ext, prog in compress_formats.items():
    if inputs.suffix == ext:
        io_opts += f" --prepipe {prog}"
        break

# Delimiter
for in_format in io_formats:
    if get_format(inputs) == in_format:
        io_opts += f" --i{in_format}"
        break


### OUTPUT
output = f"> {snakemake.output[0]}"
# Compressed
for ext, prog in compress_formats.items():
    if Path(snakemake.output[0]).suffix == ext:
        output = f" | {prog} {output}"
        break

# Delimiter
for out_format in io_formats:
    if get_format(snakemake.output[0]) == out_format:
        io_opts += f" --o{out_format}"
        break


if is_arg("cat", extra):
    # For cat operations, use all input files
    inputs = snakemake.input
elif is_arg("split", extra):
    # For split operations, add prefix based on common output prefix and clear output redirection
    extra += f" --prefix {os.path.commonprefix(snakemake.output).rstrip('_')}"
    output = ""


shell("GOMAXPROCS={snakemake.threads} mlr {io_opts} {extra} {inputs} {output} {log}")
