__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import tempfile
from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_mem
from snakemake_wrapper_utils.samtools import get_samtools_opts


samtools_opts = get_samtools_opts(snakemake)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# `-m`: Approximately the maximum required memory per thread [...]
# samtools sort can use more memory than specified (e.g. https://github.com/samtools/samtools/issues/831)
mem_overhead_factor = snakemake.params.get("mem_overhead_factor", 0.1)
mem_per_thread_mb = int(
    get_mem(snakemake) / snakemake.threads * (1.0 - mem_overhead_factor)
)

with tempfile.TemporaryDirectory() as tmpdir:
    tmp_prefix = Path(tmpdir) / "samtools_sort"

    shell(
        "samtools sort {samtools_opts} -m {mem_per_thread_mb}M {extra} -T {tmp_prefix} {snakemake.input[0]} {log}"
    )
