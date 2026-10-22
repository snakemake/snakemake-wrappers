__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2024, Filipe G. Vieira"
__license__ = "MIT"

import os
from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format, is_arg

# The append=True is set, because we log the shell command to the log
# file manually, before the shell command is run and add its own logging.
log = snakemake.log_fmt_shell(stdout=False, stderr=True, append=True)
extra = snakemake.params.get("extra", "")


compress_formats = [
    ".gz",
    ".bz2",
    ".z",
    ".zst",
]
io_formats = [
    ".asv",
    ".asvlite",
    ".csv",
    ".csvlite",
    ".tsv",
    ".tsvlite",
    ".json",
    ".jsonl",
    ".md",
    ".markdown",
    ".nidx",
    ".pprint",
    ".usv",
    ".usvlite",
    ".xtab",
    ".dkvp",
]


io_opts = ""
### INPUT
inputs = Path(snakemake.input[0])

# check last file extension, do not use get_format as it will map compression
# extensions to the software names for compression/decompression
if inputs.suffix not in compress_formats + io_formats:
    raise ValueError(
        f"The suffix '{inputs.suffix}' of '{inputs}' is not supported by miller.\n"
        "Supported input and output formats are:\n"
        f"{io_formats}\n"
        "Supported compression formats are:\n"
        f"{compress_formats}\n"
    )


# input format
in_format = get_format(inputs, ignore_compression=True)
if f".{in_format}" not in io_formats:
    raise ValueError(
        f"The input format '{in_format}' of '{inputs}' is not supported by miller.\n"
        "Supported input and output formats are:\n"
        f"{io_formats}\n"
    )
else:
    io_opts += f" --i{in_format}"


### OUTPUT
output_path = Path(snakemake.output[0])
output = f"> {output_path}"
# Compressed
if output_path.suffix in compress_formats:
    prog = get_format(output_path, ignore_compression=False)
    output = f" | {prog} {output}"

# Delimiter
out_format = get_format(output_path, ignore_compression=True)
if f".{out_format}" not in io_formats:
    raise ValueError(
        f"The output format '{out_format}' of '{output_path}' is not supported by miller.\n"
        "Supported input and output formats are:\n"
        f"{io_formats}\n"
    )
else:
    io_opts += f" --o{out_format}"


if is_arg("cat", extra):
    # For cat operations, use all input files
    inputs = snakemake.input
elif is_arg("split", extra):
    # For split operations, add prefix based on common output prefix and clear output redirection
    extra += f" --prefix {os.path.commonprefix(snakemake.output).rstrip('_')}"
    output = ""

shell_cmd = f"GOMAXPROCS={snakemake.threads} mlr {io_opts} {extra} {inputs} {output} {log}"

with open(snakemake.log[0], 'w') as log_file:
    print(f"Will now run this shell command:\n{shell_cmd}", file=log_file)

shell(shell_cmd)
