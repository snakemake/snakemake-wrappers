__author__ = "Kateřina Havlová"
__copyright__ = "Copyright 2026, Kateřina Havlová"
__email__ = "katkahemalova@gmail.com"
__license__ = "MIT"


import shlex
import tempfile
from pathlib import Path

from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import move_files

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Optional gap/filter BED (-f). Built-in names (hg19/hg38/mm10) can go via extra.
bed = snakemake.input.get("bed", "")
if bed:
    bed = f"-f {shlex.quote(bed)}"

# NanoVar writes several files into a working directory, naming the VCF after the
# input (e.g. <sample>.nanovar.pass.vcf). Run it in a temporary directory, then
# move the single PASS VCF to the requested output path. The temp dir is placed
# under Snakemake's `tmpdir` resource, so on HPC it can be steered to node-local
# scratch (e.g. `--default-resources tmpdir="'$SCRATCHDIR'"`).
with tempfile.TemporaryDirectory(dir=snakemake.resources.get("tmpdir")) as workdir:
    shell(
        "nanovar"
        " -t {snakemake.threads}"
        " {bed}"
        " {extra}"
        " {snakemake.input.reads:q}"
        " {snakemake.input.ref:q}"
        " {workdir:q}"
        " {log}"
    )

    # NanoVar names the VCF after the input file, mirroring its own logic
    # (src/nanovar/nanovar.py): strip .bam/.cram, or for reads split off ".f".
    name = Path(snakemake.input.reads).name
    if name.endswith(".bam"):
        prefix = name.rsplit(".bam", 1)[0]
    elif name.endswith(".cram"):
        prefix = name.rsplit(".cram", 1)[0]
    else:
        prefix = name.rsplit(".f", 1)[0]
    vcf = Path(workdir) / f"{prefix}.nanovar.pass.vcf"

    log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
    for move_cmd in move_files(snakemake, {"vcf": vcf}):
        shell("{move_cmd} {log}")
