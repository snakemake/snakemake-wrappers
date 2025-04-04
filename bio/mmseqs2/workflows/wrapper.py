__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2024, Filipe G. Vieira"
__license__ = "MIT"

import os
import tempfile
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


target = snakemake.input.get("target", "")
if isinstance(target, list):
    target = os.path.commonprefix(snakemake.input.target)

# TODO: arbitrary output names
module = snakemake.params.module
if snakemake.params.module == "easy-taxonomy":
    out = snakemake.output.report
elif module in ["easy-cluster", "easy-linclust"]:
    out = snakemake.output.prefix
elif module in ["easy-search", "easy-rbh"]:
    out = snakemake.output.aln
else:
    raise ValueError(f"Workflow {module} not suported.")
if isinstance(out, list):
    out = os.path.commonprefix(out).rstrip("_")


with tempfile.TemporaryDirectory() as tmpdir:
    print(
        f"mmseqs {module} {snakemake.input.query} {target} {out} {tmpdir} --threads {snakemake.threads} {extra} {log}"
    )
    shell(
        "mmseqs {module} {snakemake.input.query} {target} {out} {tmpdir} --threads {snakemake.threads} {extra} {log}"
    )
