__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "metaDMG-cpp lca --threads {snakemake.threads} --bam {snakemake.input.aln} --names {snakemake.input.names} --nodes {snakemake.input.nodes} --acc2tax {snakemake.input.acc2taxid} --temp {tmpdir} {extra} --out_prefix {tmpdir}/out {log}"
    )

    for output in snakemake.output:
        for ext in [".bdamage.gz", ".lca.gz", ".stat"]:
            if output.endswith(ext):
                shell("cat {tmpdir}/out{ext} > {output}")
                continue
