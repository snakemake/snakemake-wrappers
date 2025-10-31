__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2024, Filipe G. Vieira"
__license__ = "MIT"

import os
import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format

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
    # (0) BLAST-TAB
    # (1) SAM
    # (2) BLAST-TAB + query/db length
    # (3) HTML
    # (4) BLAST-TAB + column headers
    if format_mode == "sam":
        extra += " --format-mode 1"
    elif format_mode == "html":
        extra += " --format-mode 3"

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "mmseqs {snakemake.params.module} {snakemake.input.query} {target} {out} {tmpdir} --threads {snakemake.threads} {extra} {log}"
    )
