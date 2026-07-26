__author__ = "Kateřina Havlová"
__copyright__ = "Copyright 2026, Kateřina Havlová"
__email__ = "katkahemalova@gmail.com"
__license__ = "MIT"


import shlex
import shutil
import tempfile
from pathlib import Path

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Optional gap/filter BED (-f). Built-in names (hg19/hg38/mm10) can go via extra.
filter_bed = snakemake.input.get("filter_bed", "")
if filter_bed:
    filter_bed = f"-f {shlex.quote(filter_bed)}"

# NanoVar writes several files into a working directory, naming the VCF after the
# input (e.g. <sample>.nanovar.pass.vcf). Run it in a temporary directory, then
# copy the single PASS VCF to the requested output path. The temp dir is placed
# under Snakemake's `tmpdir` resource, so on HPC it can be steered to node-local
# scratch (e.g. `--default-resources tmpdir="'$SCRATCHDIR'"`).
with tempfile.TemporaryDirectory(dir=snakemake.resources.get("tmpdir")) as workdir:
    shell(
        "nanovar"
        " -t {snakemake.threads}"
        " {filter_bed}"
        " {extra}"
        " {snakemake.input.reads:q}"
        " {snakemake.input.ref:q}"
        " {workdir:q}"
        " {log}"
    )

    hits = list(Path(workdir).glob("*.nanovar.pass.vcf"))
    if len(hits) != 1:
        raise ValueError(
            f"Expected exactly one *.nanovar.pass.vcf in {workdir}, found {len(hits)}."
        )

    shutil.copy(hits[0], snakemake.output.vcf)
