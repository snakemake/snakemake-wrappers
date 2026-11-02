__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2024, Filipe G. Vieira"
__license__ = "MIT"

import os
import tempfile
from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format, move_files

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


# Input
target = snakemake.input.get("target", "")
if isinstance(target, list):
    target = os.path.commonprefix(snakemake.input.target)


with tempfile.TemporaryDirectory() as tmpout:
    out = snakemake.output
    move_cmds = ""
    # Output
    if snakemake.params.module in ["easy_search", "easy_rbh"]:
        format_mode = get_format(out)
        # (0) BLAST-TAB
        # (1) SAM
        # (2) BLAST-TAB + query/db length
        # (3) HTML
        # (4) BLAST-TAB + column headers
        if format_mode == "sam":
            extra += " --format-mode 1"
        elif format_mode == "html":
            extra += " --format-mode 3"
    elif snakemake.params.module in ["easy-cluster", "easy-linclust"]:
        out = Path(tmpout) / "clust"
        mapping = {
            "fas": str(out) + "_all_seqs.fasta",
            "tsv": str(out) + "_cluster.tsv",
            "fas_rep": str(out) + "_rep_seq.fasta",
        }
        move_cmds = "; ".join(move_files(snakemake, mapping))
    elif snakemake.params.module == "easy-taxonomy":
        out = Path(tmpout) / "taxonomy"
        mapping = {
            "lca": str(out) + "_lca.tsv",
            "report": str(out) + "_report",
            "taln": str(out) + "_tophit_aln",
            "treport": str(out) + "_tophit_report",
        }
        move_cmds = "; ".join(move_files(snakemake, mapping))

    # Run mmseqs2
    with tempfile.TemporaryDirectory() as tmpdir:
        shell(
            "(mmseqs {snakemake.params.module} {snakemake.input.query} {target} {out} {tmpdir} --threads {snakemake.threads} {extra}; {move_cmds}) {log}"
        )
