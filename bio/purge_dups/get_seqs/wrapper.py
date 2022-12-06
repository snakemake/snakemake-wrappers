__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


import tempfile
from pathlib import Path
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)


if Path(snakemake.input.bed).stat().st_size:
    with tempfile.TemporaryDirectory() as tmpdir:
        shell(
            "get_seqs {extra} -p {tmpdir}/out {snakemake.input.bed} {snakemake.input.fas} {log}"
        )

        if snakemake.output.get("hap"):
            shell("cat {tmpdir}/out.hap.fa > {snakemake.output.hap}")
        if snakemake.output.get("purged"):
            shell("cat {tmpdir}/out.purged.fa > {snakemake.output.purged}")
else:
    # If BED file empty, copy input to output since `get_seqs` will segfault
    log = Path(snakemake.log[0])
    log.write_text(
        "WARN: Input BED file is empty. Input FASTA file will be copied to output."
    )
    shell("cp {snakemake.input.fas} {snakemake.output.hap}")
    Path(snakemake.output.purged).touch()
