__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2024, Filipe G. Vieira"
__license__ = "MIT"

import os
import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils import get_format

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


target = snakemake.input.get("target", "")
if isinstance(target, list):
    target = os.path.commonprefix(snakemake.input.target)

# TODO: arbitrary output file names
out = snakemake.output
if isinstance(out, list):
    out = os.path.commonprefix(out).rstrip("_")
else:
    format_mode = get_format(out)
    if format_mode == "tab":
        # BLAST-TAB
        format_mode = 0
    elif format_mode == "sam":
        # SAM
        format_mode = 1
    elif format_mode == "tabdb":
        # BLAST-TAB + query/db length
        format_mode = 2
    elif format_mode == "html":
        # HTML
        format_mode = 3
    else:
        # BLAST-TAB + column headers
        format_mode = 4
    extra += f" --format-mode {format_mode}"

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "mmseqs {snakemake.params.module} {snakemake.input.query} {target} {out} {tmpdir} --threads {snakemake.threads} {extra} {log}"
    )
