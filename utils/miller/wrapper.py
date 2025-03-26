__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2024, Filipe G. Vieira"
__license__ = "MIT"

import os
from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import is_arg


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
input = in_file = Path(snakemake.input[0])
# Compressed
for ext, prog in compress_formats.items():
    if in_file.suffix == ext:
        io_opts += f" --prepipe {prog}"
        in_file = in_file.with_suffix("")
        break

# Delimiter
for in_format in io_formats:
    if in_file.suffix == f".{in_format}":
        io_opts += f" --i{in_format}"
        break


### OUTPUT
out_file = Path(snakemake.output[0])
output = f"> {snakemake.output[0]}"
# Compressed
for ext, prog in compress_formats.items():
    if out_file.suffix == ext:
        output = f" | {prog} {output}"
        out_file = out_file.with_suffix("")
        break

# Delimiter
for out_format in io_formats:
    if out_file.suffix == f".{out_format}":
        io_opts += f" --o{out_format}"
        break


if is_arg("cat", extra):
    input = snakemake.input
elif is_arg("split", extra):
    extra += f" --prefix {os.path.commonprefix(snakemake.output).rstrip('_')}"
    output = ""


shell("GOMAXPROCS={snakemake.threads} mlr {io_opts} {extra} {input} {output} {log}")
