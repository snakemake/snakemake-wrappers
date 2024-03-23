__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


ref = snakemake.input.get("ref", "")
if ref:
    ref = f"--fasta {ref}"


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "metaDMG-cpp getdamage --threads {snakemake.threads} {ref} {extra} --out_prefix {tmpdir}/out {snakemake.input.aln} {log}"
    )

    for output in snakemake.output:
        for ext in [".bdamage.gz", ".res.gz", ".stat"]:
            if output.endswith(ext):
                shell("cat {tmpdir}/out{ext} > {output}")
                continue
