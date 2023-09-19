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
    shell("metaDMG-cpp getdamage --threads {snakemake.threads} {ref} {extra} --outname {tmpdir}/out {input.aln} {log}")

    if snakemake.output.get("dmg"):
        assert snakemake.output.dmg.endswith(".gz"), "'dmg' file is Gzip compressed, but extension is not '.gz'"
        shell("cat {tmpdir}/out.bdamage.gz > {snakemake.output.dmg}")

    if snakemake.output.get("res"):
        assert snakemake.output.res.endswith(".gz"), "'res' file is Gzip compressed, but extension is not '.gz'"
        shell("cat {tmpdir}/out.res.gz > {snakemake.output.res}")

    if snakemake.output.get("stats"):
        assert not snakemake.output.stats.endswith(".gz"), "'stats' file is NOT Gzip compressed, but extension is '.gz'"
        shell("cat {tmpdir}/out.stat > {snakemake.output.stats}")
