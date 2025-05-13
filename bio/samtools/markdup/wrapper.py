__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2024, Filipe G. Vieira"
__license__ = "MIT"


import tempfile
from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import get_samtools_opts

samtools_opts = get_samtools_opts(snakemake, parse_output=False)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

metrics = snakemake.output.get("metrics", "")
if metrics:
    metrics = f"-f {metrics}"


with tempfile.TemporaryDirectory() as tmpdir:
    tmp_prefix = Path(tmpdir) / "samtools_markdup"
    shell(
        "samtools markdup {samtools_opts} {extra} -T {tmp_prefix} {metrics} {snakemake.input[0]} {snakemake.output[0]} {log}"
    )
