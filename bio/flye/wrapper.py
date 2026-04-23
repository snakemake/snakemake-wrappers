__author__ = "Artur Gomes"
__copyright__ = "Copyright 2026, Artur Gomes"
__email__ = "arafaelogomes@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
import os
import shutil

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

if "--polish-target" in extra:
    raise ValueError(
        "Flye `--polish-target` mode is not supported by this wrapper. "
    )

output_dir = snakemake.params.get("dir", None)
if output_dir is None:
    raise ValueError(
        "Missing required param `dir`. " \
        "Flye assembly mode requires a dedicated output directory."
    )


def parse_bool_param(value, param_name):
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"true", "1", "yes", "y", "on"}:
            return True
        if normalized in {"false", "0", "no", "n", "off"}:
            return False

    raise ValueError(
        f"Parameter `{param_name}` must be a boolean value (true/false), got: {value!r}."
    )


keep_intermediates = parse_bool_param(
    snakemake.params.get("keep_intermediates", False), "keep_intermediates"
)

file_path = os.path.dirname(snakemake.output[0]) # probably extra pass to remove file name to stay only the path
if file_path is not None:
    if file_path != output_dir:
        raise ValueError(
            "Ambiguous outputs: `output` files must point to "
            f"`output.dir` which is `{output_dir}`. "
            f"Got `{file_path}`."
        )

input_arg = ""

seq_types = {
    "nano-raw": "--nano-raw",
    "nano-corr": "--nano-corr",
    "nano-hq": "--nano-hq",
    "pacbio-raw": "--pacbio-raw",
    "pacbio-corr": "--pacbio-corr",
    "pacbio-hifi": "--pacbio-hifi",
}

param_seq_type = snakemake.params.get("seq_type")
if not param_seq_type:
    raise ValueError(
        "Missing required parameter `seq_type`. "
        f"Must be one of: {', '.join(seq_types.keys())}"
    )

if param_seq_type in seq_types:
    input_arg += f" {seq_types[param_seq_type]}"
else:
    raise ValueError(
        f"Invalid seq_type: {param_seq_type}. Must be one of: {', '.join(seq_types.keys())}"
    )

reads = snakemake.input[0]
if reads is None:
    raise ValueError("Missing required input `reads` for Flye assembly mode.")

if isinstance(reads, list):
    reads = " ".join(reads)

input_arg += f" {reads}"

try:
    shell(
        "flye"
        " --threads {snakemake.threads}"
        " {extra}"
        " {input_arg}"
        " -o {output_dir}"
        " {log}"
    )
except Exception:
    # Do not clean intermediates on failure.
    raise

if not keep_intermediates:
    for dirname in [
        "00-assembly",
        "10-consensus",
        "20-repeat",
        "30-contigger",
        "40-polishing",
    ]:
        path = os.path.join(output_dir, dirname)
        if os.path.isdir(path):
            shutil.rmtree(path)
