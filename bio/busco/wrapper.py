"""Snakemake wrapper for BUSCO assessment"""

__author__ = "Tessa Pierce"
__copyright__ = "Copyright 2018, Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")


mode = snakemake.params.get("mode")
assert mode in [
    "genome",
    "transcriptome",
    "proteins",
], "invalid run mode: only 'genome', 'transcriptome' or 'proteins' allowed"


lineage = lineage_opt = snakemake.params.get("lineage", "")
if lineage_opt:
    lineage_opt = f"--lineage {lineage_opt}"


with tempfile.TemporaryDirectory() as tmpdir:
    dataset_dir = snakemake.input.get("dataset_dir", "")
    if not dataset_dir:
        dataset_dir = f"{tmpdir}/dataset"

    shell(
        "busco"
        " --cpu {snakemake.threads}"
        " --in {snakemake.input}"
        " --mode {mode}"
        " {lineage_opt}"
        " {extra}"
        " --download_path {dataset_dir}"
        " --out_path {tmpdir}"
        " --out output"
        " {log}"
    )

    if snakemake.output.get("short_txt"):
        assert lineage, "parameter 'lineage' is required to output 'short_tsv'"
        shell(
            "cat {tmpdir}/output/short_summary.specific.{lineage}.output.txt > {snakemake.output.short_txt:q}"
        )
    if snakemake.output.get("short_json"):
        assert lineage, "parameter 'lineage' is required to output 'short_json'"
        shell(
            "cat {tmpdir}/output/short_summary.specific.{lineage}.output.json > {snakemake.output.short_json:q}"
        )
    if snakemake.output.get("full_table"):
        assert lineage, "parameter 'lineage' is required to output 'full_table'"
        shell(
            "cat {tmpdir}/output/run_{lineage}/full_table.tsv > {snakemake.output.full_table:q}"
        )
    if snakemake.output.get("miss_list"):
        assert lineage, "parameter 'lineage' is required to output 'miss_list'"
        shell(
            "cat {tmpdir}/output/run_{lineage}/missing_busco_list.tsv > {snakemake.output.miss_list:q}"
        )
    if snakemake.output.get("out_dir"):
        shell("mv {tmpdir}/output {snakemake.output.out_dir:q}")
    if snakemake.output.get("dataset_dir"):
        shell("mv {dataset_dir} {snakemake.output.dataset_dir:q}")
