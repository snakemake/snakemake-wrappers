__author__ = "Curro Campuzano Jiménez"
__copyright__ = "Copyright 2023, Curro Campuzano Jiménez"
__email__ = "campuzanocurro@gmail.com"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
mem_mb = snakemake.resources.get("mem_mb", 3072)  # Default value


ref = snakemake.input.ref
if isinstance(ref, list):
    ref = " --ref ".join(ref)


reads = snakemake.input.reads
if isinstance(reads, list):
    assert len(reads) == 2, "if paired input, reads must be a list of two files"
    reads = " --reads ".join(reads)


aligned = snakemake.output.get("aligned")
if aligned:
    if isinstance(aligned, list):
        assert (
            len(aligned) == 2
        ), "if paired input, aligned must be a list of two files, if any"
        assert isinstance(
            reads, list
        ), "if paired input, reads must be a list of two files"


other = snakemake.output.get("other")
if other:
    if isinstance(other, list):
        assert (
            len(other) == 2
        ), "if paired input, other must be a list of two files, if any"
        assert isinstance(
            reads, list
        ), "if paired input, reads must be a list of two files"


# A list output means split paired output (_fwd/_rev files), which requires
# --out2; a single output file with paired input produces one interleaved file.
split_output = isinstance(aligned, list) or isinstance(other, list)


# fastx output is required whenever aligned or other reads are requested
if aligned or other:
    extra = f"--fastx {extra}"


if split_output:
    extra = f"--out2 {extra}"


# A pre-built index can be supplied as the optional `idx_dir` input so it is
# reused across runs instead of rebuilt in the (ephemeral) workdir each time.
# The per-run kvdb still lives in the temporary workdir, so it stays fresh.
idx_dir = snakemake.input.get("idx_dir")
if idx_dir:
    extra = f"--idx-dir {idx_dir} {extra}"


with tempfile.TemporaryDirectory() as temp_workdir:
    shell(
        " sortmerna --ref {ref}"
        " --reads {reads}"
        " --workdir {temp_workdir}"
        " --threads {snakemake.threads}"
        " -m {mem_mb}"
        " --aligned {temp_workdir}/aligned_reads"
        " --other {temp_workdir}/other_reads"
        " {extra}"
        " {log}"
    )

    if split_output:
        if aligned:
            # Handle the case were no alignment
            shell("mv {temp_workdir}/aligned_reads_fwd.* {aligned[0]}")
            shell("mv {temp_workdir}/aligned_reads_rev.* {aligned[1]}")
        if other:
            shell("mv {temp_workdir}/other_reads_fwd.* {other[0]}")
            shell("mv {temp_workdir}/other_reads_rev.* {other[1]}")
    else:
        if aligned:
            shell("mv {temp_workdir}/aligned_reads.f* {aligned}")
        if other:
            shell("mv {temp_workdir}/other_reads.f* {other}")

    stats = snakemake.output.get("stats")
    if stats:
        shell("mv {temp_workdir}/aligned_reads.log {stats}")
