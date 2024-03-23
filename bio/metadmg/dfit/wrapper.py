__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


names = snakemake.input.get("names", "")
if names:
    names = f"--names {names}"

nodes = snakemake.input.get("nodes", "")
if nodes:
    nodes = f"--nodes {nodes}"

lca_stats = snakemake.input.get("lca_stats", "")
if lca_stats:
    lca_stats = f"--lcastat {lca_stats}"


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "metaDMG-cpp dfit {snakemake.input.dmg} {names} {nodes} {lca_stats} {extra} --out_prefix {tmpdir}/out {log}"
    )

    for output in snakemake.output:
        for ext in [".dfit.txt.gz", ".dfit.stat.txt.gz", ".boot.stat.txt.gz"]:
            if output.endswith(ext):
                shell("cat {tmpdir}/out{ext} > {output}")
                continue
