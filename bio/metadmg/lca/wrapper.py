__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


with tempfile.TemporaryDirectory() as tmpdir:
    shell("metaDMG-cpp lca -bam {input.aln} -names {input.names} -nodes {input.nodes} -acc2tax {input.acc2taxid} {extra} --outnames {tmpdir}/out {log}")

    if snakemake.output.get("dmg"):
        assert snakemake.output.dmg.endswith(".gz"), "'dmg' file is Gzip compressed, but extension is not '.gz'"
        shell("cat {tmpdir}/out.bdamage.gz > {snakemake.output.dmg}")

    if snakemake.output.get("lca"):
        assert snakemake.output.lca.endswith(".gz"), "'lca' file is Gzip compressed, but extension is not '.gz'"
        shell("cat {tmpdir}/out.lca.gz > {snakemake.output.lca}")

    if snakemake.output.get("stats"):
        assert not snakemake.output.stats.endswith(".gz"), "'stats' file is NOT Gzip compressed, but extension is '.gz'"
        shell("cat {tmpdir}/out.stat > {snakemake.output.stats}")

    if snakemake.output.get("log"):
        assert not snakemake.output.log.endswith(".gz"), "'log' file is NOT Gzip compressed, but extension is '.gz'"
        shell("cat {tmpdir}/out.log > {snakemake.output.log}")
