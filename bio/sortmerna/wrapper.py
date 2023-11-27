__author__ = "Curro Campuzano Jiménez"
__copyright__ = "Copyright 2023, Curro Campuzano Jiménez"
__email__ = "campuzanocurro@gmail.com"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

ref = snakemake.input.ref
reads = snakemake.input.reads
aligned = snakemake.output.get("aligned", None)
other = snakemake.output.get("other", None)
stats = snakemake.output.get("stats", None)
mem_mb = snakemake.resources.get("mem_mb", 3072)  # Default value

if isinstance(ref, list):
    ref = " --ref ".join(ref)

if aligned:
    if isinstance(aligned, list):
        assert (
            len(aligned) == 2
        ), "if paired input, aligned must be a list of two files, if any"
        assert isinstance(
            reads, list
        ), "if paired input, reads must be a list of two files"

if other:
    if isinstance(other, list):
        assert (
            len(other) == 2
        ), "if paired input, other must be a list of two files, if any"
        assert isinstance(
            reads, list
        ), "if paired input, reads must be a list of two files"
    extra = f"--fastx {extra}"

is_paired = False
if isinstance(reads, list):
    assert len(reads) == 2, "if paired input, reads must be a list of two files"
    reads = " --reads ".join(reads)
    is_paired = True

if stats:
    assert isinstance(stats, str), "stats must be a single file"


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

    if is_paired:
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
    if stats:
        shell("mv {temp_workdir}/aligned_reads.log {stats}")
