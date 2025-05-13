__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2024, Filipe G. Vieira"
__license__ = "MIT"


import tempfile
from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import get_samtools_opts


samtools_opts = get_samtools_opts(snakemake, parse_write_index=False)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

with tempfile.TemporaryDirectory() as tmpdir:
    tmp_prefix = Path(tmpdir) / "samtools_collate"

    shell(
        "samtools collate {samtools_opts} {extra} -T {tmp_prefix} {snakemake.input[0]} {log}"
    )
